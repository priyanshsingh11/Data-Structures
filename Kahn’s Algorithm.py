from collections import deque

def kahn_algo(n, edges):
    # Step 1: Build graph & indegree array
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Step 2: Push all 0-indegree nodes into queue
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo = []

    # Step 3: Process queue
    while q:
        node = q.popleft()
        topo.append(node)

        # Step 4: Reduce indegree of neighbors
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # Step 5: Cycle check
    if len(topo) != n:
        return []   # cycle exists

    return topo
