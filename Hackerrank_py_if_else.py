#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    #n = 22
    #modulus operator to see if remainder, we know that odd will have a remainder and even will not
    if n % 2 == 1:
        print("Weird")
    #we now can check even knowing modulus will have zero remainder and we can use range where its start, end and what to skip by interating to go through all possibilities
    elif n % 2 == 0 and n in range(2,5,2):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6,21,2):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")