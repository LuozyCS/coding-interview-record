# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        A, B = headA, headB
        a = set()
        while A != None:
            a.add((A.val, A))
            A = A.next

        while B != None:
            if (B.val, B) in a:
                return B
            B = B.next
        return None

        