'''
You are implementing your own programming language and you've decided to add support for merging strings. 
A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained 
by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".
Example

For s1 = "dce" and s2 = "cccbd", the output should be
solution(s1, s2) = "dcecccbd".
All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.

For s1 = "super" and s2 = "tower", the output should be
solution(s1, s2) = "stouperwer".
Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.
'''
def solution(s1, s2):
    new = []
    i = 0
    j = 0
    while True:
        if s1.count(s1[i]) < s2.count(s2[i]):
            new.append(s1[i])
            i += 1
        else:
            new.append(s2[j])
            j += 1
        if i == len(s1):
            rem = s2[j:]
            new.extend(rem)
            break
        elif j == len(s2):
            rem = s1[i:]
            new.extend(rem)
            break 
    return "".join(new)
           