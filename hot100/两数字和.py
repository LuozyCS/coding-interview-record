'''哈希

如果是O(n^2)那就双循环,很简单.

如果要求小于O(n^2),需要用到哈希.
重点是怎么解决数组中出现重复数字的情况,或重复使用某数的情况.

错误点提示
不要瞎考虑优化,因为有负数的情况,直接做普遍情况

然后这种做法的内存消耗肯定是比双循环大的,主要是看运行时间.
然后我的运行时间就是第一梯队,没问题的.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 所有数存到字典里, 然后遍历每个数, 查看是否存在那个补数
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                dict[num].append(i)
            else:
                dict[num] = [i]

        for i, num in enumerate(nums):
            print(num)
            # 避免重复
            del dict[num][dict[num].index(i)]
            tmp = target - num

            # 存在这个补数, 而且这个补数不是刚刚被删除的本次查询数
            if tmp in dict and len(dict[tmp]) != 0:
                res = []
                res.append(i)
                res.append(dict[tmp][0])

                return res

            dict[num].append(i)
