class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
         seen = set()
         current_length = 0
         for j in range(i,len(s)):
            if s[j] not in seen:
             seen.add(s[j])
             current_length += 1
             length = max(length,current_length)
            else:
                break
        return length 
            
              
          


        