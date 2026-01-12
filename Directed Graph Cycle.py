class Solution:
    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
             
        vis=[False]*V
        path=[False]*V
        
        def dfs(node):
            vis[node]=True
            path[node]=True
            
            for neigh in adj[node]:
                if not vis[neigh]:
                    if dfs(neigh):
                        return True
                    
                elif vis[neigh] and path[neigh]:
                    return True
                
                
            path[node]=False
            
            return False
            
            
            
        for i in range(V):
            if not vis[i]:
                if dfs(i):
                    return True
                    
        return False
