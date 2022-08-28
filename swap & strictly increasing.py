'''
You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. 
If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

Example

For numbers = [1, 5, 10, 20], the output should be solution(numbers) = true.

The initial array is already strictly increasing, so no actions are required.

For numbers = [1, 3, 900, 10], the output should be solution(numbers) = true.

By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. 
So the updated array will look like [1, 3, 9, 10], which is strictly increasing.
'''
def solution(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            digits = list(str(numbers[i]))
            digits = [i for i in digits if i != "0"]
            if len(digits) > 1:
                leading = min(digits)
                l_indx = digits.index(leading)
                digits[0], digits[l_indx] = digits[l_indx], digits[0]                
            numbers[i] = int("".join(digits))
            if i == 0 :
                continue
            elif numbers[i-1] < numbers[i] < numbers[i+1]:
                continue
            else:
                return False
    return True