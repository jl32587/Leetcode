class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.result = []
        n = len(graph)
        def dfs(i, path):
            if i == n - 1: 
                self.result.append(path)
                return 
            for child in graph[i]:
                dfs(child, path + [child])
                
        dfs(0, [0])
        return self.result