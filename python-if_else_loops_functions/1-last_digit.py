#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastNumber = number %10
if LastNumber > 5:
    print('Last digit of', number, 'is', LastNumber, 'and is greater than 5')
elif LastNumber == 0:
    print('Last digit of', number, 'is', LastNumber, 'and is 0')
elif LastNumber < 6 != 0:
    print('Last digit of', number, 'is', LastNumber, 'and is less than 6 and not 0')
