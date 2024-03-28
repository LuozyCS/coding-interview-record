'''滑动窗口

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

回去看acwing的解法
'''

# import collections

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        map = collections.defaultdict(int)
        max_size = 0
        
        left = 0

        for right in range(len(s)):
            map[s[right]] += 1
            while left <= right and map[s[right]] > 1:
                map[s[left]] -= 1
                left += 1
            max_size = max(max_size, right - left + 1)
            
       
        return max_size
                