__author__ = 'Yash'

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class lorenz():
    def __init__(self, sig, r, b):
        self.sig = sig
        self.r = r
        self.b = b

    def x_dot(self, x, y):
        return np.float_(self.sig*(y - x))

    def y_dot(self, x, y, z):
        return np.float_((self.r)*x - y - x*z)

    def z_dot(self, x, y, z):
        return np.float_(-1*(self.b)*z + x*y)

def main():
    num_iter = 100000
    points = np.zeros([num_iter, 3])

    lor = lorenz(10, 27.1, 2.66667)
    points[0, :] = [25, 18, 120]
    h = 0.01

    kx = np.zeros([4], dtype=np.float_)
    ky = np.zeros([4], dtype=np.float_)
    kz = np.zeros([4], dtype=np.float_)

    for i in range(0, num_iter - 1):
        kx[0] = lor.x_dot(points[i, 0], points[i, 1])
        ky[0] = lor.y_dot(points[i, 0], points[i, 1], points[i, 2])
        kz[0] = lor.z_dot(points[i, 0], points[i, 1], points[i, 2])

        kx[1] = lor.x_dot(points[i, 0] + kx[0]*h/2, points[i, 1] + ky[0]*h/2)
        ky[1] = lor.y_dot(points[i, 0] + kx[0]*h/2, points[i, 1] + ky[0]*h/2, points[i, 2] + kz[0]*h/2)
        kz[1] = lor.z_dot(points[i, 0] + kx[0]*h/2, points[i, 1] + ky[0]*h/2, points[i, 2] + kz[0]*h/2)

        kx[2] = lor.x_dot(points[i, 0] + kx[1]*h/2, points[i, 1] + ky[1]*h/2)
        ky[2] = lor.y_dot(points[i, 0] + kx[1]*h/2, points[i, 1] + ky[1]*h/2, points[i, 2] + kz[1]*h/2)
        kz[2] = lor.z_dot(points[i, 0] + kx[1]*h/2, points[i, 1] + ky[1]*h/2, points[i, 2] + kz[1]*h/2)

        kx[3] = lor.x_dot(points[i, 0] + kx[2]*h, points[i, 1] + ky[2]*h)
        ky[3] = lor.y_dot(points[i, 0] + kx[2]*h, points[i, 1] + ky[2]*h, points[i, 2] + kz[2]*h)
        kz[3] = lor.z_dot(points[i, 0] + kx[2]*h, points[i, 1] + ky[2]*h, points[i, 2] + kz[2]*h)

        points[i+1, :] += points[i, :] + [(h/6)*(kx[0] + 2*kx[1] + 2*kx[2] + kx[3]), (h/6)*(ky[0] + 2*ky[1] + 2*ky[2] + ky[3]), (h/6)*(kz[0] + 2*kz[1] + 2*kz[2] + kz[3])]
'''
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(points[:, 0], points[:, 1], points[:, 2])
    #ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=2)
    #plt.plot(points[:, 0], points[:, 1], '-')
    #plt.show()
    np.savetxt("lor.dat", points, delimiter=' ')
'''
if __name__ == '__main__':main()
