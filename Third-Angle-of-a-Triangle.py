"""
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle
"""
def other_angle(a, b):
    total_angles = 180
    return total_angles - (a + b)