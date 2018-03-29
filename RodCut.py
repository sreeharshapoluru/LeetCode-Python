# CLRS Dynamic Programming

import sys
# Rod Cut Problem - iteratively
def RodCut(price,rodLen):
    if(rodLen == 0):
        return 0
    profit = -(sys.maxsize) - 1
    for i in range(1,rodLen+1):
        profit = max(profit,price[i]+RodCut(price,rodLen-i))
    return profit

# Rod Cut problem  - top down memoization
def RodCut(price,rodLen):
    returns = [(-sys.maxsize)-1]*(rodLen+1)               
    return RodCutMemoized(price,rodLen,returns)

def RodCutMemoized(p,n,r):
    if(p[n] >= 0):
        return p[n]
    if(n == 0):
        return 0
    else:
        profit = -(sys.maxsize)-1
    for i in range(1,n+1):
        profit = max(profit,p[i]+RodCutMemoized(p,n-i,r))
    r[n] = profit
    return profit

# Rod Cut problem - bottom up
def RodCut(price,rodLen):
    returns = [-(sys.maxsize)-1]*(rodLen+1)
    returns[0] = 0
    for i in range(1,rodLen+1):
        profit = -(sys.maxsize)-1
        for j in range(1,i+1):
            profit = max(profit,price[j]+returns[i-j])
        returns[i] = profit
    return returns[rodLen]

     
    


        

    
    