// 尝试用golang写

package main

func letterCombinations(digits string) (res []string) {
	n := len(digits)
	if n == 0 {
		return nil
	}
	path := make([]byte, n)
	var set = [...]string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
	var dfs func(int)
	dfs = func(i int) {
		if i == n {
			res = append(res, string(path))
			return
		}
		for _, v := range set[digits[i]-'0'] {
			path[i] = byte(v)
			dfs(i + 1)
		}

	}
	dfs(0)
	return
}
