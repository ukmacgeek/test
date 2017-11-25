#!/usr/bin/python

from random import randint

player = raw_input('rock (r) , paper (p) , stone (s)?')
print player + ' vs '

chosen = randint(1,3)
print(chosen)

if chosen == 1:
   computer = 'r'
elif chosen == 2:
   computer = 'p'
else:
   computer = 's'

print (computer)

if player == computer:
   print('DRAW!!')