'''中等

感觉是并查集.  而且只要求求出长度

确实是并查集

https://leetcode.cn/problems/longest-consecutive-sequence/solutions/2359072/python-128-ha-xi-bing-cha-ji-dong-tai-gu-wmko

三种解法  并查集  哈希  dp
'''

# 这是并查集
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## 并查集
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            u, v = find(u), find(v)
            if u != v:
                parent[v] = u # 注意传进去的 u < v，把小值 u 作为根节点
                size[u] += size[v]
        nums = set(nums)
        parent = {num: num for num in nums}
        size = {num: 1 for num in nums}
        res = 0
        for num in nums:
            if num + 1 in parent:
                union(num, num + 1)
            res = max(res, size[find(num)]) # 注意这里要用find(num)找到根节点，用根节点的大小去更新结果
        return res
    

# 哈希查找的方法, 巧妙的点在于要找是否是左端点
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## 哈希判断
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums: # 如果前一位的值不在集合里，就是有效左端点
                cnt = 0
                while n in nums:
                    cnt += 1
                    n += 1
                res = max(res, cnt)
        return res





        

