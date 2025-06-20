# Last updated: 6/11/2025, 10:35:07 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        ans = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())

            

            
        