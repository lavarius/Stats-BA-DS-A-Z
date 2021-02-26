# -*- coding: utf-8 -*-
"""
Homework 2 from Statistics for Business Analytics and Data Science A-Z

Created: 2021.02.25 Thursday

Author: Mark Bartolo

Scenario: 
Use central limit theorem concepts
Calculate Z-Score
mean: $95.70
standard deviation = $1,247.00
100 trades per week
"""

# import some libraries
import math

n = 100 # 100 trades per week
mu_x = 95.70 # mean
sigma = 1247.00 # standard deviation
sigma_x = sigma/math.sqrt(n)
x_gain = 20000.00/n
x_loss = -95.71/n

z_gain = (x_gain - mu_x)/sigma_x
z_loss = (x_loss-mu_x)/sigma_x
print('sigma_x is: ' + str(sigma_x))
print('z_gain is: ' + str(z_gain))
print('z_loss is: ' + str(z_loss))
print('Referencing a Z-Score Table:')
print('Probability for gaining $20k, where,')
print('P(x>x_gain) = 1-0.80 = 0.20, 20%') 
print('P(x<0) = .22 , 22%')

# Question 7
N=121
mu_x = 34
sigma = 4.1
sigma_x = sigma/math.sqrt(N)
print('std of samplels N is: ' + str(sigma_x))

# Question 6
N=100
mu_x = 192
sigma = 8
sigma_x = sigma/math.sqrt(N)
print('std of samplels N is: ' + str(sigma_x))
x_crit = 193.6
z_score = (x_crit - mu_x)/sigma_x
print('z_score is: ' + str(z_score))