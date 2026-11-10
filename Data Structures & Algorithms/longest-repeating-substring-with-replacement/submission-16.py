class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        char_set = set(s)
        max_length = 0

        for i in char_set:
            l = 0
            count = 0

            for r in range(len(s)): 

                if s[r] == i:
                    count += 1
                    

                
                while ((r - l + 1) - count) > k:
                    
                    if s[l] == i:
                        count -= 1
                    l += 1
                
                

                max_length = max(r - l + 1, max_length)
        
        return max_length