'''中等

注意可以重复使用字典中的词语, 像acwing里的完全背包?

思考:
    做不出来

    看了一眼提示, 首先需要思考dp问题里的dp数组代表着什么
    这里可以代表到第i个字母为止, 是否可以被字典里的词拼出来
'''

# 一种直观方法, 但是有一点重复计算
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         worddict = set(wordDict)
#         n = len(s)
#         f = [True] + [False] * (n)
#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 if f[i] and s[i:j] in worddict:
#                     f[j] = True
#         return f[-1]

# # 没有重复的
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         worddict = set(wordDict) # 这里不转也可以用
#         n = len(s)
#         trues = [0] # 只需要记录i指针之前有哪些是可以被拼写出来的, 然后遍历那些被拼写出来的
#         for i in range(n + 1): # 因为i是右边的指针, 是开区间
#             for j in trues:
#                 if s[j:i] in worddict:
#                     trues.append(i) # i是开区间, 因此可以直接写到trues里, 意思是s[i]之前是可以被拼写出来的
#                     break # 找到一个就可以了, 不break会死循环, 因为trues一直在更新, 会一直往前走, 直到[i:i]
#         return trues[-1] == n # 和上面一样的道理, n是s[n - 1], 如果n是trues的最后一位, 就代表0到n - 1(闭区间)是可以被拼写出来的

# 最快的     
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 容量为len(s)的背包，物品为wordDict中的单词
        # 单词可重复使用，为完全背包问题
        # 1. dp[j]：物品能否达成容量为j的背包；j：长度
        # 2. 递推式：dp[j] = dp[j] or (dp[j - wordDict[i]] and s[j - wordDict[i] : j + 1] == wordDict[i])
        # 3. 初始化：dp[0] = True, dp[j] = False
        # 3. 遍历顺序：内外层背包物品均可，均需正序
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for j in range(len(s) + 1):
            for i in range(len(wordDict)):
                if j >= len(wordDict[i]):
                    dp[j] = dp[j] or (dp[j - len(wordDict[i])] and s[j - len(wordDict[i]) : j] == wordDict[i])
        return dp[len(s)]

