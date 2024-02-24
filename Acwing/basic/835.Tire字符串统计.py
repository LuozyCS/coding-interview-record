# 这题除了暴力方法我没想到其他的
# 这题是Tire树的应用 （字典树）
# 用来 快速 存储 和 查找 字符串集合 的数据结构
# 一般字符的类型不是很多
# https://blog.csdn.net/raelum/article/details/128885107  参考该博客
# 难点在于如何理解并实现
# y总的Trie树用的是数组存，其核心在于idx，我们可以看到idx是一直自增长的，所以说，不同的字符占用的下标一定不一样，这句话很重要，举个例子细细体会一下，假设’abcdg’和’abcef’，’abc’是相同的，所以下标在son里都是一样的，但是’d’和’e’两个字符不相同，必然导致idx会自增长，所以’d’和’e’在son[c]这26个下标处必然处于不同的位置，这就实现了’c’同时指向’d’和’e’两个字母了。
from sys import stdin
N = 100010
idx = 0
cnt = [0] * N
son = [[0] * 26 for _ in range(N)]

def insert(str):
    global son, idx
    p = 0
    for i in range(len(str)):
        # ord() 函数是 chr() 函数（对于8位的ASCII字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
        u = ord(str[i]) - ord('a')     
        # 如果这个字符没有被创建过，则赋值idx+1创建  
        if not son[p][u]:
            idx += 1
            son[p][u] = idx
        p = son[p][u]
    # 在最后给这个唯一的idx计数+1代表这个字符串出现过
    cnt[p] += 1

def query(str):  
    p = 0 
    for i in range(len(str)):
        u = ord(str[i]) - ord('a')
        if not son[p][u]:
            print(0)
            return
        p = son[p][u]
    print(cnt[p])

def main():
    n = int(stdin.readline().rstrip())
    for i in range(n):
        # 这里不需要压缩的写法
        op, str = stdin.readline().rstrip().split()
        if op == 'I':
            insert(str)
        elif op == "Q":
            query(str)
main()