from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: quick check on lengths
        if len(s) != len(t):
            return False
        
        # Step 2: count characters in s
        hashmapCount = Counter(s)
        
        # Step 3: subtract counts using t
        for char in t:
            if char not in hashmapCount:
                return False
            hashmapCount[char] -= 1
            if hashmapCount[char] < 0:
                return False
        
        # Step 4: after processing all chars, verify all counts are zero
        for value in hashmapCount.values():
            if value != 0:
                return False
        
        return True
