func findAnagrams(s string, p string) (ans []int) {
	cnt := [128]int{} // 存储每个字符的出现次数
	for _, ch := range p {
		cnt[ch]++
	}

	left := 0 // 跟踪当前窗口的左边界
	for right, ch := range s {
		cnt[ch]--

		// 这里的循环会一直执行大括号内的代码块，直到cnt[ch]的值不再小于0为止。
		for cnt[ch] < 0 { // 字符 ch 的出现次数超过了在字符串 p 中的出现次数
			cnt[s[left]]++
			left++
		}
		if right-left+1 == len(p) { // 恰好
			ans = append(ans, left)
		}
	}
	return
}

