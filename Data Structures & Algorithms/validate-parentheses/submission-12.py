class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack and brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0