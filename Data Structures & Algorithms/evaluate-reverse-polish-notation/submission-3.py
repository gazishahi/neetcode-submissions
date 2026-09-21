class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for n in tokens:
            if stack and n == "+":
                stack.append(stack.pop() + stack.pop())
            elif stack and n == "*":
                stack.append(stack.pop() * stack.pop())
            elif stack and n == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif stack and n == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(n))

        return stack[0]
            