# -*- coding: utf-8 -*-
"""
Homework 2 Financial Statement Analysis for Python A-Z

Created: 2021.02.27 Saturday

Author: Mark Bartolo

Scenario: 
Assess the financial statement of organization X
Given two lists of data for the financial year:
    Monthly revenue
    Monthly expenses
Calculate the following metrics:
    Profit for ea. month
    profit after tax for ea. month (tax rate is 30%)
    profit margin for ea. month == profit after tax divided by revenue
    good months- profit after tax was greater than the mean for the year
    bad months- where the profit after the tax was less than the mean for the year
    the best month- profit after tax was max for the year
    the worst month- profit after tax was min for the year

Results to presented as a list
calculted at $0.01 precision
presented in units of $1,000 (1k) [no decimal points]
Note: warned that tax may be negative for any given month (aka deferred tax asset)
"""
import pandas as pd
from Python_Homework_3_Data import revenue, expenses

#print(revenue)
#print(expenses)
# calculate profit as revenue - expenses
# operations with two lists, 'the difficult' way
profit = list([])
for i in range(0, len(revenue)):
    profit.append(round(revenue[i] - expenses[i], 2))
#print('profit: ')
#print(profit)

# Calculate tax as 30% of profit 
tax = list([ round(i* 0.3, 2) for i in profit ])
#print('tax: ')
#print(tax)

# profit after tax 
profit_after_tax = list([])
# operations with two lists using list comprehension
for i in range(0,len(profit)):
    profit_after_tax.append(round(profit[i] - tax[i], 2)) 
#print('Profit after tax: ')
#print(profit_after_tax)

# profit margin
# Profit after tax divided by revenue
profit_margin = []
[profit_margin.append(profit_after_tax[i]/revenue[i]) for i in range(0,len(profit_after_tax))]
profit_margin = [round(i*100, 2) for i in profit_margin] # convert to percentage

# calculate the mean profit for the year
mean_profit_after_tax = round(sum(profit_after_tax)/len(profit_after_tax), 2)
#print('mean_profit_after_tax: ')
#print(mean_profit_after_tax)

# first attempt was to pass either T or F in each cell
# good months- profit after tax was greater than the mean for the year
good_months = []
for i in range(0,len(profit_after_tax)):
    # no need for if statement, since printing T/F
    good_months.append(profit_after_tax[i] > mean_profit_after_tax)

# bad months- where the profit after the tax was less than the mean for the year
bad_months = []
for i in range(0,len(profit_after_tax)):
    bad_months.append(profit_after_tax[i] < mean_profit_after_tax)

# the best month- profit after tax was max for the year, list T/F
best_month = list([])
for i in range(0,len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax)) 

# the worst month- profit after tax was min for the year
worst_month = list([])
for i in range(0,len(profit)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax)) 
#convert all calculations to units of one thousand dollars
#revenue_1000 = [ round(revenue[i], -2) for i in range(0,len(revenue))]
revenue_1000 = [ round(i/1000, 2) for i in revenue]
revenue_1000 = [ int(i) for i in revenue_1000]

expenses_1000 = [ round(i/1000, 2) for i in expenses]
expenses_1000 = [int(i) for i in expenses_1000]

profit_1000 = [ round(i/1000, 2 ) for i in profit]
profit_1000 = [int(i) for i in profit_1000]

profit_after_tax_1000 = [ round(i/1000, 2 ) for i in profit_after_tax]
profit_after_tax_1000 = [ int(i) for i in profit_after_tax_1000]

print('Revenue (1k): ')
print(revenue_1000)
print('Expenses (1k): ')
print(expenses_1000)
print('Profit (1k): ')
print(profit_1000)
print('Profit after tax (1k): ')
print(profit_after_tax_1000)
print('Profit margin: ')
print(profit_margin)
print('good months: ')
print(good_months)
print('bad months: ')
print(bad_months)
print('best month: {}'.format(best_month)) 
print('worst month: {}'.format(worst_month))