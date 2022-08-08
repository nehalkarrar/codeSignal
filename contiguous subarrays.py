'''
You are given an array of integers arr. Your task is to count the number of contiguous subarrays, 
such that elements of the subarray are arranged in strictly decreasing order.

For example, if arr = [9, 8, 4, 9, 3], then the subarray [9, 8, 4] meets the criteria (9 > 8 > 4), but the subarray [8, 4, 9] does not.
Example

For arr = [9, 8, 7, 6, 5], the output should be solution(arr) = 15.

All contiguous subarrays satisfy the condition of problem, because all elements of the array are arranged in decreasing order. 
There are 15 possible contiguous subarrays, so the answer is 15.

For arr = [10, 10, 10], the output should be solution(arr) = 3.
'''

'''
def solution(arr):
    res = []
    x = len(arr)
    
    while x > 0:
        test_arr = arr[:x]
        test_arr.sort(reverse = True)
        if arr[:x] == test_arr:
            res = test_arr
            break
        x -= 1
        
    count = 0
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if res[i] > res[j]:
                count += 1
        
    if count == 0:
        return len(arr)
    else:
        return count+len(res)
'''
def solution(arr):
    
    x = 1
    
    while x <= len(arr):
        test_arr = arr[:x]
        test_arr.sort(reverse = True)
        if arr[:x] == test_arr:
            res = []
            res.extend(arr[:x])
        else:
            break
        x += 1
        
    count = 0
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if res[i] > res[j]:
                count += 1
        
    if count == 0:
        return len(arr)
    else:
        return count+len(res)
        