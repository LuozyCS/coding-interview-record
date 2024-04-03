'''简单

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

思考:
    我还是觉得好难
    找每个卖出时间点之前的最小值
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

import heapq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        margin = 0
        # q = []
        # heapq.heapify(q) # 小根堆, 找每个卖出时间点之前的最小值
        # 其实不需要维护一个堆, 一个数字就行了
        if not prices:
            return 0
        min_price_in = prices[0]
        for i in range(1, len(prices)):
            margin = max(margin, prices[i] - min_price_in)
            min_price_in = min(prices[i], min_price_in)

        return margin