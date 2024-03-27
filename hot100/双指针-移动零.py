'''双指针

难点在于: 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

思考:
1. 已经提示了是双指针
2. 最终目的是保持顺序, 以及0在最后, 但是0之间是没有区别的 (即0 0 0 都是0)

那么我们遇到一个0就往后移动就可以(大致)

但是这样的方法效率比较低, 因为0会堆积.

那就把不是0的数往前移.(这个才是双指针)
'''

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """

#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 continue
#             for j in range(i, len(nums)):
#                 # i指向的是第一个0, 然后往后找第一个不是0的数然后交换
#                 if nums[j] != 0:
#                     nums[j], nums[i] = nums[i], nums[j]
#                     # print(nums)
#                     break # 别忘了break 易错

#         return nums
    

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        