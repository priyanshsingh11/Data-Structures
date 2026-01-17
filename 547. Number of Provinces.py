class Solution(object):

    def dfs(self, city, isConnected, visited, n):
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                self.dfs(neighbor, isConnected, visited, n)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1         
                visited[i] = True
                self.dfs(i, isConnected, visited, n)

        return provinces
