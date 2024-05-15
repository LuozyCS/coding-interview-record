func twoSum(nums []int, target int) []int {
	hash := map[int]int{}
	for i, x := range nums {
		if p, exist := hash[target-x]; exist {
			return []int{p, i} // 如果target-x找到了,那说明之前访问过，没找到就存下来
		}
		hash[x] = i
	}
	return nil
}