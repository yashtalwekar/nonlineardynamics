import sys
import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt

def valid_input(func, prompt, len_var):
    while True:
        try:
            tmp_var = list(map(func, input(prompt).split()))
        except:
            print("Invalid input, please try again")
            continue
        if len(tmp_var) is len_var:
            return tmp_var
        else:
            print("Invalid input, please try again")
            continue

in_filename = input("File name: ")
dsysfile = [elem[:-1] for elem in open(in_filename, 'r').readlines()[::-1]]

dsys_name = dsysfile.pop()

# Ask user to specify the variables in the equations
t = sp.symbols('t')
in_var = dsysfile.pop()
var = sp.symbols(in_var)

# Ask user to specify the parameters in the equations
in_par = dsysfile.pop()
par = sp.symbols(in_par)

# Ask for parameter values
in_par_val = dsysfile.pop()
par_val = list(map(float,in_par_val.split(' ')))

# Ask for equations using above info
in_deq = []
for v in var:
    in_deq.append(dsysfile.pop())

# Print system
print(dsys_name)
for v in range(0, len(var)):
    print("dot(" + str(var[v]) + ") = " + in_deq[v])

# Make a class for the system
class dynsys():
    def __init__(self, vars, pars, par_vals, eqs):
        self.vars = vars
        self.num_vars = len(self.vars)
        self.par_dict = dict(zip(pars, par_vals))
        self.eqs = [parse_expr(eq) for eq in eqs]
        self.points_evolved = []
    
    def var_dots(self, var_val, **kwargs):
        var_dict = dict(zip(self.vars, var_val))
        return [elem.subs({**var_dict, **self.par_dict, **kwargs}).evalf() for elem in self.eqs]

    def time_evolution(self):
        t_step = float(input("Enter time step: "))
        num_iter = int(input("Enter number of iterations: "))
        tt = float(input("Enter time to start from: "))
        self.points_evolved = np.zeros([num_iter, self.num_vars + 1])    # Storing time in the 0th column
        self.points_evolved[0, :] = [tt, *valid_input(float, "Enter starting state, separated by spaces: ", self.num_vars)]
        
        # nth column for nth variable
        k = np.zeros([4, self.num_vars])
        for i in range(0, num_iter - 1):
            k[0, :] = self.var_dots(self.points_evolved[i, 1:], t= tt)
            k[1, :] = self.var_dots(self.points_evolved[i, 1:] + 0.5*k[0, :], t= tt + 0.5*t_step)
            k[2, :] = self.var_dots(self.points_evolved[i, 1:] + 0.5*k[1, :], t= tt + 0.5*t_step)
            k[3, :] = self.var_dots(self.points_evolved[i, 1:] + k[2, :], t= tt + t_step)

            self.points_evolved[i+1, 1:] = self.points_evolved[i, 1:] + (t_step/6)*(k[0, :] + 2*k[1, :] + 2*k[2, :] + k[3, :])
            tt += t_step
            self.points_evolved[i+1, 0] = tt
            
            integration_progress = int(100*i/num_iter)
            print("\rIntegrating... [{}{}] {}%".format('#'*int(integration_progress/5), '-'*(20-int(integration_progress/5)), integration_progress), end="")
            sys.stdout.flush()
        print("\rIntegrating... [{}] 100%".format('#'*20))
            
    def time_evolution_plots(self, ax_x, ax_y, save_to_file=False):
        plt.plot(self.points_evolved[:, ax_x], self.points_evolved[:, ax_y])
        plt.show()

        if save_to_file is not None:
            np.savetxt("{}.csv".format(save_to_file), self.points_evolved, delimiter=',')
    

dsys_obj = dynsys(var, par, par_val, in_deq)
dsys_obj.time_evolution()
dsys_obj.time_evolution_plots(1, 2, save_to_file=True)
