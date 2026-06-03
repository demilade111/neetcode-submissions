class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
        "]": "[",
        ")": "(",
        "}": "{"
       }

        for str in s:
            if str in '[({':
                stack.append(str)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if top != match[str]:
                  return False
                stack.pop()
        return len(stack) == 0





  



        