#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LNum = number % 10
if LNum > 5:
    print('Last digit of', number, 'is', LNum, 'and is greater than 5')
elif LNum == 0:
    print('Last digit of', number, 'is', LNum, 'and is 0')
elif LNum < 6 != 0:
    print('Last digit of', number, 'is', LNum, 'and is less than 6 and not 0')
