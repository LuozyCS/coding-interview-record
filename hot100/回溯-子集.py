'''中等


代码

测试用例

测试结果
测试结果
78. 子集
中等

相关标签
相关企业
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集
（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

** 注意 这题不需要全排列了

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

'''

# 回溯方法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)
        path = []
        def dfs(i):
            res.append(path[:])
            
            # 用树的思想去想这个例子[0, 1, 2], 之所以用循环, 是因为一旦这个点选过了, 同一个深度就不能再选
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return res
