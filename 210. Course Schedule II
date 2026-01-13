class Solution(object):
    def dfs(self, src, vis, path,graph, order):
        vis[src]=True
        path[src]=True

        for neigh in graph[src]:
            if not vis[neigh]:
                if (self.dfs(neigh, vis, path, graph, order)):
                    return True
            elif path[neigh]:
                return True
            
        path[src]=False
        order.append(src)
        return False

    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)

        vis=[False]*numCourses
        path=[False]*numCourses
        order=[]

        for i in range(0,numCourses):
            if not vis[i]:
                if self.dfs(i, vis, path, graph, order):
                    return []

        return order



