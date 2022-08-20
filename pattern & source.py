'''
You are given two strings - pattern and source. The first string pattern contains only the symbols 0 and 1, 
and the second string source contains only lowercase English letters.

Let's say that pattern matches a substring source[l..r] of source if the following three conditions are met:

they have equal length,
for each 0 in pattern the corresponding letter in the substring is a vowel,
for each 1 in pattern the corresponding letter is a consonant.
Your task is to calculate the number of substrings of source that match pattern.

Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
'''

def solution(pattern, source):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    flag = False
    for i in range(len(source)-len(pattern)+1):
        subs = source[i:i+len(pattern)]
        for j in range(len(pattern)):
            if len(subs) == len(pattern):
                if (pattern[j] == "0" and subs[j] in vowels) or (pattern[j] == "1" and subs[j] not in vowels):
                    flag = True
                else:
                    flag = False
                    break
        if flag:
            count += 1
    return count
            