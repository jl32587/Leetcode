class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        out = []
        while i <= len(nums) - 3:
            while i > 0 and i <= len(nums) - 3 and nums[i-1] == nums[i]:
                i += 1
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if  threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
            i += 1
        return out