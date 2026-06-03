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
            if token not in  ['+','-','*','/']:
             stack.append(int(token))
            else:
                firstelement = stack.pop()
                secondElement = stack.pop()
                newValue = operations[token](secondElement,firstelement)
                stack.append(newValue)
        return stack[-1]


             
            