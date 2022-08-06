'''
Given an array of integers a, your task is to count the number of pairs i and j (where 0 ≤ i < j < a.length), such that a[i] and a[j] are digit anagrams.

Two integers are considered to be digit anagrams if they contain the same digits. In other words, 
one can be obtained from the other by rearranging the digits (or trivially, if the numbers are equal). 
For example, 54275 and 45572 are digit anagrams, but 321 and 782 are not (since they don't contain the same digits). 
220 and 22 are also not considered as digit anagrams, since they don't even have the same number of digits.

Example

For a = [25, 35, 872, 228, 53, 278, 872], the output should be solution(a) = 4.

There are 4 pairs of digit anagrams:

a[1] = 35 and a[4] = 53 (i = 1 and j = 4),
a[2] = 872 and a[5] = 278 (i = 2 and j = 5),
a[2] = 872 and a[6] = 872 (i = 2 and j = 6),
a[5] = 278 and a[6] = 872 (i = 5 and j = 6).
'''

def solution(a):
    count = 0
    for i in range(len(a)-1):
        lst1 = list(str(a[i]))
        lst1.sort()
        for j in range(i+1, len(a)):
            lst2 = list(str(a[j]))
            lst2.sort()
            if lst1 == lst2:
                count += 1
    return count