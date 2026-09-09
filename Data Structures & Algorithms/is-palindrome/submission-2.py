class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s =  "".join(char for char in s if char.isalnum()).lower()

        l = 0
        r = len(clean_s) - 1

        while l <= r:
            if clean_s[l] == clean_s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
