from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for char in strs:
            sortedvalue = ''.join(sorted(char))
            hashmap[sortedvalue].append(char)
        return list(hashmap.values())


        



