class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        max_ending = 0
     
        for i in nums:
            
            if (max_ending < 0):
                max_ending = 0
            max_ending = max_ending + i
            max_val = max(max_ending,max_val)
        return max_val
        