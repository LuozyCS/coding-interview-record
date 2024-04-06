'''简单

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

前中后序指的是什么时候访问根节点. 左右都是先左后右
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [] # 都是从右边pop append
        res = []
        node = root

        # 怎么思考的?
        # 把每个循环看做一个单独的中序遍历, 独立的考虑子问题, 每个node都是下一个子树的根节点
        while stack or node: # 且还是或?
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right

        return res
