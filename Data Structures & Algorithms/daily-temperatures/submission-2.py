class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]* n
        stack = []
        for current_day in range(n):
            current_temperatuure = temperatures[current_day]
            while len(stack) > 0:
                waiting_time = stack[-1]
                waiting_tempersture= temperatures[waiting_time]
                if current_temperatuure > waiting_tempersture:
                    stack.pop()
                    result[waiting_time] = current_day - waiting_time
                else:
                    break
            stack.append(current_day)
        return  result 
        



        