'''
Given an array of integers a, your task is to find how many of its contiguous subarrays of length m contain a pair of integers with a sum equal to k.

More formally, given the array a, your task is to count the number of indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] 
contains at least one pair (a[s], a[t]), where:

s ≠ t
a[s] + a[t] = k
For a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output should be solution(a, m, k) = 5.

Let's consider all subarrays of length m = 4 and see which fit the description conditions:

Subarray a[0..3] = [2, 4, 7, 5] doesn't contain any pair of integers with a sum of k = 10. Note that although the pair (a[3], a[3]) has the sum 5 + 5 = 10, 
it doesn't fit the requirement s ≠ t.
Subarray a[1..4] = [4, 7, 5, 3] contains the pair (a[2], a[4]), where a[2] + a[4] = 7 + 3 = 10.
Subarray a[2..5] = [7, 5, 3, 5] contains two pairs (a[2], a[4]) and (a[3], a[5]), both with a sum of k = 10.
Subarray a[3..6] = [5, 3, 5, 8] contains the pair (a[3], a[5]), where a[3] + a[5] = 5 + 5 = 10.
Subarray a[4..7] = [3, 5, 8, 5] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
Subarray a[5..8] = [5, 8, 5, 1] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
Subarray a[6..9] = [8, 5, 1, 7] doesn't contain any pair with a sum of k = 10.
So the answer is 5, because there are 5 contiguous subarrays that contain a pair with a sum of k = 10.
'''

def solution(a, m, k):
    count = 0
    for i in range(len(a)-m+1):
        suba = a[i:i+m]
        flag = False
        for j in range(m-1):
            for z in range(j+1,m):
                if suba[j] + suba[z] == k:
                    flag = True
                    break
            if flag:
                count += 1
                break
    return count