class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 1:
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
            
        return False

    
        """
        Approach 2:
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        check_set = set(nums)

        if len(check_set) == len(nums):
            return False
        
        return True


        """
        Approach 3 (NeetCode solution):
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
