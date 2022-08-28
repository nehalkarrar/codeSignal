'''
 You are given an array of integers a, where each element a[i] represents the length of a ribbon.

Your goal is to obtain k ribbons of the same length, by cutting the ribbons into as many pieces as you want.

Your task is to calculate the maximum integer length L for which it is possible to obtain at least k ribbons of length L by cutting the given ones.

Example

For a = [5, 2, 7, 4, 9] and k = 5, the output should be solution(a, k) = 4.


For a = [5, 2, 7, 4, 9] and k = 5, the output should be solution(a, k) = 4.

example

Here's a way to achieve 5 ribbons of length 4:

Cut the ribbon of length 5 into one ribbon of length 1 (which can be discarded) and one ribbon of length 4.
Cut the ribbon of length 7 into one ribbon of length 3 (which can be discarded) and one ribbon of length 4.
Use the existing ribbon of length 4 (no need to cut it)
Cut the ribbon of length 9 into two ribbons of length 4 (and one of length 1 which can be discarded)
Discard the ribbon of length 2.
And since it wouldn't be possible to make 5 ribbons of any greater length, the answer is 4.

For a = [1, 2, 3, 4, 9] and k = 6, the output should be solution(a, k) = 2.

Here's one way we could make 6 ribbons of length 2:

Cut the ribbon of length 9 into four ribbons of length 2 and one ribbon of length 1 (which won't be used).
Cut the ribbon of length 4 into two ribbons of length 2.
Ignore all other ribbons (1, 2, and 3). Even though ribbons with lengths 2 and 3 can also be used to obtain the ribbon of length 2, 
we don't need more than 6 ribbons of that length.
'''
def solution(a, k):
    i = 1
    while i > 0:
        count = 0
        for num in a:
            res = num // i                
            count += res
        if count == k:
            break
        i += 1
    return i