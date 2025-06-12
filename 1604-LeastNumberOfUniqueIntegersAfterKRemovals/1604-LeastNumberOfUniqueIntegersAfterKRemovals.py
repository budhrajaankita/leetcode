# Last updated: 6/11/2025, 10:34:15 PM
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_dict = {}
        for i in arr:
            if i not in arr_dict:
                arr_dict[i] = 1
            else:
                arr_dict[i] += 1
        l = list(arr_dict.values())
        l_sorted = sorted(l)
        for i in range(len(l_sorted)):
            if l_sorted[i] <= k:
                k = k - l_sorted[i]
                l_sorted[i]=0
            else:
                break
        
        final=0
        for j in l_sorted:
            if j != 0:
                final = final+1
        return final
                


