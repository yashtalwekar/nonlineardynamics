__author__ = 'Yash'
'''
    x[n+1] = a*x[n]*(1 - x[n])
'''

import sys
import numpy as np
from matplotlib import pyplot as plt

class logistic():
    def __init__(self, a, x):
        self.x = x
        self.a = a

    def next_point(self):
        xn = self.x
        self.x = (self.a)*xn*(1 - xn)
        return self.x

    def curr_point(self):
        return self.x

def cobweb(l_obj, count, f_name):

    plot_points = np.zeros([count*2, 2])

    for i in range(count):
        plot_points[2*i][0] = l_obj.curr_point()
        plot_points[2*i][1] = l_obj.next_point()
        plot_points[2*i+1][0] = l_obj.curr_point()
        plot_points[2*i+1][1] = l_obj.curr_point()


    #np.savetxt(f_name, plot_points, delimiter=',')
    plt.axis([0, 1, 0, 1])
    plt.plot(plot_points[:, 0], plot_points[:, 1], '-')
    plt.show()

def bifurcation():
    print("In progress")

    #use step size function

def plotting():
    plt.axis([0, 1, 0, 1])

def main():
    option = int(input("Plot: 1.Cobweb Diagram 2.Bifurcation Diagram \n"))
    if option == 1:
        try:
            a = 3.3#float(input("a = "))
            xi = 0.61#float(input("initial x = "))
            #num_iter = int(input("number of iterations = "))
            count = 10000#int(input("size = "))
            file = "test.csv"#input("filename.csv: ")
        except Exception as e:
            print("Error in input")
            sys.exit(0)

        l = logistic(a, xi)
        print("Logistic Map with a=" + "{:.9f}".format(a) + " x=" + "{:.9f}".format(xi))
        cobweb(l, count, file)

    if option == 2:
        bifurcation()

if __name__ == '__main__': main()
