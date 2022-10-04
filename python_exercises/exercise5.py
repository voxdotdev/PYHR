# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true 
import math
import os
import random
import re
import sys

n = input()
n = int(n)

even_or_odd = n % 2
normal_range = range(2,6)
weird_range = range(6,20)

if even_or_odd != 0: # If n is odd, print weird  
    print("Weird")
else:
    if n in weird_range: # if not odd, check if in weird range. if so, print weird.
        print("Weird")
    elif n in normal_range:
        print("Not Weird") # else, print not weird. 
    elif n > 20:
        print("Not Weird")