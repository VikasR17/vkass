# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 03:55:59 2022

@author: SPTINT-04
"""

import numpy as np
arr1=np.array([10,20,30,40,50])
print(arr1)
arr2=np.array([[10,20,30],[30,40,50],[70,70,80]])
print(arr2)
arr3=np.array([[15,4,5,-5,6,7,],[2,3,4,5,99,-44]])
print(arr3)
print('the sum of array 1,2,3 respectively:')
print(arr1.sum())

print(arr2.sum())
print(arr3.sum())
print('the average of array 1,2,3  respectively:')
print(np.average(arr1))
print(np.average(arr2))
print(np.average(arr3))
print('the min of array1 and max of array2:')
print(arr1.min())
print(arr2.max())