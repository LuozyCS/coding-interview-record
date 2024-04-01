'''简单

提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
普通方法很简单, 重点是空间O1
然后需要注意易错点, 奇数也可以是回文串
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 先遍历一次
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        print(length)
        if length == 1:
            # 一个数也是回文
            return True
        # if length % 2 != 0:
        #     print("ji")
        #     return False
        # length = int(length / 2)
        # 奇数也可以是回文
        length = length // 2
        
        # 反转后半段
        node = head
        for i in range(length - 1):
            node = node.next
        
        # 反转. 背模板
        pre = None
        cur = node
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        node = head
        for i in range(length):
            if pre.val == node.val:
                pre = pre.next
                node = node.next
                continue
            else:
                return False
        return True
        

