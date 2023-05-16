# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:56:48 2023

@author: suman
"""

#Bubble Sort

def Bubblesort(Arr):
    n= len(Arr)
    
    for i in range(0,n-1):
        flag =0
        for j in range(0,n-i-1):
            if(Arr[j]>Arr[j+1]):
                Arr[j],Arr[j+1] = Arr[j+1], Arr[j]
                flag =1
        if(flag==0):
            return


if __name__ == "__main__":
    
    A= [3,2,5,9,6,4,1]
    
    Bubblesort(A)
    n = len(A)
    for i in range(0,n):
        print("% d" % A[i], end=" ")
                
    