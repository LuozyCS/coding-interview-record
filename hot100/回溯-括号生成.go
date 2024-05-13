func generateParenthesis(n int) (ans []string) {
	m := n * 2
	path := make([]byte, m)
	var dfs func(int, int)
	dfs = func(i, left int) {
		if i == m {
			ans = append(ans, string(path))
			return
		}
		if left < n {
			// 左括号还没填完
			path[i] = '(' // 全局使用一个path，因此用等号覆盖
			dfs(i+1, left+1)
		}
		if i-left < left {
			// i - left = right, 右括号少于左，可以填左括号
			path[i] = ')'
			dfs(i+1, left)
		}
	}
	dfs(0, 0)
	return
}