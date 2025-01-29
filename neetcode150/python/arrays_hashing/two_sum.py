class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1:
        Time Complexity: O(n^2)
        Space Complexity: O(1) 
        """


        for i in range(len(nums)):
            num = nums[i]
            check = target - num

            for j in range(i+1,len(nums)):
                if check == nums[j]:
                    return [i,j]
                

        """
        Approach 2:
        Time Complexity: O(n)
        Space Complexity: O(n) 
        """

        dic = {}

        for i in range(len(nums)):
            num = nums[i]
            check = target - num
            dic[check] = i

        for k in range(len(nums)):
            num = nums[k]
            
            if num in dic:
                if k != dic[num]:
                    return [k, dic[num]]
                

        """
        Approach 3 (NeetCode solution):
        Time Complexity: O(n)
        Space Complexity: O(n) 
        """

        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i