class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_set = set()
        l = 0
        length = 0

        for r in range(len(s)):
            if s[r] in num_set:
                while s[r] in num_set:
                    num_set.remove(s[l])
                    l += 1
            
            num_set.add(s[r])
            length = max(length,len(num_set))
        
        return length


