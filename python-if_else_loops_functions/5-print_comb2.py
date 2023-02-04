#!/usr/bin/python3
for l in range(00, 99 + 1):
    if l == 99:    
        print("{}".format(l))
    else:    
        print("{:02}".format(l), end=', ')
