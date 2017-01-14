# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0
    for s in words:
        if len(s) > 1 and s[0] == s[-1]:
            count += 1
    return count

print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print match_ends(['aaa', 'be', 'abc', 'hello'])


def front_x(words):
    words_x = []
    words_nox = []
    for s in words:
        if s[0] == 'x':
            words_x.append(s)
        else:
            words_nox.append(s)
    return sorted(words_x) + sorted(words_nox)

print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])


def sort_last(tuples):
    return sorted(tuples, key = lambda x: x[-1])

print sort_last([(1, 3), (3, 2), (2, 1)])
print sort_last([(2, 3), (1, 2), (3, 1)])
print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])


def remove_adjacent(nums):
    nums_reduced = []
    for n in nums:
        if len(nums_reduced) == 0:
            nums_reduced.append(n)
        elif nums_reduced[-1] != n:
            nums_reduced.append(n)
    return nums_reduced

print remove_adjacent([1, 2, 2, 3])
print remove_adjacent([2, 2, 3, 3, 3])
print remove_adjacent([3, 2, 3, 3, 3])
print remove_adjacent([])


def linear_merge(list1, list2):
    return sorted(list1 + list2)

print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])

