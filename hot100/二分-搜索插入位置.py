'''简单题. 回顾二分模板

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

logn当然是二分, 而且题目给了

二分感觉还是得不断尝试边界条件
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2 # 整除
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] != target:
            if nums[l] > target:
                return l
            else:
                return l + 1
        return l