'''简单

141. 环形链表
简单

相关标签
相关企业
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意: pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。

# 这题纯傻逼, 输出不需要什么pos ,只需要true false
# 简单方法很简单, 看提升

提升: 如何使用O(1)空间复杂度完成

回答: 快慢指针
问：兔子会不会「跳过」乌龟，从来不会和乌龟相遇呢？

答：这是不可能的。如果有环的话，那么兔子和乌龟都会进入环中。这时用「相对速度」思考，乌龟不动，兔子相对乌龟每次只走一步，这样就可以看出兔子一定会和乌龟相遇了。

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         dict = {}
#         node = head
#         # cnt = 0
#         while node:
#             if node in dict:
#                 return True
#             else:
#                 dict[node] = 1
#                 # cnt += 1
#             node = node.next
#         return False

# 用快慢指针也可以, 空间O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head  # 乌龟和兔子同时从起点出发
        while fast and fast.next:
            # 这里必须是这样的判断条件, 因为如果fast.next存在, 其fast.next.next才有可能存在, 至少是None. 如果直接判断fast.next.next很可能报错, 因为有可能根本不存在fast.next
            slow = slow.next  # 乌龟走一步
            fast = fast.next.next  # 兔子走两步
            if fast is slow:  # 兔子追上乌龟（套圈），说明有环
                return True
        return False  # 访问到了链表末尾，无环

'''

'''