#!/usr/bin/env python
import sys

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0].strip()   #key is first item in list
    value_in   = key_value[1].strip()   #value is 2nd item

    #print key_in
    if  (value_in[0:3] == 'ABC') or (value_in.isdigit()):           #if this entry has <date word> in key
        print( '%s\t%s' % (key_in, value_in) )  #print a string, tab, and string


#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value