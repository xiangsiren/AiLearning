#! /usr/bin/env python
# -*- coding: utf-8 -*-


import math

"""
归并算法练习
"""
def mergsort(arr):

    if len(arr) < 2:
        return arr

    mid = math.floor(len(arr) / 2)

    left, right = arr[:mid], arr[mid:]

    left_s, right_s = mergsort(left),mergsort(right)

    result = []

    while left_s and right_s:
        if left_s[0] <= right_s[0]:
            result.append(left_s.pop(0))
        else:
            result.append(right_s.pop(0))
    while left_s:
        result.append(left_s.pop(0))
    while right_s:
        result.append(right_s.pop(0))

    return result


if __name__ == '__main__':

    arr = [23,33,2,4,5,77,24,3,9]

    print(mergsort(arr))
