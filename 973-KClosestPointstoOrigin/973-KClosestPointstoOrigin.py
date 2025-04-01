# Last updated: 4/1/2025, 3:53:28 PM
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        allP = []
        heap = []

        for x, y in points:
            dist = x**2 + y**2
        
            if len(heap) < k:
                heapq.heappush(heap, (-dist, x, y) )
            else:
                heapq.heappushpop(heap, (-dist, x, y))


        return [[x,y] for _,x,y in heap]
        # allP.append([dist, x, y])
        # allP.sort(key=lambda x: x[0])
        # return allP[0:k]



        