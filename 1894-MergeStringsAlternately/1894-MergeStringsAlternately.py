# Last updated: 6/11/2025, 10:34:11 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        rnge = min(len(word1), len(word2))
        merged = ""

        for i in range(rnge):
            merged = merged + word1[i] + word2[i]
        
        if len(word1) == len(word2):
            return merged
        elif len(word1) < len(word2):
            return(merged + word2[len(word1):])
        else:
            return (merged + word1[len(word2):])