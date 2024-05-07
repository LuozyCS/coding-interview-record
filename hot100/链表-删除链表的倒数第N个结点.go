/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// 思路, 快慢指针:
	// 要找到倒数第n个，只要快指针比慢指针先走n步，这样快指针到结尾的时候慢指针就是我们想要到节点

	// 因为可能删掉头节点, 因此引入哨兵节点

	dummy := &ListNode{}
	dummy.Next = head
	fast := dummy
	slow := dummy
	for fast.Next != nil {

		fast = fast.Next
		if n != 0 {
			n -= 1
		} else {
			slow = slow.Next
		}
	}
	slow.Next = slow.Next.Next
	return dummy.Next
}