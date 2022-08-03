'''
You are given an array of integers a and an integer k. Your task is to calculate the number of ways to pick two different indices i < j, 
such that a[i] + a[j] is divisible by k
'''

def solution(a, k):
    count = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            res = a[i] + a[j]
            if res % k == 0:
                count +=1
    return count
