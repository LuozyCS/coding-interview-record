# 这题还是Trie树的应用，是835的扩充

# 如果没有思路可以先用暴力来写，然后再优化
# 第一步选第一个异或数是固定的，优化第二步，怎么选第二个异或的数更快。
# 因为第一个数肯定都得选一遍，那么有没有办法让第二个数不需要遍历所有的数呢？
# 考虑异或的特点，异或的结果是两个数的二进制位不同的地方，所以我们可以先找到最高位不同的地方，然后再找到次高位不同的地方，以此类推。

# step1 先建立一个Trie树，然后把所有的数都插入到Trie树中
# step2 遍历所有的整数，根据上述异或的特点，找到最大的异或值MAX，然后不断的更新MAX
from sys import stdin

N = 100010
M = N * 31
# 因为只会有0和1两种情况，所以可以用[0, 0]来存储
son = [[0, 0] for _ in range(M)]
idx = 0
MAX = 0
# 这道题仍然需要idx

def insert(nums):
    global son, idx
    for num in nums:
        # 把num转为二进制,前两位不需要 0b是前缀，转出来的num是个数组
        num = list(map(int, bin(num)[2:]))
        num = [0] * (31 - len(num)) + num
        # p的作用是记录当前的位置（因为idx是唯一的）
        p = 0
        for i in num:
            try: 
                if not son[p][i]:
                    idx += 1
                    son[p][i] = idx
            except: 
                print("aka", p)

            p = son[p][i]
            

def query(num):
    global son, idx, MAX
    num = list(map(int, bin(num)[2:]))
    num = [0] * (31 - len(num)) + num
    p = 0
    res = 0
    for i in num:
        # 由于是异或，所以要找到相反的数，所以如果是0就找1，如果是1就找0
        if i == 0:
            if son[p][1]:
                p = son[p][1]
                # 从二进制理解这一步，就是直接算出来异或结果，因为已经根据idx确认这里是有数字的，背模板！
                res = res * 2 + 1
            else:
                # 如果没有就求其次选0
                p = son[p][0]
                res = res * 2
        elif i == 1:
            if son[p][0]:
                p = son[p][0]
                res = res * 2 + 1
            else:
                p = son[p][1]
                res = res * 2
    MAX = max (res, MAX)
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    insert(nums)

    for num in nums:
        query(num)
    print (MAX)
main()