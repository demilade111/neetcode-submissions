class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for temp in range(len(temperatures)):
            while stack and temperatures[temp] > stack[-1][1]:
                popIndex, popTemperature = stack.pop()
                result[popIndex] = temp - popIndex
            stack.append((temp,temperatures[temp]))
        return result
        