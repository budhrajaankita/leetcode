# Last updated: 6/11/2025, 10:34:13 PM
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        adj = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
                if r1 >= dist:
                    adj[i].append(j)

                if r2 >= dist:
                    adj[j].append(i)
        
        maxBombs = 0

        def dfs(bomb, visited):
            visited.add(bomb)

            for nei in adj[bomb]:
                if nei not in visited:
                    dfs(nei, visited)

            return len(visited)
            


        for i in range(len(bombs)):
            
            res = dfs(i,visited=set())
            maxBombs = max(res, maxBombs)
        
        return maxBombs



        