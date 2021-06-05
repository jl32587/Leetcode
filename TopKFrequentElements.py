class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == k:
            return nums
        
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        
        dic2 = {}
        for n in dic:
            if dic[n] not in dic2:
                dic2[dic[n]] = [n]
            else:
                dic2[dic[n]].append(n)
        klist = []
        count = 1
        for i in sorted(dic2.keys(), reverse = True):
            if k == 1:
                return dic2[i]
            elif count <= k:
                klist += dic2[i]
                count += len(dic2[i])
        return klist
