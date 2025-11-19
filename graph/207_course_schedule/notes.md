### Core Idea:
1. Build a graph:
      For each course, keep a list of courses it depends on.

2. For each course, run a DFS that answers:
      “Can this course eventually be completed without entering a cycle?”

3. During DFS:
      - Mark a course as "in the current path."
      - Recursively check all its prerequisites.
      - If you ever revisit a course already "in the current path":
            A cycle exists → return False.
      - When all prerequisites are good:
            Unmark the course from the current path.
            Mark the course as "safe" so we never need to check it again.

4. If EVERY course is confirmed safe (no cycles found):
      return True.
   Otherwise:
      return False.
