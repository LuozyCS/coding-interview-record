'''中等

想不出来, 看答案

看了一眼状态转移就懂了

f[k] = max{f[k - 1], nums[k] + f[k - 2]}
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        if n == 1:
            return f[-1]
        f[1] = max(f[0], nums[1])
        robbed = True
        for i in range(2, n):
            f[i] = max(f[i - 1], nums[i] + f[i - 2])

        return f[-1]
