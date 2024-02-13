"""
Can you compute a cube as a sum?

In this Kata, you will be given a number n (where n >= 1) and your task is to find n consecutive odd numbers whose sum is exactly the cube of n.

Mathematically:
cube = n ** 3
sum = a1 + a2 + a3 + ..... + an
sum == cube
a2 == a1 + 2, a3 == a2 + 2, .......

For example:

find_summands(3) = [7,9,11] # because 7 + 9 + 11 = 27, the cube of 3. Note that there are only n = 3 elements in the array.
Write function findSummands(n) which will return an array of n consecutive odd numbers with the sum equal to the cube of n (n*n*n).
"""

# def find_summands(n):
#     # find the odd numbers after n and add them to a list
#     if n == 1:
#         return [1]
    
#     odd_num_list = []
#     last_three_items = []
#     for i in range(n, n ** 3):
#         # check if i is odd and append it to a odd_num_list
#         if i % 2 == 1:
#             odd_num_list.append(i)
#         if len(odd_num_list) >= n:
#             last_three_items = odd_num_list[-n:]
#         if sum(last_three_items[-n:]) == n ** 3:
#             return last_three_items

def find_summands(n):
    # find the odd numbers after n and add them to a list
    if n == 1:
        return [1]
    
    odd_num_list = []
    last_three_items = []

    for i in range(n, n * n * n):
        # check if i is odd and append it to odd_num_list
        if i % 2 == 1:
            odd_num_list.append(i)

        if len(odd_num_list) > n:
            odd_num_list.pop(0)  # Remove the first element to maintain a rolling window of size n

        if sum(odd_num_list) == n * n * n:
            return odd_num_list.copy()

    return None  # Return None if no such summands are found within the range

"""
Execution Timed Out (12000 ms)
Why did my code time out?
Our servers are configured to only allow a certain amount of time for your code to execute. In rare cases the server may be taking on too much work and simply wasn't able to run your code efficiently enough. Most of the time though this issue is caused by inefficient algorithms. If you see this error multiple times you should try to optimize your code further.
"""
