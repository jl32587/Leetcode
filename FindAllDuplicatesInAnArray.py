class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                dup.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return dup