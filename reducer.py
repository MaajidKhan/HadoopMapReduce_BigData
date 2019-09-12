#!/usr/bin/python

import sys

sales_total = 0
old_key = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data = line.strip().split("\t")
	
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_key, this_sale = data

    if old_key and old_Key != this_key:
        print "#{0}\t{1}".format(old_key, sales_total)
        sales_total = 0

    old_key = this_key
    sales_total += float(this_sale)

if old_key != None:
    print "#{0}\t{1}".format(old_key, sales_total)