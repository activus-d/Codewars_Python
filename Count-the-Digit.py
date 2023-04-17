"""
n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
"""
def nb_dig(n, d):
    k = ''
    for x in range((n+1)):
        sqr_root = str(x * x)
        for y in sqr_root:
            if y == str(d):
                k += y
        
    return len(k)

nb_dig(5750, 2)