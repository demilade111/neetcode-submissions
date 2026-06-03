class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefixtotal = 1
        for i in range(n):
            result[i]=prefixtotal
            prefixtotal*=nums[i]
        suffixTotal = 1
        for i in range(n-1,-1,-1):
          result[i] *= suffixTotal
          suffixTotal*=nums[i]
        return result

        
