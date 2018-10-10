#! usr/bin/env python 3
#coinFlip2 - simulates a coin flip.

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the result! Type either heads or tails:')
    guess = input()
x = ['heads', 'tails']
toss = random.choice(x)
if toss == guess:
    print('Success!')
else:
    print('Badluck! Try again.')
    guess = input()
    if toss == guess:
        print('Success!')
    else:
        print('Badluck! You are not very lucky today.')

