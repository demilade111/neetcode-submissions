class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations={
        "+": lambda a, b : a + b,
        "-": lambda a, b : a - b,
        "*": lambda a, b : a * b,
        "/": lambda a, b : int(a / b)
}
        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                second_element= stack.pop()
                first_element = stack.pop()
                result = operations[token](first_element,second_element,)
                stack.append(result)
        return stack[0] 
            


      

        