# 散列表 hash函数 一个映射关系（时间复杂度O(1)）
# 离散化是一种特殊的hash函数，需要保序，即保证原来的大小关系
# 开放寻址法和拉链法  这两个方法都很多人用。

# 拉链法就是用领接链表来解决冲突
# 开放寻址法
# 算法题里的哈希表一般只有添加或者查找某个数
# 若真的要实现删除，而是在那个点上开一个布尔变量，表示这个点被删除了

# 哈希函数的模  最好取一个质数  而且离2的整数次幂越远越好  这样可以保证哈希函数的均匀性，减少冲突

# 具体哈希  就是取模（数学上称之为取余数）
# 比如数据范围是0-100 要映射到10的散列表里，那么100 90 50...都回映射到0 因为取余数是0 
# 而5 15 25... 都是到5。实现了映射的效果。
'''找到大于n的最小质数
i = 100000
while True:
    i += 1
    flag = True
    j = 2
    # 为什么用平方，因为一个数的因子不会超过它的平方根，假如j * j > i, 那这个时候算i % j == 0是没有意义的，因为一定存在一个小于j的因子k，k * j = i，此时k要么不存在，要么就已经算过了，所以不用再算了
    while j * j <= i:
        if i % j == 0:
            flag = False
            break
        j += 1
    if flag:
        print(i)
        break
'''

# 开放寻址法不需要链表，只需要一个数组，但是数组的长度一般要到数据量的2-3倍


# N = 100003 # 大于10w最小的质数
N = 200003  # 大于20w最小的质数
outside = 10e9 + 10 # 用来表示不存在的数
h = [outside] * N

def find(x):
    global h
    # 如果存在，返回x的位置，不存在则返回插入的位置
    k = abs(x) % N # y总用的是 (x % N + N) % N
    while h[k] != outside and h[k] != x:
        k += 1 # 线性探测
        if k == N:
            # 看到最后一个坑位都有人，那就回头看第一个坑位
            k = 0
    return k
def main():
    global h
    n = int(input())
    for _ in range(n):
        op, num = list(input().split(" "))
        num = int(num)
        if op == "I":
            k = find(num)
            h[k] = num # 插入 如果存在就覆盖，因为数值一样。不存在就在这里插入
        else:
            k = find(num)
            if h[k] == outside:
                print("No")
            else:
                print("Yes")
main()