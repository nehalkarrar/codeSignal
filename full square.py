'''
An integer n is called a full square, if there exists some integer s, such that n = s * s. Examples of full squares are 0, 1, 4, 9, 16, etc.

Given an array of distinct integers numbers, your task is to find the number of pairs of indices (i, j) 
such that i ≤ j and the sum numbers[i] + numbers[j] is a full square.

Example

For numbers = [-1, 18, 3, 1, 5], the output should be solution(numbers) = 4.

There is one pair of indices where the corresponding elements sum up to 0:

(0, 3): numbers[0] + numbers[3] = -1 + 1 = 0.
There are two pairs of indices where the corresponding elements sum up to 4:

(0, 4): numbers[0] + numbers[4] = -1 + 5 = 4;
(2, 3): numbers[2] + numbers[3] = 3 + 1 = 4.
There is one pair of indices where the corresponding elements sum up to 36:

(1, 1): numbers[1] + numbers[1] = 18 + 18 = 36;
In total, there are 1 + 2 + 1 = 4 pairs summing up to full squares.
'''

import math
def solution(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i <= j:
                summ = numbers[i] + numbers[j]
                if summ >= 0:
                    root = math.sqrt(summ)
                    if int(root + 0.5) ** 2 == summ:
                        count += 1
    return count
