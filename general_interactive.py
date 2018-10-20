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

sys_name = input("Enter system name")

# Ask user to specify the variables in the equations
t = sp.symbols('t')
in_var = input("Enter dependent variables, with 't' independent, separated by spaces:\n")
var = sp.symbols(in_var)

# Ask user to specify the parameters in the equations
in_par = input("Enter parameters involved, separated by spaces:\n")
par = sp.symbols(in_par)

# Ask for parameter values
in_par_val = input("Enter parameter values in the above order, separated by spaces:\n")
par_val = list(map(float,in_par_val.split(' ')))

# Ask for equations using above info
in_deq = []
for v in var:
    in_deq.append(input("dot(" + str(v) + ") = "))

# Make a class for the system
class dynsys():
    def __init__(self, vars, pars, par_vals, eqs):
        self.vars = vars
        self.num_vars = len(self.vars)
        self.par_dict = dict(zip(pars, par_vals))
        self.eqs = [parse_expr(eq) for eq in eqs]
    
    def var_dots(self, var_val, **kwargs):
        var_dict = dict(zip(self.vars, var_val))
        return [elem.evalf(subs={**var_dict, **self.par_dict, **kwargs}) for elem in self.eqs]

    def time_evolution(self):
        t_step = float(input("Enter time step: "))
        num_iter = int(input("Enter number of iterations: "))
        tt = float(input("Enter time to start from: "))
        points = np.zeros([num_iter, self.num_vars])
        points[0, :] = valid_input(float, "Enter starting state, separated by spaces: ", self.num_vars)

        # nth column for nth variable
        k = np.zeros([self.num_vars, 4])
        for i in range(0, num_iter - 1):
            k[0, :] = self.var_dots(points[i, :], t= tt)
            k[1, :] = self.var_dots(points[i, :] + 0.5*k[0, :], t= tt + 0.5*t_step)
            k[2, :] = self.var_dots(points[i, :] + 0.5*k[1, :], t= tt + 0.5*t_step)
            k[3, :] = self.var_dots(points[i, :] + k[2, :], t= tt + t_step)

            points[i+1, :] = points[i, :] + (t_step/6)*(k[0, :] + 2*k[1, :] + 2*k[2, :] + k[3, :])
            tt += t_step
        
        np.savetxt(sys_name + ".csv", points, delimiter=',')

