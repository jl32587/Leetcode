class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}  
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        order = {}
        for c in freq:
            if freq[c] not in order:
                order[freq[c]] = [c]
            else:
                order[freq[c]].append(c)
        
        arr = [i for i in order]
        arr.sort(reverse=True)
        out = ""
        for i in arr:
            for c in order[i]:
                out += c*i
        
        return out