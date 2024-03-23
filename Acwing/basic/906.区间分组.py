'''区间分组 还是贪心
确实很难.

区间内部两两之间没有交集.
找最小组.

这个按照左端点从小到大排列

怎么
ans cnt
按照notion906的分法一定是合法方案,ans是最小值.


贪心很难  因为不知道到底是按照左端点还是右端点.
'''
from heapq import *
def main():
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort(lambda x:x[0])
    # cnt = 1

    # max_r指的是每一组里的最右端点, 但是要记住的是所有组里的最小的最右端点
    ans = []
    for i in range(1, N):
        if len(ans) == 0 or ans[0]>=arr[i][0]:
            # 如果没有分组 或 组内最小值(小根堆)即最小的max_r大于等于当前区间右端点(即相交),说明要加组了
            heappush(ans, arr[i][1])
        else:
            # 如果没有相交,说明可以放进来,至少放最小这一组,当然最小这一组的maxr就要变化了,然后这一组就不一定是最小maxr可
            # 这就是为什么一定要堆
            heappop(ans)
            heappush(ans,arr[i][1])
    print(len(ans))
main()