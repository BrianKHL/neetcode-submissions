class Solution:
    def isValid(self, s: str) -> bool:
        #Need to use Hashmap to pair parentheses
        stack = [] #Create empty list
        closeToOpen = {")": "(", "]": "[", "}": "{"} # Make the parentheses key and value pair

        for c in s: #Use s instead of len(s), because its just str
            if c in closeToOpen: #If c is in the closeToOpen
                if stack and stack[-1] == closeToOpen[c]: # check if stack and last parentheses match from closeToOpen
                    stack.pop() #if match pop it
                else:
                    return False # if there is unmatched
            else:
                stack.append(c) # if its match, then we can add as much as we want

        return True if not stack else False #At the end should be empty since you popped it before