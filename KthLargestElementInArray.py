class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #QuickSelect approach
        v = random.choice(nums)
        left = [i for i in nums if i > v]
        mid = [i for i in nums if i == v]
        right = [i for i in nums if i < v]
        l, m = len(left), len(mid)
    
        if k <= l: return self.findKthLargest(left, k)
        elif k > l + m: return self.findKthLargest(right, k-l-m)
        else: return mid[0]