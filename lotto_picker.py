#! python3
__author__ = 'Casey'
# lotto number generator
# test

import random

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
power_ball = 0


my_list = []                               # create a new list
while len(my_list) < 6:                    # while it has fewer than 6 elements...
    new_number = random.randrange(49)+1    # store the new number in a variable
    if not new_number in my_list:          # actually almost plain english
        my_list.append(new_number)         # put it in the list!
winners = sorted(my_list)
print(winners)
'''
num1 = random.randint(1,10)      # get random number between 1 and 50
print('num1 = ' + (str(num1)))

num2 = random.randint(1,10)      # get random number between 1 and 50
while num2 == num1:
    num2 = random.randint(1,10)
    print('Second try for num2 ' + (str(num2)))
print('num2 = ' + (str(num2)))

num3 = random.randint(1,10)      # get random number between 1 and 50
while num3 == num1 or num2:
    num3 = random.randint(1,10)
    print('Second try for num3 ' + (str(num3)))
    if num3 != num1 or num2:
        break
print('num3 = ' + (str(num3)))
'''


'''
num1 = random.randint(1,50)      # get random number between 1 and 50
print('num1 = ' + (str(num1)))

num2 = random.randint(1,50)      # get random number between 1 and 50
if num2 == num1:
    num2 = random.randint(1, 50)
    print('Second try for num2 ' + (str(num2)))

else:
    num2 = random.randint(1, 50)
    print('num2 = ' + (str(num2)))

num3 = random.randint(1,50)      # get random number between 1 and 50
if num3 != num1 or num2:
    print('num3 = ' + (str(num3)))
else:
    num3 = random.randint(1,50)
    print('Second try for num3 ' + (str(num3)))

num4 = random.randint(1,50)      # get random number between 1 and 50
if num4 != num1 or num2 or num3:
    print('num4 = ' + (str(num4)))
else:
    num4 = random.randint(1,50)
    print('Second try for num4 ' + (str(num4)))

num5 = random.randint(1,50)      # get random number between 1 and 50
if num5 != num1 or num2 or num3 or num4:
    print('num5 = ' + (str(num5)))
else:
    num5 = random.randint(1,50)
    print('Second try for num5 ' + (str(num5)))

num6 = random.randint(1,50)      # get random number between 1 and 50
if num6 != num1 or num2 or num3 or num4 or num5:
    print('num6 = ' + (str(num6)))
else:
    num6 = random.randint(1,50)
    print('Second try for num6 ' + (str(num6)))
'''




