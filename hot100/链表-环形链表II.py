'''中等, 比环形链表I难一点

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置(索引从 0 开始)。
如果 pos 是 -1,则在该链表中没有环。注意: pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

优化: 仍然是空间O(1)
想不出来这个优化. 看答案

自己想了一下: 数学推导
看这个帖子
https://leetcode.cn/problems/linked-list-cycle-ii/solutions/441306/142-huan-xing-lian-biao-ii-jian-hua-gong-shi-jia-2
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        
        return None
        