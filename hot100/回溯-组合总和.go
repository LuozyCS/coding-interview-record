func combinationSum(candidates []int, target int) [][]int {
	ans := [][]int{}
	var trace func(sum int, cur []int, idx int)
	trace = func(sum int, cur []int, idx int) {
		if sum > target {
			// 这个方案不行,直接返回
			return
		}
		if sum == target {
			tmp := make([]int, len(cur))
			copy(tmp, cur)
			ans = append(ans, tmp)
		}
		// 可以重复当前字符,但是前面的就不重复了
		for i := idx; i < len(candidates); i++ {
			next := append(cur, candidates[i])
			trace(sum+candidates[i], next, i)
		}
	}
	trace(0, []int{}, 0)
	return ans
}