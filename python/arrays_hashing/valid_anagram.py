class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach 1:
        Time Complexity: O(n)
        Space Complexity: O(n)

        Assuming the size of both the strings are almost the same(or same)
        """


        d1 = {}
        d2 = {}

        for x in s:
            if x not in d1:
                d1[x] = 1
            else:
                d1[x] = d1[x] + 1

        for y in t:
            if y not in d2:
                d2[y] = 1
            else:
                d2[y] = d2[y] + 1
        
        
        if len(d1) != len(d2):
            return False
        else:
            for key in d1:
                if key not in d2:
                    return False
                if d1[key] != d2[key]:
                    return False
            return True
        

        """
        Approach 2 (using .get function on hashmap):
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
