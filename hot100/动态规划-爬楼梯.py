'''简单

    但是我觉得很难


    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 分析：想象一个爬行序列
 到达n阶,最后一步只能爬1阶或者2阶
 爬1阶:到达n-1阶 然后一次爬1阶 序列最后为1
 爬2阶:到达n-2阶 然后一次爬2阶 序列最后为2
 因此 方法数(n) = 方法数(n-1) + 方法数(n-2) 

 易错:
    1. dp不一定是需要max这种
'''

class Solution:
    def climbStairs(self, n: int) -> int:

        f = [0] * (n + 100)
        f[0] = 1
        f[1] = 2
        if n < 2:
            return f[n - 1]
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]
        return f[n - 1]
