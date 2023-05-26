#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time 

n = 100

# define list of sizes to test
lst = [10, 100, 1000, 5000, 10000, 20000]


def main():
    print("Problem Size  Iterations   Seconds")  
    
    # iterate over problem sizes
    for n in lst:
        count = 0  # initialize counter variable
        
        # start timing loop
        start = time.time()
        
        # iterate over all numbers from 0 to n-1
        for i in range(n):
            for j in range(n):
                # calculations
                x = i * i
                y = j * j
                z = i * j
                count += 1  # increment the counter variable
        
        # iterate over all numbers from 0 to n-1
        for k in range(n):
            w = 5 * k + 45
            v = 6 * 6
            count += 1
        
        # stop timing loop
        end = time.time()
        
        # calculate total time taken
        total = end - start
        
        # print results
        print(f"{n:<13}{count:<12}{total:.6f}")


main()


# In[ ]:




