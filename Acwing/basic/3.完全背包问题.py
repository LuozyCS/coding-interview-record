'''完全背包

和01背包的问题是每种物品只有一个,完全背包问题是每种物品有无限个。

https://blog.csdn.net/raelum/article/details/128996521
上面的链接解释了为何正常的推导会导致TLE,以及为啥需要优化,但是优化讲的不清楚,看Notion或者AcWing。

就是用f(i,j-vi)替代f(i,j)中枚举的部分

回顾重要的点：
1. 确定状态转移的物理意义 实际意义
2. 记住这个完全背包的推导:用f(i,j-vi)替代f(i,j)中枚举的部分
'''



if __name__ == '__main__':
    N, V = map(int, input().split()) #种类数  总体积

    f = [[0] * (V + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        v, w =map(int, input().split()) # 体积 价值å
        for j in range(0, V + 1):
            if j >= v: # 能放进去，只要能放进去就算进去，不一定说体积要刚好达到j
                f[i][j] = max(f[i - 1][j], f[i][j - v] + w)
            else:
                f[i][j] = f[i-1][j]
    print(f[N][V]) # f[i][j]代表当前选择第i个物品体积不大于V时的最大价值，因此直接选这个就行
                   # 好像01背包也是选这个

