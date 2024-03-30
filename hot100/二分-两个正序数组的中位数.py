'''困难 二分里经常考的题 背这题!  3-30 第一次写 要重新写

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

有个题解还不错https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/277873/cong-yi-ban-dao-te-shu-de-fang-fa-dai-ma-jing-jian

一个核心的思想是 这个中位数一定在两个数组的中位数的区间内. 
例如: 如果nums1[k/2]>=nums2[k/2], 这意味着:nums2数组的左半边都不需要考虑了, 因为肯定会比第k小的数要来得小。
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        k1 = ( len(nums1) + len(nums2) + 1 ) // 2
        k2 = ( len(nums1) + len(nums2) + 2 ) // 2

        # 作用是找到第k小的数, 注意这里说第k小是从1开始的, 所以上面是+1, +2, 而不是+0, +1, 因此第k个是nums[k - 1]
        def helper(nums1, nums2, k):
            # 保证nums1是长的那一半, 因为最后剩1一定是长的那一边剩下
            if len(nums1) < len(nums2):
                nums1, nums2 = nums2, nums1
            
            if len(nums2) == 0: 
                return nums1[k - 1] # k是第k个, 数组上是k-1
            
            if k == 1:
                return min(nums1[0], nums2[0])
            # k//2是分治思想, 意思是每边都找第k//2个数, 看看哪个大, 因为k//2肯定是小于等于k的, 那么小的那一边的k//2肯定不是第k大, 直接丢掉
            t = min(k//2, len(nums2)) # 避免上溢 而且nums2是短的那个,以短的为准
                        
            if nums1[t - 1] >= nums2[t - 1]:
                return helper(nums1, nums2[t:], k - t) # 把小的那个(比如这里是nums2), 说明肯定不是第k大数, 直接拿掉不要了, 0到t-1不要, 从t开始留
            else:                                      # 然后剩下的也不用找第k个, 而是找k - t个
                return helper(nums1[t:], nums2, k - t)
            
        
        return (helper(nums1, nums2, k1) + helper(nums1, nums2, k2)) / 2