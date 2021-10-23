import os
from pprint import pprint


def JFE_header(f, verbose=False):
    header = {'header':''}
    for i, line in enumerate(open(f, encoding='shift_jis').readlines(4000)):
        if '[Item]' in line:
            break
        elif '=' in line:
            k, v = line.strip('\n').split('=')
            header[k] = v
        elif '//' in line:
            header['header'] += line.strip('\n')
    if verbose: pprint(header)
    return header, i
