class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        n, m = len(grid), len(grid[0])
        
        #Union Find (weighted quick-union with path compression)
        roots = {(y, x):(y, x) for y in range(n) for x in range(m) if grid[y][x] == "1"}
        #sz = {(y, x): 0 for y in range(n) for x in range(m)}
        
        def find(p):
            while p != roots[p]:
                roots[p] = roots[roots[p]]
                p = roots[p]
            return p
        
        def union(p,q):
            p, q = find(p), find(q)
            #if sz[p] < sz[q]: 
            roots[p] = q
            #    sz[q] += sz[p]
            # else:
            #    roots[q] = p
            #    sz[p] += sz[q]
                
        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1":
                    if x+1 < m and grid[y][x+1] == "1": union((y,x),(y,x+1))
                    if y+1 < n and grid[y+1][x] == "1": union((y,x),(y+1,x))

        return len(set(find(roots[(y,x)]) for (y, x) in roots))