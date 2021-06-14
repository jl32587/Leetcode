class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #backtracking
        if len(nums) == 0: return [[]]
        
        results = []
        
        for i in range(len(nums)):
            remainder = nums[:i] + nums[i+1:]
            perms = self.permute(remainder)
            for p in perms:
                p.append(nums[i])
            results.extend(perms)
         
        return results