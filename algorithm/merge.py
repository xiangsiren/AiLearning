#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
归并排序
"""
import math


def mergeSort(arr):

    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    print(left,"---",right)
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    print(result)
    return result


if __name__ == '__main__':

    arr = [23,33,2,4,5,77,24,3,9]


    print(mergeSort(arr))
