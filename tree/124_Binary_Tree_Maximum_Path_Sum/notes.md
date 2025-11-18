- This problem is very similar to problem `543: diameter of a binary tree`!
- The structure is nearly identical:
    - Both use postorder DFS.
    - Both compute a “through-this-node” value using left + right + node.
    - Both return an extendable single-branch value to the parent.
    - Both maintain a global best separately from what DFS returns.

- The only real difference:
    - Diameter counts edges.
    - Max path sum adds node values (which can be negative).