"""
Created on Sat Dec  1 13:23:08 2018

@author: xu_lu
"""

'''
0-1 Knapsack Problem | DP-10
objective: maxv and satisfiy maxw
pseudocode
define:
    s - a max value solution to an instance of knapsack
    V(i, x) - value of the best solution on that:
        1 use only the first i items
        2 has total size of x
base case:
    V(i, x) = 0
recursive case:
    case 1: i not belong to S
    case 2: i belong to S
    
    V(i, x) = V(i-1, x)         if case 1  &  if x < wi
            = Vi + V(i-1, x-wi) if case 2 
'''
import numpy as np
v = [6, 10, 12]
w = [1, 2, 3]
maxw = 5

def backpack(n, v, w, maxw):
    vmatrix = np.zeros((maxw+1, n+1))
    for i in range(1, n+1):
        for x in range(maxw+1):
            if x < w[i-1]:
                vmatrix[x, i] = vmatrix[x, i-1]
            else:
                vmatrix[x, i] = max(vmatrix[x, i-1], v[i-1] + vmatrix[x-w[i-1], i-1])
    return vmatrix
print (backpack(3, v, w, maxw))
