class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { "}": "{", "]": "[", ")": "(" }
        stack = []
        # check if it's a closing tag
        # if it is and the latest on the stack isn't matching, return false 

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        return True
            
