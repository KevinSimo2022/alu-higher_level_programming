#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LNum = abs(number) % 10
if  number < 0:
    LNum = -LNum
print('Last digit of' , number, 'is', LNum, 'and is end=')
if LNum > 5:
    print('Last digit of', number, 'is', LNum, 'and is greater than 5')
elif LNum == 0:
    print('Last digit of', number, 'is', LNum, 'and is 0')
