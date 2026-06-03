class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
               return [hashmap[complement],i]
            hashmap[num] = i
    




# # // nums = [3,4,5,6], target = 7
# #  Output: [0,1]

# we create a hashmap , empty hashmap

# for each of the element in the array , substract the target from the elemt=result

# then we check hashmap

# if the result is in the hasmap, then return the current index and the complement value










