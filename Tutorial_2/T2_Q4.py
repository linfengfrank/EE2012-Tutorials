import numpy as np
import matplotlib.pyplot as plt

P_B  = 1e-4 # prior
P_B_ = 1- P_B
P_A_B = 0.99 # sensitivity 
P_A_B_ = 0.1 # false positive rate

num = 10
P_B_A_array = np.zeros((num, 1))


for i in range (1, num):
    print(i)
    # Bayes' theorem
    P_B_A = P_A_B * P_B / ( P_A_B * P_B  + P_A_B_ * P_B_ ) 

    P_B_A_array[i] = P_B_A

    P_B = P_B_A  # update next prior using current posterior pobability
    P_B_ = 1- P_B 

print(P_B_A_array)

plt.plot(P_B_A_array)
plt.xlabel('The number of tested positive')
plt.ylabel('P(B|A)')
plt.grid(True)
plt.show()


