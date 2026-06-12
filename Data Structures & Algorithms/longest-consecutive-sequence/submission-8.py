class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newset = set(nums)
        maxLength = 0
      
        for num  in newset:
            if num-1 not in newset:
                length = 1
                while num + length in newset:
                    length+=1
                maxLength = max(length,maxLength)
        return maxLength
            




            


           
        