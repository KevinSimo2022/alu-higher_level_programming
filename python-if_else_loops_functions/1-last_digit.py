#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print('Last digit of', number, 'is', number[:-1] )
if number[5:] < number[:-1] < 5:
    if number[0:] == number[:-1] == 0: 
        if 6 > number[:-1] != 0:
            print('and is less than 6 and not 0')
            