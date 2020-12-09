#!/usr/bin/env python
import fileinput

product_cost = {}

for line in fileinput.input():
    data =line.strip().split("\t")
    if len(data) != 2:
        continue
 
    ptype, cost = data
 
    if ptype in product_cost:
        product_cost[ptype].append(float(cost))
    else:
        product_cost[ptype] = []
        product_cost[ptype].append(float(cost))

for ptype in product_cost.keys():
    average_cost = sum(product_cost[ptype])*1.0 / len(product_cost[ptype])
    total_cost = sum(product_cost[ptype])
    print 'Store_Type: %s\t  Total Sales:  %s\t Average Sales: %s'%( ptype, total_cost,average_cost)
