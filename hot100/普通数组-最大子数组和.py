class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(1, len(nums)):
            # 如果一项导致整个连续子数组为负了, 那么就没有必要选了, 就选0, 相当于不连续了重新开始找子序列.
            # 然后最后遍历整个数组的最大值.  如果全是负数, 因为是求和, 负数越加越小, 正数越加越大, 所以找到的一定是连续数组
            nums[i] = nums[i] + max(nums[i - 1],0)

        return max(nums)