#!/usr/bin/env python

import sys

last_key = ""
running_total = 0
filter_key = "ABC"

# -----------------------------------
# Loop thru file
#  --------------------------------
for input_line in sys.stdin:
    input_line = input_line.strip()

    # --------------------------------
    # Get Next Word    # --------------------------------
    this_key, value = input_line.split("\t")  #the Hadoop default is tab separates key value
                          #the split command returns a list of strings, in this case into 2 variables

    # ---------------------------------
    # Key Check part
    #    if this current key is same
    #          as the last one Consolidate
    #    otherwise  Emit
    # ---------------------------------
    if filter_key != value:     #check if key has changed ('==' is                                   #      logical equalilty check

        if last_key == this_key or last_key == "":
            calculated_value = int(value)
            running_total += calculated_value   # add value to running total
            last_key = this_key

        else:
            last_key = this_key
            running_total = int(value)

    else:
        print( "{0}\t{1}".format(this_key, running_total) )
        running_total = 0    #reset values