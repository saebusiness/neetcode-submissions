class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        big_word = word1 + word2
        pointer1 = 0
        pointer2 = len(word1)
        new_string = ""

        while pointer1 < len(word1) and pointer2 < len(big_word):
            print(big_word)
            new_string = new_string + big_word[pointer1]
            new_string = new_string + big_word[pointer2]
            pointer1 += 1
            pointer2 += 1
        
        if pointer1 >= len(word1):
            for i in range(pointer2, len(big_word)):
                new_string = new_string + big_word[i]
        else:
            for i in range(pointer1, len(word1)):
                new_string = new_string + big_word[i]
            
        return new_string
        
        