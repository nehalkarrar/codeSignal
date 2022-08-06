'''
You are given an array of strings arr. Your task is to construct a string from the words in arr, 
starting with the 0th character from each word (in the order they appear in arr), followed by the 1st character, then the 2nd character, etc. 
If one of the words doesn't have an ith character, skip that word.

Return the resulting string.

Example

For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".

First, we append all 0th characters and obtain string "DRHP";
Then we append all 1st characters and obtain string "DRHPaoyo";
Then we append all 2nd characters and obtain string "DRHPaoyoisap";
Then we append all 3rd characters and obtain string "DRHPaoyoisapaecp";
Then we append all 4th characters and obtain string "DRHPaoyoisapaecpyiy";
Finally, only letters in the arr[2] are left, so we append the rest characters and get "DRHPaoyoisapaecpyiynth"
'''
def solution(arr):
    res = []
    maxim = max(arr, key=len)
    
    for word in arr:
        new = list(word)
        if len(new) < len(maxim):
            while len(new) < len(maxim):
                new.append(" ")
        res.append(new)
    
    tlist = list(zip(*res))
    new_str = []
    for el in tlist:
        for chr in el:
            new_str.append(chr)
    
    final = "".join(new_str)
        
    return final.replace(" ", "")