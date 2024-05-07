func productExceptSelf(nums []int) []int {
	// 因为不能用除法， 因此保存前后缀乘积
	// 可以优化，直接先乘前缀，后乘后缀，不需要保存下来
	n := len(nums)
	ans := make([]int, n)
	pre := make([]int, n)
	fw := make([]int, n)
	pre[0] = nums[0]
	fw[n-1] = nums[n-1]
	for i := 1; i < n; i++ {
		pre[i] = pre[i-1] * nums[i]
		fw[n-1-i] = fw[n-i] * nums[n-1-i]
	}
	for i := 0; i < n; i++ {
		if i == 0 {
			ans[i] = fw[i+1]
		} else if i == (n - 1) {
			ans[i] = pre[i-1]
		} else {
			ans[i] = pre[i-1] * fw[i+1]
		}
	}
	return ans
}