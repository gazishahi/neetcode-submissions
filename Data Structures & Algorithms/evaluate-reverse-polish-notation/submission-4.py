class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if stack and c == "+":
                stack.append(stack.pop() + stack.pop())
            elif stack and c == "*":
                stack.append(stack.pop() * stack.pop())
            elif stack and c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif stack and c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        
        return stack[-1]
