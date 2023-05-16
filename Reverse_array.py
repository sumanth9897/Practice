# -*- coding: utf-8 -*-
"""
Created on Mon May  1 09:49:29 2023

@author: suman
"""
#reverse an array 
def Reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -= 1
        
    
arr = [1,2,3,4,5,6,7]
Reverse(arr,0,6)
print(arr)

