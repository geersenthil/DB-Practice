class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for x in range(len(nums)):
            if target - nums[x] in values:
                return [values[target-nums[x]],x]
            else:
                values[nums[x]]=x
                
        