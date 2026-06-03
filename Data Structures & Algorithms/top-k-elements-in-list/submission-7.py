class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sortedValues = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        k = [item[0] for item in sortedValues[:k]]

        return k
       
        