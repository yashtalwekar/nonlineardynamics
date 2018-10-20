__author__ = 'Yash'

import numpy as np
from matplotlib import pyplot as plt

class duffing():
    def __init__(self, a, b, f, w0_sq, w):
        self.a = a
        self.b = b
        self.f = f
        self.w0_sq = w0_sq
        self.w = w

    def y_dot(self, t, x, y):
        return -1*self.a*y - self.w0_sq*x - self.b*x*x*x + self.f*np.sin(self.w*t)

    def x_dot(self, y):
        return y

def main():
    t_step = 0.1
    num_iter = 100
    points = np.zeros([num_iter, 2])
    points[0, :] = [-1, 0]
    t = 0

    duff = duffing(0.5, 1, 0.42, -1, 1)
    k_x = [0, 0, 0, 0]
    k_y = [0, 0, 0, 0]

    for i in range(0, num_iter - 1):
        k_x[0] = duff.x_dot(points[i, 1])
        k_y[0] = duff.y_dot(t, points[i, 0], points[i, 1])

        k_x[1] = duff.x_dot(points[i, 1] + k_y[0]*t_step/2)
        k_y[1] = duff.y_dot(t + t_step/2, points[i, 0] + k_x[0]*t_step/2, points[i, 1] + k_x[0]*t_step/2)

        k_x[2] = duff.x_dot(points[i, 1] + k_y[1]*t_step/2)
        k_y[2] = duff.y_dot(t + t_step/2, points[i, 0] + k_x[1]*t_step/2, points[i, 1] + k_y[1]*t_step/2)

        k_x[3] = duff.x_dot(points[i, 1] + k_y[2]*t_step)
        k_y[3] = duff.y_dot(t + t_step, points[i, 0] + k_x[2]*t_step, points[i, 1] + k_y[2]*t_step)

        points[i+1, :] += points[i, :] + [(t_step/6)*(k_x[0] + 2*k_x[1] + 2*k_x[2] + k_x[3]), (t_step/6)*(k_y[0] + 2*k_y[1] + 2*k_y[2] + k_y[3])]
        t += t_step

        progress = int(100*i/num_iter)
        print("\r", progress, "%", end="")

    plt.plot(points[:, 0], points[:, 1], ',')
    plt.show()
    # np.savetxt("duff.csv", points, delimiter=',')

if __name__ == '__main__':main()