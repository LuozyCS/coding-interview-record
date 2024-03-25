'''贪心

"您的任务是确定奶牛的排序，使得所有奶牛的风险值中的最大值尽可能的小。"

最大值尽可能的小.

谈心策略 w + s从小到大排序. 证明看y总https://www.acwing.com/video/317/
'''


if __name__ == "__main__":
    N = int(input())

    cows = []
    for _ in range(N):
        w, s = map(int, input().split())
        cows.append((w + s, w, s))
    cows.sort(key = lambda x:x[0]) # 从小到大排序,小的放最下面

    res = float("-inf") # 最大的风险值
    sumW = 0
    for _, w, s in cows:
        res = max(res, sumW - s)
        sumW += w
    print(res)

    