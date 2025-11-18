class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build an adjacency list: key is a class node, value is node(s) that are its prereqs        
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # run DFS with a visited to detect cycles 
        visited = set()
        def DFS(course: int):      
            # base case: reached a course with no prereq
            if not graph[course]:
                return True        
            if course in visited:
                return False 
            
            # process current node by adding it to visited 
            visited.add(course)

            # visit all its neighbors (its prereq) - early return False if a prereq cannot be taken
            for prereq in graph[course]:
                if not DFS(prereq):
                    return False 
            
            # why EXACTLY do we need these two lines?
            visited.remove(course)
            graph[course] = []
            
            return True 
        
        # why EXACTLY do we need to run DFS on every node?
        for i in range(numCourses):
            if not DFS(i):
                return False
        
        return True 