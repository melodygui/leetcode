"""
    NeetCode's solution. Approach 3 in the editorial.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0 # to track how many extra ( parentheses there are. it should not be negative

        # first pass to remove invalid closed parentheses ) 
        for c in s:
            if c == '(':
                res.append(c)
                cnt += 1
            elif c == ')' and cnt > 0:
                res.append(c)
                cnt -= 1            
            elif c != ')':
                # add letters
                res.append(c)

        # second pass to filter out extra open parentheses ( if needed 
        # always safe to remove the RIGHTMOST '(', so iterate through the string from right to left by reversing it first
        if cnt > 0:
            filtered = []
            for c in res[::-1]: # reverses res
                if c == '(' and cnt > 0:
                    cnt -= 1
                else:
                    filtered.append(c)
            return "".join(filtered[::-1]) # reverse it back to original order 

        return "".join(res)