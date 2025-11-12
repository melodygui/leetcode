def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        curr_path = [0]

        def dfs(u):
            """
            Recursive DFS that explores all possible paths
            from current node u to the target node n - 1.
            """
            # Base case: if we reach the target node, record a copy of the path
            if u == n - 1:
                paths.append(list(curr_path))                  
                return

            # Recursive case: explore each neighbor of the current node
            for v in graph[u]:
                curr_path.append(v) # choose: add this node to the path
                dfs(v)
                curr_path.pop()  # backtrack: remove v before trying next neighbor

        # start DFS from node 0 (source)
        dfs(0)
        return paths
