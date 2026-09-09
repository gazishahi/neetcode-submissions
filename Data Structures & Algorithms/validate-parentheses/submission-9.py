class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
  
        brackets = {')':'(', '}':'{', ']':'['}
        res = []
        for i, c in enumerate(s):
            if c == '(' or c == '{' or c == '[':
                res.append(c)
            else:
                if res and brackets[c] == res[-1]:
                    res.pop()
                else:
                    return False
        
        return len(res) == 0

