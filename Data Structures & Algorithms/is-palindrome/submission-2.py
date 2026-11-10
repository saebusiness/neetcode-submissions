class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(filter(str.isalnum, s.lower().strip()))
        print(text)
        l = 0
        r = len(text) - 1

        while l < r:
            if text[l] != text[r]:
                print("Detected " + s[l] + " and " + s[r])
                return False
            l += 1
            r -= 1
        
        return True