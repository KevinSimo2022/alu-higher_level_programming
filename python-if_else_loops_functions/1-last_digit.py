#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
LastNumber = number%10
if LastNumber > 5:
    print('Last digit of' , number, 'is', LastNumber , 'and is greater than 5')
elif LastNumber == 0:
    print('Last digit of', number, 'is', LastNumber , 'and is 0')
elif LastNumber < 6 !=0:
    print('Last digit of' , number, 'is', LastNumber , 'and is less than 6 and not 0')
=======
if number%10 > 5:
    print('Last digit of', number, 'is', number%10, 'and is greater than 5')
elif number%10 == 0:
    print('Last digit of', number, 'is', number%10, 'and is 0')
elif number%10 < 6 !=0:
    print('Last digit of', number, 'is', number%10, 'and is less than 6 and not 0')
>>>>>>> 518b8fc2aab98525b1a84827828f835663ba256a
