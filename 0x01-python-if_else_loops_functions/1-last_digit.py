#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % -10
else:
    last_digit = number % 10
message = 'Last digit of' number, 'is', last_digit '.'
if last_digit == 0:
    print(message, 'and is 0')
elif last_digit > 5:
    print(message, 'greater than 5')
else:
    print(message, 'less than and not 0')
