# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return l1
        if not l1 and l2: return l2
        if l1 and not l2: return l1
        
        if l1.val <= l2.val: head = l1
        else: head = l2
        curr1, curr2 = l1, l2
        prev = ListNode(None)
        while curr1 and curr2:
            next1 = curr1.next
            while curr1.val > curr2.val:
                if not curr2.next:
                    curr2.next = curr1
                    return head
                prev = curr2
                curr2 = curr2.next
            if curr1.val <= curr2.val:    
                prev.next = curr1
                curr1.next = curr2
                prev = curr1
                curr1 = next1
            
        return head