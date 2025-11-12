def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head 

        def dfs(prev, curr):
            """returns tail of the flattened list"""
            if not curr:
                return prev

            # process current 
            curr.prev = prev 
            if prev: 
                prev.next = curr

            # process left subtree (curr.child) - flatten child list 
            tempNext = curr.next  # save next pointer first since recursion will modify it 
            
            tail = dfs(curr, curr.child) # returns the last node of flattened child list
            curr.child = None

            # process right subtree - curr.next            
            return dfs(tail, tempNext)
        
        dfs(None, head)
        return head