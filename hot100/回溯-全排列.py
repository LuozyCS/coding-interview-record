'''中等

acwing同款题目  好像是dfs那块的

思考:
    深度优先, 然后回溯.
'''
class Solution:
    def dfs(self, x, nums):
        if x == self.n:
            self.res.append(self.path[:])  # make a copy of path
            return
        for i in nums:
            if i not in self.path:
                self.path.append(i)
                self.dfs(x + 1, nums)
                self.path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.res = []
        self.path = []
        self.dfs(0, nums)
        return self.res
    
