# Solution class defining the isValid method
import unittest
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store the opening brackets
        stack = []
        # Mapping of closing brackets to opening brackets
        mapping = {')': '(', ']': '[', '}': '{'}
        
        # Iterate through the string
        for char in s:
            if char in mapping:
                # Get the top element from stack, or a dummy value if stack is empty
                top_element = stack.pop() if stack else '#'
                
                # If the mapped value of the current closing bracket doesn't match the stack's top element
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If stack is empty, all opening brackets are closed properly
        return not stack


# Unit test code


