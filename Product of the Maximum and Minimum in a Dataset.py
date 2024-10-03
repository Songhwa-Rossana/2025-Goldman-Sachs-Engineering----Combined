#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY x
#

def maxMin(operations, x):
    # Write your code here
    elements = set()
    max_val = float('-inf')
    min_val = float('inf')
    result = []
    
    for i in range(len(operations)):
        if operations[i] == 'push':
            elements.add(x[i])
            max_val = max(max_val, x[i])
            min_val = min(min_val, x[i])
        else: 
            elements.remove(x[i])
            if not elements:
                max_val = float('-inf')
                min_val = float('inf')
            else:
                max_val = max(elements)
                min_val = min(elements)
        result.append(max_val * min_val)
        
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    result = maxMin(operations, x)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
