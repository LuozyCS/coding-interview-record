# 复习next数组,考研的时候学的很痛苦
# 参考这个学习next数组怎么求：https://blog.csdn.net/m0_73566014/article/details/132649839
# 首先明确两个名词：模式串，主串
# kmp核心思想：暴力求解每次需要匹配已经匹配过的内容，浪费算力，实际上匹配过的内容可以不用匹配了。
# 具体来说是通过next数组（由最长前缀子串变化而来）实现的。


# 是用于模式串，用于记录模式串中 各个字符对应的的前缀串 有多长的相同子串 在模式串的头部是匹配的。
# 比如a b a a b c。其中的一个前缀串头部的 a b 和尾部的 a b匹配。
# 也就是当一次匹配失败的时候， 不用从原串的指针+1位置开始，而是可以跳跃到模式串的尾部的a b位置开始。
# a b a a b “a” （原串）
# a b a a b “c” （模式串）
# 可以直接：
# a b a a b a
#       a b a a b c
# 如果是暴力法：
# a b a a b a
#   a b a a b c
# 具体看两个帖子，只需要看懂原理，为什么需要最长前缀子串就可以了，next数组生成方法在下面。
# https://blog.csdn.net/hi25779/article/details/89504487（另一个补充帖子）
# 具体看第一个帖子的“第二种next数组求法”
# 大致流程：
# 1.生成模式串的最长前缀子串数组。
# 2.上述数组，所有位往后移动一位，并且第一位改为-1，此为next数组。
# 3.使用next数组：

from sys import stdin
class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        # i从1到len
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
        return ret

n = int(stdin.readline())
pattern = stdin.readline().rstrip()
m = int(stdin.readline())
text = stdin.readline().rstrip()
kmp = KMP()
temp = kmp.search(text,pattern)
for item in temp:
    print(item,end=' ')

