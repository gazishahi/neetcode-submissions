class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}":"{", ")":"(", "]":"["}

        for c in s:
            if c == "}" or c == "]" or c == ")":
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0