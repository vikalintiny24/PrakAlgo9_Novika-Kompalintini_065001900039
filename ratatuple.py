# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:56:55 2021

@author: vikal
"""
tuple1 = ((5,5,5,5),(3,3,3,3),(4,4,4,4),(2,2,2,2))
print("Tuple 1 :\n",tuple1)
print("Rata-rata nilai pada masing-masing tuple :\n",[sum(t)/len(t) for t in tuple1])