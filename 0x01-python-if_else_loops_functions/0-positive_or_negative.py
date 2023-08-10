#!/usr/bin/pyton3
import random
number = random.randint(-10, 10)
if number > 0:
    printf(f'{number} is positive')
elif number == 0:
    printf(f'{number} is zero')
else:
    printf(f'{number} is negative')
