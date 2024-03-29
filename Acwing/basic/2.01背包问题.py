# DP动态规划
'''理解
f[i][j]表示前i个物品,体积为j的情况下,最大的价值

f[i][j] = f[i-1][j]  # 确定不选第i个物品的情况下,体积没变仍然是j,价值也没变仍然是f[i-1][j]。
f[i][j] = f[i-1][j-v[i]] + w[i]  # 选第i个物品 
# 为什么这里是j-v[i]而不是j+v[i]?
# 意思是在确定将要选择i的情况下,在把i放到背包之前,背包的体积是j-v[i],然后再加上i的体积v[i],就是j了。

f[i][j] = max(f[i-1][j], f[i-1][j-v[i]] + w[i])  # 选或者不选第i个物品,取最大值

易错点：
    边界！
    特别是python别忘记左闭右开。
'''

if __name__ == "__main__":
    N, V = map(int, input().split())
    v = [0] * (N + 1)
    w = [0] * (N + 1)

    # 这里别忘了给到1到N
    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())
    
    # 外层是N个物品选与不选
    # 物品从1开始标号，而且0会往下取0-1因此要多开一行
    f = [[0] * (V + 1) for _ in range(N + 1)]

    # 物品标号从1开始，但是体积是从0到V
    for i in range(1, N + 1):
        for j in range(V + 1):
            f[i][j] = f[i-1][j]
            if j >= v[i]:
                # 背包容积没有可能放下i的时候不能选入背包
                # 比如当前背包里已装物品体积是3，比如f[1][3],同时物品1体积4，那么里面肯定没有物品1
                f[i][j] = max(f[i][j], f[i-1][j - v[i]] + w[i])

    # print(max(f[N][:]))      
    print(f[N][V]) # 直接找右下角就可以了


# 优化成一维数组形式
# 只需要第二个维度遍历的时候倒叙遍历(相当于遍历上一层,利用i-1层的数据,要用没算过的数,才能知道没有选择i物品的时候它的价值是多少)
    
def main():
    N, V = map(int, input().split())

    f = [0] * (V + 1)
    for i in range(N):
        v, w = map(int, input().split())
        for  j in range(V, 0, -1):
            if j >= v:
                f[j] = max(f[j], f[j - v] + w)

    print(f[V])

main()

