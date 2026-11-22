class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        max_l = 0

        for char in char_set:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] != char:
                    count += 1
                if count > k:
                    while count > k:
                        if s[l] != char:
                            count -= 1
                        l += 1
                max_l = max(max_l, r - l + 1)
        return max_l
