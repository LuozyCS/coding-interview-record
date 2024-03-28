
'''困难

给你一个整数数组 nums, 有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

思考
acwing也写过  好像是用堆?

'''

# # 下面是堆的写法, 再试试deque
# import heapq
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """

#         q = [(-nums[i], i) for i in range(k)] # 小根堆
#         heapq.heapify(q)

#         ans = [-q[0][0]]
#         for i in range(k, len(nums)):
#             heapq.heappush(q, (-nums[i], i))
#             while q[0][1] <= (i - k):
#                 # 如果这个最大值, 并不在我们的窗口范围内, 就别管他, 我们也不需要每次移动窗口都去专门处理不在窗口内的值
#                 heapq.heappop(q)
#             ans.append(-q[0][0])
        
#         return ans
        


        

