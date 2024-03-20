'''贪心

并不是第一章的合并区间.题目不一样的

贪心先用排序去尝试
只看眼前最优解,然后走到全局最优价(只有单峰才能贪心)

怎么证明是最优解呢? 
A是全局最优解
B是当前贪心方案得到的可行解
A>=B且A<=B 则A=B

具体直接看y总视频
https://www.acwing.com/video/335/
10min处开始证明
'''

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x:x[1]) # 右端点从小到大排列

    cnt = 1
    node = arr[0][1] # 选右端点
    for i in range(1, N):
        if arr[i][0] <= node:
            continue
        else:
            node = arr[i][1]
            cnt += 1
    print(cnt)
    