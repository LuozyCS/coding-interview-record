func maxProduct(nums []int) int {

	// 如果连续子数组中的元素存在负数，正数乘以负数就成负数，那么最大值乘以负数就变成了最小值。
	// 因此需要同时考虑当前连续子数组乘积的最大值 curMax 和最小值 curMin。

	// 因为可以有负数，最大值可能由之前的最小值乘当前的负数得到
	size := len(nums)
	if size == 1 {
		return nums[0]
	}

	ans, curMax, curMin := nums[0], nums[0], nums[0]

	for i := 1; i < size; i++ {
		if nums[i] < 0 {
			curMax, curMin = curMin, curMax
		}
		curMax = max(curMax*nums[i], nums[i]) // 如果当前i是负数，上面if就交换了，此时就是最小（可能是负数）乘以负数。
		curMin = min(curMin*nums[i], nums[i]) // 只是用来存储最小值
		ans = max(curMax, ans)
	}
	return ans
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}