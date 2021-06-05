class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sumDict = {}
        output = 0
        for i in nums1:
            for j in nums2:
                Sum12 = i + j
                if Sum12 not in sumDict:
                    sumDict[Sum12] = 1
                else:
                    sumDict[Sum12] += 1
            
        for i in nums3:
            for j in nums4:
                minusSum34 = -(i + j)
                if minusSum34 in sumDict:
                    output += sumDict[minusSum34]
        
        return output