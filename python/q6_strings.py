# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count < 10:
        return 'Number of donuts: %d' % count
    else:
        return 'many'

def both_ends(s):
    if len(s) > 1:
        return s[:2] + s[-2:]
    else:
        return ''

def fix_start(s):
    c = s[0]
    n = s.replace(s[0],'*')
    return c+n[1:]

def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]

def verbing(s):
    if len(s) > 2:
        if s[-3:] == 'ing':
            s += 'ly'
        else:
            s += 'ing'
    return s

def not_bad(s):
    i_not = s.find('not')
    i_bad = s.find('bad')
    if i_bad > i_not:
        return s.replace(s[i_not:i_bad+3],'good')
    else:
        return s

def front_back(a, b):
    a_split = len(a) - len(a)/2
    b_split = len(b) - len(b)/2
    return a[:a_split] + b[:b_split] + a[a_split:] + b[b_split:]