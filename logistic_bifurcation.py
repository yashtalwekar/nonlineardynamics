__author__ = 'Yash'
import numpy as np
from matplotlib import pyplot as plt

step_size_a = 0.001
size = 1 + (4/step_size_a)
A = np.linspace(0, 4, size, endpoint=True)#, retstep=True)

max_num_points = 1000
num_skip = 10000
err_lim = 0.00000001
x_initial = 0.5

results = -1*np.ones([size*max_num_points, 2])
ath_num = 0
index_results = 0
next_a_begins_at = 0

def logistic(b, x):
    return b*x*(1-x)

for a in A:
    count = 0
    x = x_initial
    err = 1
    flag_first_log = 0
    for i in range (0, num_skip +max_num_points):
        y = logistic(a, x)
        if count >= num_skip:
            #results[ath_num *100 + i - num_skip][1] = y
            if flag_first_log == 1:
                err = np.absolute(y - results[next_a_begins_at][1])        #previous values for convergence check, regenerated in each a
                if err < err_lim:
                    next_a_begins_at = index_results
                    break
            flag_first_log = 1
            results[index_results][1] = y
            results[index_results][0] = ath_num
            index_results += 1

        x = y
        count += 1
    ath_num += step_size_a

#print(results)
#np.savetxt("untrimmed.csv", results, delimiter=',')
results += 1
results = results[results.all(1)]
results -= 1
#np.savetxt("trimmed.csv", results, delimiter=',')
plt.plot(results[:, 0], results[:, 1], ',')
plt.show()
