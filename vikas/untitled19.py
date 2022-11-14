# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 03:03:59 2022

@author: SPTINT-04
"""

import numpy as np
from functools import reduce
fib=[4,5,6,7,8,9,2,3,4,5,6,6,4]
result=map(lambda x:x-1,fib)
print (list(result))
print("largest number",max(fib))

odd_numbers=list(filter(lambda x: x%2==1,fib))
print ("odd_numbers", odd_numbers)
print ("reduse function to add series",reduce (lambda x,y:x+y, fib)) 