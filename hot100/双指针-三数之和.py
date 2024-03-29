'''双指针
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ,
同时还满足 nums[i] + nums[j] + nums[k] == 0 。
请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

思考:
不会 直接懵了
然后跑去看了acwing, 双指针 就是单调性

可不可以用哈希

哈希还是不如排序+双指针
'''

# 我下面的写法超时了, 感觉是因为没有去重
# import collections
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """

#         nums.sort()
#         # 因为是要求最终值等于0
#         # 那么可不可以固定一个数k, 只需要找到i + j = -k
#         # 有点像前两天做的哈希-两数相加, 注意只是像, 并不是

#         # map = collections.defaultdict(int)
#         res = set()
#         print(nums)
#         n = len(nums)
#         # 应该算nlogn + n^2
#         for k in range(n):
#             # k固定了之后, 因为是排序的数组, 那另外两个一定是一左一右逼近k
#             i, j = 0, n - 1
            
#             while i < j:
#                 print(i, j, k)
#                 print(res)
#                 if i == k:
#                     i += 1
#                 if j == k:
#                     j -= 1
#                 if i == j:
#                     break
#                 if nums[i] + nums[j] == -nums[k]:
#                     print("0")
#                     a = [nums[i], nums[j], nums[k]]
#                     a.sort()
#                     res.add(tuple(a))
#                     i += 1
#                     j -= 1
#                     # 记得双指针的单调性, 当相等的时候, 
#                     # 说明此时已经达到一个平衡, 不可能单边加i或者单边减j, 必须同时操作
#                 elif nums[i] + nums[j] > -nums[k]:
#                     print("1")
#                     j -= 1
#                 elif nums[i] + nums[j] < -nums[k]:
#                     print("2")
#                     i += 1
#         return list(res)

            

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 如果 nums 个数 < 3，肯定组不成三元组
        if len(nums) < 3:
            return []
        # 对 nums 进行排序，这样在后面的时候可以减少重复带来的问题
        nums.sort()

        # res 存储最后的结果，set 集合的特点是无序且无重复
        res = set()

        for i in range(len(nums)):

            # 元素去重
            if i > 0 and nums[i] == nums[i -1]:
                continue

            # 初始化哈希表。
            hash = {}

            for j in range(i+1, len(nums)):

                # 下面这个比较难理解, 如果nums[j]在哈希表里, 说明之前有一个hash[-nums[i]-nums[x]] = 1操作
                # 意思是之前的那个x表明, 在当前i情况下, 需要一个数-nums[i]-nums[x]才能使得三元组为0

                # 如果不在哈希表中，加入哈希表(加入-nums[i]-nums[j]表明需要这个数字使得当前j的三元组为0, 下次出现这个数的时候就说明找到这个为0三元组了)
                if nums[j] not in hash:
                    hash[-nums[i]-nums[j]] = 1
                # 如果在哈希表中，则存在三元组
                else:
                    res.add((nums[i],-nums[i]-nums[j],nums[j]))

        return list(res)

