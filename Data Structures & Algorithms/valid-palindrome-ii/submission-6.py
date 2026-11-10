class Solution:
    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:

                s1 = s[0:l] + s[l+1:]

                l1 = 0
                r1 = len(s1) - 1

                while l1 < r1:
                    if s1[l1] != s1[r1]:
                        s2 = s[0:r] + s[r+1:]

                        l2 = 0
                        r2 = len(s2) - 1

                        while l2 < r2:
                            if s2[l2] != s2[r2]:
                                return False
                            l2 += 1
                            r2 -= 1
                        return True
                    l1 += 1
                    r1 -= 1

                return True
            l += 1
            r -= 1
        return True
                    
            
        