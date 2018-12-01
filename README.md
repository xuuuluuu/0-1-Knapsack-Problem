# 0-1-Knapsack-Problem

0-1 Knapsack Problem | DP-10
objective: maxv and satisfiy maxw
pseudocode
define:
    vi - value of ith item
    wi - weight of ith item
    S - a max value solution to an instance of knapsack
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
