'''简单

# 深度优先

是递归还是循环?

''''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# # 循环方法
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         deque = collections.deque()
#         if not root:
#             return 0
#         deque.append(root)
#         depth = 0
#         # 每一层一次while循环
#         while deque:
#             n = len(deque) # 每一层的节点数, 这个不随着deque的变化而变化, 每层只变化一次
#             for _ in range(n):
#                 node = deque.popleft()
#                 if node.left:
#                     deque.append(node.left)
#                 if node.right:
#                     deque.append(node.right)
#             depth += 1
#         return depth
    
# 递归方法
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        return max(l_depth, r_depth) + 1 # +1代表的是当前节点深度, 只要不是None空姐点, 就不会返回0, 那就+1



        
        