class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        
        for current_day in range(n):
            current_temp = temperatures[current_day]
            
            while len(stack) > 0:
                waiting_day = stack[-1]
                waiting_temp = temperatures[waiting_day]
                
                if current_temp > waiting_temp:
                    stack.pop()
                    result[waiting_day] = current_day - waiting_day
                else:
                    break
            
            stack.append(current_day)  
        
        return result