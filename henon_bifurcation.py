__author__ = 'Yash'
import numpy as np
from matplotlib import pyplot as plt

step_size_a = 0.0001
max_a = 1.4
size = 1 + (max_a/step_size_a)
shift_factor = 2
A = np.linspace(0, max_a, size, endpoint=True)#, retstep=True)

max_num_points = 1000
num_skip = 10000
err_lim = 0.00000001
pt_initial = [0, 0]

results = -shift_factor*np.ones([size*max_num_points, 2])
ath_num = 0
index_results = 0
next_a_begins_at = 0

def henon(a_, pt_):
    b_ = 0.3
    temp_x = 1 - a_*pt_[0]*pt_[0] + pt_[1]
    temp_y = b_*pt_[0]
    return [temp_x, temp_y]

for a in A:
    count = 0
    pt = pt_initial
    err = 1
    flag_first_log = 0
    for i in range (0, num_skip +max_num_points):
        pt = henon(a, pt)
        if count >= num_skip:
            #results[ath_num *100 + i - num_skip][1] = y
            if flag_first_log == 1:
                err = np.absolute(pt[0] - results[next_a_begins_at][1])        #previous values for convergence check, regenerated in each a
                if err < err_lim:
                    next_a_begins_at = index_results
                    break
            flag_first_log = 1
            results[index_results][1] = pt[0]
            results[index_results][0] = ath_num
            index_results += 1

        count += 1
    ath_num += step_size_a

#print(results)
#np.savetxt("untrimmed.csv", results, delimiter=',')
results += shift_factor
results = results[results.all(1)]
results -= shift_factor
np.savetxt("trimmed.csv", results, delimiter=',')
print(index_results)
plt.plot(results[:, 0], results[:, 1], ',')
plt.show()

