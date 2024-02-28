# 还是并查集
# 本质上还是并查集，主要是脑子要转过弯来
N = 100010
# 多维护一个数组size，表示以i为根的集合的元素个数
# 不要老是去想那些奇奇怪怪的操作，每到算法题考的知识点都是固定的
p, size = [0] * N, [1] * N

def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return p[x]

def main():
    n, m = list(map(int, input().split()))
    for i in range(n):
        p[i] = i
    for _ in range(m):
        s = list(input().split(" "))
        op = s[0]
        
        if op == 'C':
            a, b = int(s[1]), int(s[2])
            A = find(a)
            B = find(b)
            # 避免在同一个块总重复计算
            if A != B:
                size[find(b)] += size[find(a)]
            # 要计算size后再合并集合
            p[A] = B
        elif op == 'Q1':
            a, b = int(s[1]), int(s[2])
            if find(a) == find(b):
                print('Yes')
            else:
                print('No')
        else:
            a = int(s[1])
            print(size[find(a)])

main()
            
        