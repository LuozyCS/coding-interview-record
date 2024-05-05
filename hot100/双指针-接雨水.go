func trap(height []int) (ans int) {
	// 动态规划或者双指针都可以做
	n := len(height)
	if n == 0 {
		return 0
	}
	left, right := 0, n-1
	leftMax, rightMax := 0, 0
	for left < right {
		leftMax = max(leftMax, height[left])
		rightMax = max(rightMax, height[right])
		if leftMax < rightMax {
			ans += (leftMax - height[left]) // 不会有负数
			left++
		} else {
			ans += (rightMax - height[right])
			right--
		}

	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}