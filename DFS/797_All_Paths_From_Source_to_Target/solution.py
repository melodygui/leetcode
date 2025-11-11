def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        curr_path = [0]

        def dfs(u):
            if u == n - 1:
                paths.append(list(curr_path))                  
                return

            for v in graph[u]:
                curr_path.append(v)
                dfs(v)
                curr_path.pop()

        dfs(0)
        return paths