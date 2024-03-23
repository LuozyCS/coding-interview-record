'''区间覆盖

还是贪心

我的思考:
    左端点从小到大排序,
    那么肯定覆盖s开始往右的内容,不会有其他的区间比前面的更少的东西能覆盖前面的左端点

    想不出来 太难了

看完y总:
    我的方向没错:
    1. 将所有区间按左端点从小到大排序
    2. 从前往后依次枚举每个区间, 在所有能覆盖start的区间中, 选择右端点最大的区间,然后将start更新成右端点的最大值
    

直接证明  不用反证法 y总这里讲的有点乱 从17:10开始  https://www.acwing.com/video/337/
任何一个最优解可以替换为我们算出来的cnt,等价的.
'''


def main():
    s, t = map(int, input().split())
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(lambda x:x[0])
    
    # if arr[0][0] > s:
    #     print("-1")
    #     return
    # 不能这么写 因为s一直在变化
    
    # 双指针来做
    cnt = 0
    suc = False
    for i in range(N):
        j = i
        r = -2e9
        while j < N and arr[j][0] <= s:
            r = max(r, arr[j][1])
            j += 1
        # 此时出来的r,只有两个情况:
        # 1. r是负无穷,即不存在左端点可以覆盖start的点了
        # 2. r大于等于s小于t,此时cnt+1
        if r >= t:
            cnt += 1
            suc = True
            break
        elif r < s:
            # 已经不存在左端点可以覆盖start的点了
            cnt = -1
            break
        cnt += 1
        i = j - 1 # 因为下一个循环i要加1
        s = r
    # 不能直接print(cnt) 因为可能没有覆盖到t
    if not suc:
        cnt = -1
    print(cnt)
main()
