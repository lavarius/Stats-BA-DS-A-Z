# -*- coding: utf-8 -*-
"""
Homework 3 from Statistics for Business Analytics and Data Science A-Z

Created: 2021.02.26 Friday

Author: Mark Bartolo

Scenario: 
with alpha at 95%, prove:
defects p < 18%
N = 150 spoons
defect # spoons : 23
H0 : >= 18% are defective
H1 : < 18% are defective
"""
import math
N = 150 # sampled spoons
p_hat = 23/150

# 2 Checks 
# 1. p_hat * N > 10
print('p_hat: {}'.format(p_hat))
print('p_hat * N: {}'.format(p_hat * N)) # 23 > 10
# 2. N * q_hat > 10
q_hat = 1 - p_hat
print('q_hat: {}'.format(q_hat))
print('q_hat * N: {}'.format(q_hat * N)) # 127 > 10

# p = .18, the hypothesis we want to test
mu = 0.18
q = 1 - mu # 0.82
sigma = math.sqrt(mu*q)
print('sigma: {}'.format(sigma))

sigma_phat = sigma/math.sqrt(N)
print('sigma_phat: {}'.format(sigma_phat))

z_hat = (p_hat - mu)/sigma_phat 
print('z_hat: {}'.format(z_hat))
    
# P is 19.22 % which is > 5 and therefore there is not enough evidence to reject H0