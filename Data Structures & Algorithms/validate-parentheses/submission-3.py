class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for char in s:
            if char in pair:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if pair[top] != char:
                    return False
                stack.pop()
        return len(stack) == 0