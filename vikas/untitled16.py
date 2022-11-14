# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 02:19:59 2022

@author: SPTINT-04
"""

fib=[0,5,8,5,6,7,8,6,6,7,8,9,9,2]
odd_numbers=list(filter(lambda x: x%2==1,fib))
even_numbers=list(filter(lambda x: x%2==0,fib))
print ("even_numbers", even_numbers)
print ("odd_numbers", odd_numbers)