# Last updated: 6/11/2025, 10:35:11 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        pre = []
        
        for i in range(len(strs[0])):
            curr = strs[0][i]
            # print(pre)
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != curr:
                    return "".join(pre)
            pre.append(curr)

        return "".join(pre)


                

            
                




        