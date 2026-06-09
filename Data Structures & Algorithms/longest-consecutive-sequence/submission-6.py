class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        length = 1
        longest = 1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                length+=1
                longest = max(length, longest)
            elif  nums[i] - nums[i-1] > 1:
                length = 1
        return longest


     
        



