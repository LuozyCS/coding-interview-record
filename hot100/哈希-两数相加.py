'''写的是哈希

但是我没看懂哪里需要哈希

应该就是不需要哈希
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # 他给定义的链表,python用链表也是纯纯nt
        node = ListNode()
        head = node
        sumup = 0
        # 两个链表都为空且没有进位了则退出
        while l1 or l2 or sumup:
            if l1:
                sumup += l1.val
                l1 = l1.next
            if l2:
                sumup += l2.val
                l2 = l2.next
            node.val = sumup % 10 # 取余数为当前节点的值
            sumup //= 10 # 地板除，只去除完之后的整数部分
            if l1 == None and l2 == None and sumup == 0:
                break
            node.next = ListNode()
            node = node.next
            
        return head