'''
Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j) 
such that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.

Note: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8, etc. are considered to be powers of 2
Example

For numbers = [1, -1, 2, 3], the output should be solution(numbers) = 5.
There is one pair of indices where the corresponding elements sum up to 20 = 1:
(1, 2): numbers[1] + numbers[2] = -1 + 2 = 1
There are two pairs of indices where the corresponding elements sum up to 21 = 2:
(0, 0): numbers[0] + numbers[0] = 1 + 1 = 2
(1, 3): numbers[1] + numbers[3] = -1 + 3 = 2
There are two pairs of indices where the corresponding elements sum up to 22 = 4:
(0, 3): numbers[0] + numbers[3] = 1 + 3 = 4
(2, 2): numbers[2] + numbers[2] = 2 + 2 = 4
In total, there are 1 + 2 + 2 = 5 pairs summing up to powers of two.
For numbers = [2], the output should be solution(numbers) = 1.
The only pair of indices is (0, 0) and the sum of corresponding elements is equal to 22 = 4. So, the answer is 1.
For numbers = [-2, -1, 0, 1, 2], the output should be solution(numbers) = 5.
There are two pairs of indices where the corresponding elements sum up to 20 = 1: (2, 3) and (1, 4)
There are two pairs of indices where the corresponding elements sum up to 21 = 2: (2, 4) and (3, 3)
There is one pair of indices where the corresponding elements sum up to 22 = 4: (4, 4)
In total, there are 2 + 2 + 1 = 5 pairs summing up to powers of 2
'''

def solution(numbers):
    def isPowerOfTwo(n):
        if (n == 0):
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
        return True
    
    counter = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i <= j:
                temp = numbers[i] + numbers[j]
                if isPowerOfTwo(temp):
                    counter += 1
            
    return counter 
                

'''
def solution(numbers):   
    counter = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i <= j:
                temp = numbers[i] + numbers[j]
                if (temp & (temp-1) == 0) and temp != 0:
                    counter += 1
            
    return counter 
                
'''
             