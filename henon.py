__author__ = 'Yash'

'''
    x[n+1] = 1 - a*x[n]*x[n] + y[n]
    y[n+1] = b*x[n]
    a = 1.4, b = 0.3
'''

import sys
import numpy as np
from matplotlib import pyplot as plt

class henon():
    def __init__(self, a, b, x, y):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def next_point(self):
        xn = self.x
        yn = self.y
        self.x = 1 - self.a*xn*xn + yn
        self.y = self.b*xn
        return self.x

    def curr_point(self):
        return [self.x, self.y]

def phase_diag(h_obj, count, f_name):

    plot_points = np.zeros([count, 2])

    for i in range(count):
        plot_points[i, :] = h_obj.curr_point()
        try:
            h_obj.next_point()
        except Exception as e:
            print("Can't find next point")


    #np.savetxt(f_name, plot_points, delimiter=',')
    #plt.axis([0, 1, 0, 1])
    plt.plot(plot_points[:, 0], plot_points[:, 1], ',')
    plt.show()

def bifurcation():
    print("In progress")
    #use step size function

def plotting():
    plt.axis([0, 1, 0, 1])

def main():
    option = int(input("Plot: 1.Phase Diagram 2.Bifurcation Diagram \n"))
    if option == 1:
        try:
            a = 1.4#float(input("a = "))
            b = 0.3
            xi = 0#float(input("initial x = "))
            yi = 0#float(input("initial x = "))
            #num_iter = int(input("number of iterations = "))
            count = 10000000#int(input("size = "))
            file = "test_henon.csv"#input("filename.csv: ")
        except Exception as e:
            print("Error in input")
            sys.exit(0)

        h = henon(a, b, xi, yi)
        print("Henon Map with a=" + "{:.9f}".format(a) + " b=" + "{:.9f}".format(b) + " x=" + "{:.9f}".format(xi) + " y=" + "{:.9f}".format(yi))
        phase_diag(h, count, file)

    if option == 2:
        bifurcation()

if __name__ == '__main__': main()
