#!/usr/bin/env python
import fileinput
 
storename_cost = {}
 
for line in fileinput.input():
    data =line.strip().split("\t")
    if len(data) != 2:
        continue
    storename, cost = data
 
    if storename in storename_cost:
        storename_cost[storename].append(float(cost))
    else:
        storename_cost[storename] = []
        storename_cost[storename].append(float(cost))
 
for storename in storename_cost.keys():
    higest_cost = max(storename_cost[storename])
    lowest_cost = min(storename_cost[storename])
    print 'Store_name: %s\t Maximum Sales: %s\t Minimum Sales:  %s'% (storename, higest_cost, lowest_cost)
