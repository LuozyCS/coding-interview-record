'''多重背包

如果利用完全背包思维去化简公式的话:

A式:dp[i][j]=max(dp[i-1][j],dp[i-1][j-v]+w,dp[i-1][j-2v]+2w,⋯,dp[i-1][j-kv]+kw)(其中k等于s[i]).
令j = j - v 得到

B式:dp[i][j-v]=max(dp[i-1][j-v],dp[i-1][j-2v]+w,⋯,dp[i-1][j-kv]+(k-1)w)
两式联立得

C式:dp[i][j]=max(dp[i-1][j],dp[i][j-v]+w)

这个推导C式的过程看似没有问题,但如果仔细去分析C式中dp[i][j-v]部分:

如果dp[i][j - v]这个状态还想再添加一件第i个物品的话(假设第i个物品的体积为v价值为w),如果第i个物品刚好在之前被装完了,那么即使还有空间,想要再装入一件i物品也是不行的,那么dp[i][j] = dp[i][j - v],而不是上述部分的dp[i][j - v] + w,由于这种情况的存在,所以多重背包不能继续套用完全背包的公式。

作者:yxc
链接:https://www.acwing.com/video/216/
来源:AcWing
著作权归作者所有。商业转载请联系作者获得授权,非商业转载请注明出处。


因此要是用01背包的思路,即遍历每个物品每个体积m,然后每个体积下,不超过该体积的情况下可以放多少该物体达到最大收益。

错误点记录：
1. 进行每个物品的数量s循环之前忘记初始化f[i][j] = f[i-1][j],使得后面f[i][j] = max(f[i-1][j] ......
    要记得上一层的初始化只能在一开始用一次
2. 第二点就是记得看上面的解释为什么不能用完全背包的思路去推导多重背包的公式.
'''

if __name__ == "__main__":
    N, V = map(int, input().split()) # 物品种类数 背包体积
    
    f = [[0] * (V + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        v, w, s = map(int, input().split()) # i物品的体积,价值,数量
        for j in range(V + 1):
                f[i][j] = f[i - 1][j] # 这里卡了很久，这里应该只能取一次i-1层进行初始化，否则后面都不是最优解
                for k in range(s + 1):
                    if k * v <= j:
                        f[i][j] = max(f[i][j], f[i - 1][j - k * v] + k * w)
    print(f[N][V])
                         
