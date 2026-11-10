class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        max_l = 0
        for c in char_set:
            l = 0
            rep = 0
            for r in range(len(s)):
                if s[r] != c:
                    rep += 1
                    while rep > k:
                        if s[l] != c:
                            rep -= 1
                        l += 1
                max_l = max(max_l,r - l + 1)
        return max_l