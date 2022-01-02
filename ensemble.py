#!/usr/bin/python
#
# Author: Alexander Castro
# Description: A Python implementation of the ensemble method
#

import operator
from functools import reduce
from collections import Counter
from math import factorial

def num_permutations(l):
    '''Count number of permutations for a list'''
    num = factorial(len(l))
    mults = Counter(l).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num / den

def ensemble(num_models,success_rate,failure_rate):
    '''Performs ensemble probability calculations'''
    total_error_probability = 0

    for v_count in range(0,num_models//2 + 1):
        # generate the lists to create permutations of
        x_count = num_models - v_count
        predict_list = ["x"] * x_count + ["v"] * v_count
        perm_count = num_permutations(predict_list)
        probability = perm_count * (failure_rate**x_count) * (success_rate**v_count)
        total_error_probability += probability

        print("\nCorrect predictions:",x_count," Incorrect predictions:",v_count)
        print("Number of permutations: ", perm_count)
        print("Error Probability:",perm_count,"* (",failure_rate,"^",x_count,") * (",success_rate,"^",v_count,") =", probability)

    return total_error_probability

# Define our model characteristics
num_models = 25 # Number of models used
success_rate = 0.45 # Success rate of models used
failure_rate = 0.55 # Failure rate of models used

error_probability = ensemble(num_models,success_rate,failure_rate)

print('\nError rate: ', round(100*error_probability,2), "%")
print('Success rate: ', round(100*(1-error_probability),2), "%")
