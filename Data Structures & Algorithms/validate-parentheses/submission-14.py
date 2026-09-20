class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}":"{", ")":"(", "]":"["}

        for i in range(len(s)):
            if s[i] == "}" or s[i] == "]" or s[i] == ")":
                if stack and stack[-1] == brackets[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return len(stack) == 0