'''中等

给你一个整数数组 coins ,表示不同面额的硬币；以及一个整数 amount ,表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额,返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1:

输入:coins = [1, 2, 5], amount = 11
输出:3 
解释:11 = 5 + 5 + 1


思考:
这题还是不会.  

看了答案, 这就是背包问题  acwing!
(完全背包: 有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。)
对比理解
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    f[i] = min(f[i], f[i - coin] + 1 )