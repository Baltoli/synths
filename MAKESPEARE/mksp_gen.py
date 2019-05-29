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

def flatten(l):
    return [i for s in l for i in s]

# Writing a generator: I think that the important registers for my style of
# problem are 6, 2 and 0 as follows:
#   r6 is the last valid index for the first array (i.e. size - 1)
#   r2 is the first valid index for the next array (i.e. size)
#   r0 is the number of arrays - in my case 2 for now?

def to_raw(ret, inps, outp, test=False):
    len0 = len(inps[0])
    assert(all(map(lambda i: len(i) == len0, inps)))

    return {
        'test': test,
        'r7': 0, 'r6': len0 - 1, 'r2': len0,
        'r0': len(inps), 'r8': 0, 'r9': 0,
        'input_mem': flatten(inps),
        'sc_return_flag': 0, 'sc_return_val': ret,
        'output_mem_start': 0, 'output_mem': outp
    }

if __name__ == "__main__":
    print(format_example(to_raw(0, [[1, 2, 3]], [2, 4, 6])))
