# 和数字排列问题很像
n = 0
N = 10
path = [[0] * N for _ in range(N)]

# 因为是二维的，而且还有对角线的皇后也不可以存在，所以需要更多东西去存状态
# 一个是列，一个是左对角线，一个是右对角线
col, dg, udg = [False] * N, [False] * N, [False] * N
# 不需要行，因为行是递增的，不可能有重复的

def dfs(u):
    global n, path, col, dg, udg
    # 输出结果
    if u == n:
        for i in range(n):
            for j in range(n):
                if path[i][j] == 1:
                    print("Q", end = "") 
                    break # 一行只能有一个皇后
                else:
                    print(".", end = "")
            print()
        return
    # 开始放皇后
    for i in range(n):
        # 为什么是u + i, u - i + n？ 画图出来算一下就知道了 
        if not col[i] and not dg[u + i] and not udg[u - i + n]:
            path[u][i] = 1
            dg[u + i] = udg[u - i + n] = col[i] = True
            dfs(u + 1)
            # 回溯
            path[u][i] = 0
            dg[u + i] = udg[u - i + n] = col[i] = False

def main():
    global n
    n = int(input())
    dfs(1)
main()