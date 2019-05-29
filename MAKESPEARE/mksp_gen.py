#!/usr/bin/env python3

import csv
import random

def header():
    return [
        'Train=0/test=1',
        'r7', 'r6', 'r2', 'r0', 'r8', 'r9',
        'mem size', 'input memory',
        'scalar return flag', 'scalar return val',
        'output memory start', 'output memory size', 'output memory'
    ]

def format_example(ex):
    row = []

    if ex['test']:
        row.append(1)
    else:
        row.append(0)

    [row.append(ex['r{}'.format(r)]) for r in [7, 6, 2, 0, 8, 9]]

    row.append(len(ex['input_mem']))
    row.append(' '.join(map(str, ex['input_mem'])))

    row.append(ex['sc_return_flag'])
    row.append(ex['sc_return_val'])

    row.append(ex['output_mem_start'])
    row.append(len(ex['output_mem']))
    row.append(' '.join(map(str, ex['output_mem'])))

    return row

# Writing a generator: I think that the important registers for my style of
# problem are 6, 2 and 0 as follows:
#   r6 is the last valid index for the first array (i.e. size - 1)
#   r2 is the first valid index for the next array (i.e. size)
#   r0 is the number of arrays - in my case 2 for now?

# TODO
def add_one(length):
    return {
        'test': False,
        'r7': 0, 'r6': length - 1, 'r2': length,
        'r0': 2, 'r8': 0, 'r9': 0
    }

def generate_many(gen_f, max_len = 20):
    pass 

if __name__ == "__main__":
    ex = {
        'test': False,
        'r7': 3, 'r6': 2, 'r2': 1, 
        'r0': 8, 'r8': 0, 'r9': 9,
        'input_mem': [1, 2, 3],
        'sc_return_flag': 0,
        'sc_return_val': 0,
        'output_mem_start': 0,
        'output_mem': [4, 5, 6]
    }
    print(format_example(ex))
