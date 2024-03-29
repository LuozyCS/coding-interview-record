'''

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur, pre = head, None

        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 分为四步, tmp往前移保存下一个要反转的, cur往前指, pre前移, cur前移
        return pre
            