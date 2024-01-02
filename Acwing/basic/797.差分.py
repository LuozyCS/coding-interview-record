# 差分和前缀和的关系 类似于 微分与积分
# 构造b为a的差分，即a为b的前缀和。
# 要想给一个区间里的a全加c，则需要O(n)
# 若使用差分数组b，只需要给bl + c，br+1 - c。
# 第一次看这个思路的时候的疑惑是，这样不是还要算一次数组a吗？效率不是一样的吗？
# 实际上是有非常多个lrc操作，才能体现出这个差分数组算法的优势（原因稍微想想）。


n, m = map(int, input().split()) 
a = list(map(int, input().split()))
l, r, c = [0]*m, [0]*m, [0]*m

for i in range(m):
    l[i], r[i], c[i] = map(int, input().split())
b = []
b.append(a[0])
for i in range(1, n):
    b.append(a[i] - a[i - 1])
for j in range(m):
    b[l[j]] += c[j]
    if r[j] == n - 1:
        break
    else:
        b[r[j] + 1] -= c[j]
# print (b)
a[0] = b[0]
for i in range(1, n):
    a[i] = a[i - 1] + b[i]
print(a)
