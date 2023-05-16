# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:27:27 2023

@author: suman
"""

#insertion sort 
def Insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
            
        arr[j+1] = key
        
    print(arr)

if __name__ == "__main__":
    
    A = [64, 34, 25, 12, 22, 11, 90]
    
    Insertion(A)
   
        
        