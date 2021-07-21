
import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    my_dict, frequencies = defaultdict(int), defaultdict(int)
    returnvalues = []
    for query, value in queries:
        if query == 1:
            my_dict[value] += 1
            frequencies[my_dict[value]] += 1
            frequencies[my_dict[value] - 1] -= 1
        elif query == 2 and my_dict[value] != 0:
            my_dict[value] -= 1
            frequencies[my_dict[value]] += 1
            frequencies[my_dict[value] + 1] -= 1
        elif query == 3:
            returnvalues.append(1 if frequencies[value] > 0 else 0)
    return returnvalues