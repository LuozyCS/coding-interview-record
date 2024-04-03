'''简单题

和爬楼梯差不多, 思考动态规划方程的物理意义


'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        nums = [[1]]
        for i in range(1, numRows):
            tmp = []
            tmp.append(1)
            for j in range(i - 1):
                tmp.append(nums[i - 1][j] + nums[i - 1][j + 1])

            tmp.append(1)
            nums.append(tmp)
        return nums