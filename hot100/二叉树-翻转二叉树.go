/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	reverse(root)
	return root
}

func reverse(root *TreeNode) {
	l := root.Left
	r := root.Right
	if l == nil && r == nil {
		return
	}
	if r != nil {
		reverse(r)
	}
	if l != nil {
		reverse(l)
	}
	root.Left, root.Right = r, l
	return
}