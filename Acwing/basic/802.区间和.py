# 有多种做法：
# 1.如果数据范围小，没有10^9这么多，只有10^5，那么前缀和就可以。
# 2.另外也可以用线段树去解决。
# 3.acwing里讲到的离散化+二分+前缀和的做法。

# 链接：https://www.acwing.com/solution/content/9962/

def find(x):
    """二分查找模板,从索引数组alls中找到大于等于x的最小的索引"""
    l = 0
    r = len(alls)-1
    while l<r:
        # 也可以用(l+r)>>2
        mid = (l+r)//2
        if alls[mid]>=x: r = mid    # ！！！if条件忘记了=号
        else: l = mid+1
    return l+1    # 因为要计算前缀和，所以加1保证索引从1开始

if __name__=="__main__":
    n, m = map(int, input().split())
    N = 300010
    a = [0]*N    # 用于存储离散化后的索引和对应值，其中索引对应离散化后的索引，值对应离散化前索引的取值
    s = [0]*N    # 存a数组的前缀和数组

    add = []    # 存储插入操作的二元组
    query = []    # 存储查询操作的二元组

    alls = []    # 存储离散化前输入的所有索引，n+2*m

    # 和我思路的不同就是，把每个查询的l和r都放进去了，这样就不需要考虑这些边界条件了
    for i in range(n):
        x, c = map(int, input().split())
        add.append((x, c))
        alls.append(x)

    for i in range(m):
        l, r = map(int, input().split())
        query.append((l, r))
        alls.append(l)
        alls.append(r)

    alls = list(set(sorted(alls)))    # 将alls数组排序并去重


    # 1. 处理插入
    for x, c in add:
        # 不能直接把x放到a里的原因是：
        # x是没有离散化的index，经过find(x)后得到的是离散化后的alls数组中x对应的位置
        x2 = find(x)
        a[x2] += c

    # 2. 处理前缀和
    for i in range(1, len(alls) + 1):
        s[i] = s[i - 1] + a[i]

    # 3. 处理查询
    for l, r in query:
        l2 = find(l)
        r2 = find(r)
        res = s[r2] - s[l2 - 1]
        print(res)


