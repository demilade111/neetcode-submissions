class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
             if j != i:
                total*=nums[j]
            result[i]=total
        return result

        


        