# 有多种做法：
# 1.如果数据范围小，没有10^9这么多，只有10^5，那么前缀和就可以。
# 2.另外也可以用线段树去解决。
# 3.acwing里讲到的离散化+二分+前缀和的做法。


def findl(l, r, x):
    while l < r:
        mid = (l + r) // 2
        if q[mid][0] >= x: r = mid
        else: l = mid + 1
    return l

def findR(l, r, x):
    while l < r:
        mid = (l + r + 1)//2 
        if q[mid][0] < x: l = mid
        else: r = mid -1 
    return r

def main():  
    n, m =map(int, input().split())
    global q
    q, Q = [], []  
    for _ in range(n):
        x, c = map(int, input().split())
        Q.append((x, c))
    Q.sort()
    # 对一个x可能有多次加c操作
    q.append(Q[0])
    j = 1
    for i in range(1, n):
        if Q[i - 1][0] == Q[i][0]:
            q.append((Q[j][0], Q[j][1] + Q[i][1]))
        else:
            q.append((Q[i][0], Q[i][1]))
            j += 1
    n = len(q)
    # 计算c的前缀和
    for i in range(1, n):
        q[i] = (q[i][0], q[i][1] + q[i - 1][1])
        
    for _ in range(m):
        res = 0
        l, r = map(int, input().split())
        # 让l，r找到左右边界
        l = findl(0, len(q) - 1, l)
        r = findR(0, len(q) - 1, r)
        print (l, r)
        if l == 0: res = q[r][1]
        else : res = q[r][1] - q[l - 1][1]
        print(res)

main()