#!/usr/bin/env python
import fileinput
payMethod_cost = {}

for line in fileinput.input():
    data =line.strip().split("\t")
    if len(data) != 2:
        continue
    payMethod, cost = data
 
    if payMethod in payMethod_cost:
        payMethod_cost[payMethod].append(float(cost))
    else:
        payMethod_cost[payMethod] = []
        payMethod_cost[payMethod].append(float(cost))

for payMethod in payMethod_cost.keys():
    average_cost = sum(payMethod_cost[payMethod])*1.0 / len(payMethod_cost[payMethod])
    total_cost = sum(payMethod_cost[payMethod])
    print 'Store_name: %s\t  total Sales:  %s\t Average Sales: %s'% (payMethod, total_cost,average_cost)
