class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach 1:
        Time complexity: O(n)
        Space complexity: O(n)
        """


        dic = {'}':'{', ')':'(', ']':'['}
        
        stack = []

        if len(s)%2 != 0:
            return False

        for char in s:
            if char in dic:
                if stack[-1] == dic[char]:
                    stack.pop()
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True

        return False
    


        """
        Approach 2 (Neetcode solution):
        Time complexity: O(n)
        Space complexity: O(n)
        """
        
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack


        