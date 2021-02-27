# -*- coding: utf-8 -*-
"""
Homework 1 for Python A-Z

Created: 2021.02.27 Saturday

Author: Mark Bartolo

Scenario: 
x_bar_n = E(x) when n -> infiniti
Test law of of large numbers for n random normally distributed numbers with mean = 0 and std = 1 
Count how many of these numbers fall between -1 to 1 and divide the total quantity by N
E(x) for this scenario is 68%
check that mean(x_n) -approaches-> E(x) as you rerun your script while increasing N
"""

import numpy as np
from numpy.random import randn

N = [100, 1000, 10000, 100000]
#print(randn(50))
for n in N:
    conditionmet = 0 # reset
    for i in randn(n):
        if (i >= -1 and i <= 1):
            conditionmet += 1
    answer = conditionmet / n
    print('Hits on condition: {}, n: {}, and hit ratio: {}'.format(conditionmet, n, answer))
print('that"s all folks')
