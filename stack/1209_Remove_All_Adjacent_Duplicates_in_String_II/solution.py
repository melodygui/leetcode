def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # each item in the stack stores (char, count)

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1 
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        res = ""
        for item in stack:
            char, count = item
            res += char * count 
        
        return res