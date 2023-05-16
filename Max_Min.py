# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:18:57 2023

@author: suman
"""

#maximum and minimum element of an array 
def maxmin(arr,n):
    
    max = arr[0]
    min = arr[0]
    for i in range(0,n):
        if(arr[i]<min):
            min = arr[i]
        elif(arr[i]>max):
            max = arr[i]
            
    Maxmin = [max,min]
    print(Maxmin)

arr = [1,4,5,7,3,8,9,19]
n = len(arr)
print(n)
maxmin(arr,n)
