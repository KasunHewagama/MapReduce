#!/usr/bin/env python

import fileinput
StoreName_cost = {}

for line in fileinput.input():
    data =line.strip().split("\t")
    if len(data) != 2:
        continue
 
    storename, cost = data
 
    if storename in StoreName_cost:
        StoreName_cost[storename].append(float(cost))
    else:
        StoreName_cost[storename] = []
        StoreName_cost[storename].append(float(cost))
 
for storename in StoreName_cost.keys():
    average_cost = sum(StoreName_cost[storename])*1.0 / len(StoreName_cost[storename])
    total_cost = sum(StoreName_cost[storename])
    print 'Store_name: %s\t  total Sales:  %s\t Average Sales: %s'% (storename, total_cost,average_cost)
