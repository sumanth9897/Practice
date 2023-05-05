# -*- coding: utf-8 -*-
"""
Created on Mon May  1 10:34:18 2023

@author: suman
"""
#binary search 
def BinarySearch(arr,l,r,x):
    while l<r:
        mid = (l+(r-1))//2
        
        if(arr[mid]== x):
            return mid
        
        elif(arr[mid]>x):
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == '__main__':
    arr =[1,2,3,6,7,8,92,113,412]
    x=8
    result = BinarySearch(arr, 0, len(arr)-1, x)
    print(result)
    if (result != -1):
        print("element is present at index",result)
    else:
        print("element is not present in array")
    