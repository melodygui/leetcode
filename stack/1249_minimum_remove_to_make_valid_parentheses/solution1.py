"""
    This is approach 1 from the editiorial.
    It uses a stack to track matching open and closed parantheses (same logic
    as in 20. Valid Parentheses problem). It uses a set to store the indicdes of
    parentheses (both open and close) to remove.

    Note that the stack stores the indices of the open parentheses, not the 
    parentheses themselves - this is to make it easier to add them to the set later.
    
    So we add to the set the indices of closed parentheses that do not have a 
    matching open parentheses. 

    For any remaining open parentheses in the stack, we add their indices to the 
    to set to remove as well.  
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        toRemove = set()

        for index, char in enumerate(s): # loop through string O(n)
            if char == '(':
                stack.append(index)
            elif char == ')':
                if not stack:
                    toRemove.add(index)
                else:
                    stack.pop()       

        if stack:
            for index in stack: # loop through stack O(n)
                toRemove.add(index)

        result = []
        for index, char in enumerate(s): # iterate over string is O(n)
            if index not in toRemove: # check if an item is in a set is O(1)
                result.append(char)
        
        return "".join(result)
    
"""
    This solution is O(n) in time and O(n) in space, where n is length of the string.
    Some O(n) operations people mistake to be O(1):
        - Any opreation involving the string is basically O(n) bc strings are immutable so
          they have to be rebuilt from scratch everytime.
        - Adding or removing NOT from end of a list is O(n) because have to shift other 
          elements up or down to fill in the gap.
        - Checking if an item is in a LIST is O(n)! Even with binary search it's O(logn).
          (However, checking if an item is in a SET is O(1)!)
"""

