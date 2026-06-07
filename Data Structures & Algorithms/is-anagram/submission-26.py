class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      newDict = {}
      for char  in s:
          newDict[char] = newDict.get(char, 0) + 1
      for char in t:
        if char not in newDict:
          return False
        newDict[char]-=1
      for char in newDict.values():
        if char != 0:
          return False
      return True
