# 这题的难点在于，你无法知道被排除出滑动窗口的那一个是第几大/小的数，因此每次滑动窗口需要重新比较一次大小
# 这样做的话时间复杂度非常高。纯暴力做法是过不去的
# 因此需要单调队列，有点像单调栈的做法
# 参考答案：https://blog.csdn.net/weixin_49486457/article/details/122929486?spm=1001.2014.3001.5502
# 用了deque，但是写的太难看懂，我对其进行了注释：https://www.acwing.com/solution/content/16810/
# 复习python的内置队列queue
from queue import Queue
from collections import deque
# deque很神奇，双端队列，可以从左侧出队入队，也可以从右侧出队入队
# deque语法：左侧出入：popleft，appendleft。右侧出入：pop，append
def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    q_max = deque()
    q_min = deque()
    ans_max = []
    ans_min = []

    # 注意！！！，一定要写enumerate(nums, 1)，而不能写enumerate(nums)，否则会少一个第一个的输出。
    # 意思是指定索引index从1开始，但是仍然是从数组的第一个开始计算。
    # 可以参考csdn的图片示例，因为假设k = 3，i = 3时应该是开始正式作为第一个滑动窗口开始找最大最小值
    # 如果不写enumerate(nums, 1)则需要下面判断时写成i + 1 - k。
    for i, num in enumerate(nums, 1):
        # q[0]代表左侧头部，q[0][0]代表左侧头部的index，而q[0][1]代表左侧头部的数值
        # q[0][0] <= i - k 表示当前头部已经超出了滑动窗口范围，则从左侧出栈（只有从左侧出栈才能让左侧头部出去，这样可以保证单调队列里的单调性）
        while q_max and q_max[0][0] <= i - k: 
            q_max.popleft()
        while q_min and q_min[0][0] <= i - k: 
            q_min.popleft()

        # 递减队列，找最大值（即左侧头部为最大值）
        # 当队列右侧的值，即q[-1][1]，小于当前入队的值num时，从右侧pop出这个值（队尾）。最后不pop的时候把当前值插入。
        # 个人感觉相当于做了一个插入排序，其实也是暴力解？（并不是，实际上是O(n)）
        while q_max and num > q_max[-1][1]: q_max.pop()
        q_max.append((i, num))

        # 递增同理，找最小值
        while q_min and num < q_min[-1][1]: q_min.pop()
        q_min.append((i, num))

        # if i >= k: print(q[0][1], end=' ')
        # 前k - 1个还没有真的形成滑动窗口并不需要记录最大最小值
        if i >= k: 
            ans_max.append(q_max[0][1])
            ans_min.append(q_min[0][1])
    
    # 输出
    
    for num in ans_min:
        print(num, end = " ")
    print("")
    for num in ans_max:
        print(num, end = " ")
    
main()

# 但是 以上我的写法不仅慢，而且整体也复杂。因为我比13行deque的多了几次遍历输出和保存。
# 上面我的：2014 ms。下面他的：1581 ms。
 
# 以下是13行做法，因为整个是O(n)做法，因此没必要合在一起做。
n, k = map(int, input().split())
arr = list(map(int, input().split()))

from collections import deque

def max_min(arr, func):
    q = deque()
    for i, v in enumerate(arr, 1):
        while q and q[0][0] <= i - k: q.popleft()
        while q and func(v, q[-1][1]): q.pop()     # v 在前
        q.append((i, v))
        if i >= k: print(q[0][1], end=' ')
    print("")

max_min(arr, lambda x, y:x < y)     # 单调递增队列
max_min(arr, lambda x, y:x > y)     # 单调递减队列

