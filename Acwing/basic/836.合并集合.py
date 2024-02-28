# 意思是比如输入数字5，那么所有的数字就是1,2,3,4,5
# 面试笔试高频，代码很短而且思路精巧
# 基本上是O(1)
# 只有经过路径压缩的并查集才能做到O(1)
N = 100010
p = [0] * N

# 返回x所在集合的编号（祖宗节点）+ 路径压缩
def find(x):
    # p[x] == x 说明x是根节点, y总用递归写的，路径压缩就在这里面
    # 我感觉可能是python的递归爆栈了
    while p[x] != x:
        p[x] = p[p[x]]  # 路径压缩
        x = p[x]
    # 这俩好像效率是一样的  但是递归才能路径压缩到祖宗节点，循环才能到爷爷节点。非常奇怪。因为改成cpp写这俩差不多
    # if p[x] != x:
    #     p[x] = find(p[x])
    return p[x]

def main():
    n, m = map(int, input().split())
    # 初始每个元素的父节点就是自己，自己就是树根
    for i in range(n):
        p[i] = i
    for _ in range(m):
        op, *nums = input().split()
        a, b = map(int, nums)
        if op == 'M':
            p[find(a)] = find(b)
        else:
            if find(a) == find(b):
                print('Yes')
            else:
                print('No')
main()