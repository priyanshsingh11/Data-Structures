class Solution:
    
    def topoSort(self, V, edges):
        # Create adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        visited = [False] * V
        stack = []
        
        # Helper DFS function
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)
        
        # Perform DFS for all unvisited nodes
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        # Reverse the stack to get topological order
        return stack[::-1]
