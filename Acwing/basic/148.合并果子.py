'''
贪心
每次搬果子重量最小的两个

秒了!
'''
from heapq import *
if __name__ == "__main__":
    N = int(input())
    in_arr = list(map(int, input().split()))
    arr = []
    # heappush(arr, in_arr) # 看看能不能一次push进去 看看下面
    for _ in range(N):
        heappush(arr, in_arr[_])
    res = 0
    for _ in range(N - 1): # 一共要静心N - 1次
        a = arr[0]
        heappop(arr)
        b = arr[0]
        heappop(arr)
        weight = a + b
        heappush(arr, weight)
        res += weight
    print(res)


# 好像可以这么写heapify
# from heapq import *

# n = int(input())
# nums = list(map(int, input().split()))

# heapify(nums)

# res = 0
# while len(nums) > 1:
#     a = heappop(nums)
#     b = heappop(nums)
#     res += a + b
#     heappush(nums, a + b)
# print(res)