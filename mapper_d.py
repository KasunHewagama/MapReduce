#!/usr/bin/env python
import string
import fileinput
for line in fileinput.input():
    data =line.strip().split(",")
    if len(data) ==6:
        date, time, Storename, item, cost, payMethod = data
        print"{0}\t{1}".format(Storename, cost)
