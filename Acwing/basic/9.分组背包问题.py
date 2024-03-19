'''分组背包

分析题目,仍然是01背包
遍历每个组
    遍历每个容量(因为当前组别下的每个容量的最优解可以从上一组别+本组某个物品的选择得到)
        要么不选,要么选1,要么选2......要么选s (共s + 1)
数据范围

0<N,V≤100
0<Si≤100
0<vij,wij≤100
'''

def main():
    N, V = map(int, input().split())

    f = [0] * (V + 1)
    for i in range(N):
        s = int(input())
        v = [0] * (s + 1)
        w = [0] * (s + 1)
        for _ in range(1, s + 1):
            v[_], w[_] = map(int, input().split())
        for j in range(V, 0, -1): # 左闭右开V V-1 V-2 ... 1
            mmax = 0
            for k in range(s + 1):
                if j >= v[k]:
                    mmax = max(mmax, f[j - v[k]] + w[k])
            f[j] = max(f[j], mmax)
    
    print(f[V])




main()