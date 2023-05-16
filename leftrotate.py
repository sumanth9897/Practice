# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:51:17 2023

@author: suman
"""

#left rotate d elements in an array 
def leftr(arr,d,n):
    k = arr.index(d)
    print(k)
    new_list = []
    new_list = arr[k+1:]+arr[:k+1]
    return new_list

if __name__ =='__main__':
    arr = [1,3,4,6,8,9,12,45,65]
    n= len(arr)
    arr = leftr(arr, 9, n)
    for i in range(0,n):
        print(arr[i],end=" ")