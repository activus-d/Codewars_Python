"""
Related to MrZizoScream's Product Array kata. You might want to solve that one first :)

This is an adaptation of a problem I came across on LeetCode.

Given an array of numbers, your task is to return a new array where each index (new_array[i]) is equal to the product of the original array, except for the number at that index (array[i]).

Two things to keep in mind:

Zeroes will be making their way into some of the arrays you are given
O(n²) solutions will not pass.
All input arrays will be valid arrays of nonzero length.

Examples:

[1, 2, 3, 4]              => [24, 12, 8, 6]
[2, 3, 4, 5]              => [60, 40, 30, 24]
[1, 1, 1]                 => [1, 1, 1]
[9, 0, -2]                => [0, -18, 0]
[0, -99, 0]               => [0, 0, 0]
[3, 14, 9, 11, 11]        => [15246, 3267, 5082, 4158, 4158]
[-8, 1, 5, 13, -1]        => [-65, 520, 104, 40, -520]
[4, 7, 3, 6, 2, 14, 7, 5] => [123480, 70560, 164640, 82320, 246960,
"""

def product_sans_n(arr):
    n = len(arr)
    result = [1] * n  # Initialize a list with all elements as 1

    # Calculate the product of all elements to the left of the current index
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= arr[i]

     # Calculate the product of all elements to the right of the current index
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]
        
    return result