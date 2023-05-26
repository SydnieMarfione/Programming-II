#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

n=100 
def main():
    lst = [10, 100, 1000, 5000, 10000, 20000]
    print("%12s%16s%12s"%("Problem Size","Iterations","Seconds"))
    
    a = 5
    b = 6
    c = 10
     
    for l in lst:
        n = l
        count = 0 
        
        start = time.time()
        for i in range(n):
            for j in range(n):
                x = i * i
                y = j * j 
                z = i * j 
                count += 1
        for k in range(n):
            w = a * k + 45 
            v = b * b
            count+= 1
            
        end = time.time()
        total = end - start
        
        
        print("%12s%16s%12s"%(n,count,total))    
            
            
        print(n,count)

main()


# In[ ]:




