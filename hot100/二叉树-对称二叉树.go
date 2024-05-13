/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
	u, v := root, root
	q := []*TreeNode{}
	q = append(q, u)
	q = append(q, v)
	for len(q) > 0 {
		u, v = q[0], q[1]
		q = q[2:]
		if u == nil && v == nil {
			continue
		}
		if u == nil || v == nil {
			return false
		}
		if u.Val != v.Val {
			return false
		}
		q = append(q, u.Left)
		q = append(q, v.Right)

		q = append(q, u.Right)
		q = append(q, v.Left)
	}
	return true
}

// // 递归方法

// func isSymmetric(root *TreeNode) bool {
// 	if root == nil {
// 		return true
// 	}

// 	return isSym(root.Left, root.Right)
// }

// func isSym(p, q *TreeNode) bool {
// 	if p == nil || q == nil {
// 		return p == q
// 	}

// 	return p.Val == q.Val && isSym(p.Left, q.Right) && isSym(p.Right, q.Left)
// }

