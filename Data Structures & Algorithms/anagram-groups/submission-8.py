class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dict = {}
      for str in strs:
        sortedValue = ''.join(sorted(str))
        if sortedValue in dict:
          dict[sortedValue].append(str)
        else:
         dict[sortedValue] = [str]
      return list(dict.values())


        
