class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            if sort in hashMap:
               hashMap[sort].append(strs[i])
            else:
                hashMap[sort]= [strs[i]]
        return list(hashMap.values())
   


        