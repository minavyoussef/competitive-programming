class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, n in enumerate(nums):
            if n in h:
                return [i, h[n]]
            h[target - n] = i


"""
Runtime: 40 ms, faster than 93.37% of Python online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 46.80% of Python online submissions for Two Sum.
"""