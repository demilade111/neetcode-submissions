class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set() 
        maxLength = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength 


       



        



Input: s = "zxyzxyz"

Output: 3



