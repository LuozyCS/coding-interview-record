'''子串

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

必须是连续的.

不能是滑动窗口, 因为存在负数, 指不定谁大谁小.
也不可以双指针, 一样的道理, 因为存在负数.

思考:
先试试暴力: 结果超时

试试前缀和

最后没做出来  是前缀和 + 哈希
'''

# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int  # return type的意思
#         """
#         # 暴力
#         cnt = 0 
#         for i in range(len(nums)):
#             kk = 0
#             for j in range(i, len(nums)):
#                 kk += nums[j]
#                 if kk == k: 
#                     cnt += 1
#                     # 这里不能break 因为有负数            
#         return cnt
                    
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int  # return type的意思
        """
        # 要求的连续子数组
        count = 0
        n = len(nums)
        preSums = collections.defaultdict(int)
        preSums[0] = 1

        presum = 0
        for i in range(n):
            presum += nums[i]
            
            # 下面这个方法很巧妙, 举个例子
            # nums 1, 2, 3  k = 3
            # pre  1, 3, 6
            # 那么当指针i=2时, presum - k就是6 - 3 = 3  而3的前缀和是存在的, 也就是6之前存在一个连续的子串和等于3
            # 当i=1时, 3-3 = 0 预设0也存在(就是从头开始)
            # if preSums[presum - k] != 0:
            count += preSums[presum - k]   # 利用defaultdict的特性，当presum-k不存在时，返回的是0。这样避免了判断

            preSums[presum] += 1  # 给前缀和为presum的个数加1
            
        return count
        






