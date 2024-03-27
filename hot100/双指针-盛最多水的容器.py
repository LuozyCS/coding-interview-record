'''写着是双指针, 但是我感觉是贪心

思考:
1. 还是按照双指针做.
2. 然后,首先要想让容积最大,最好宽度最大,因此双指针从左右两端开始
3. 

'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 找到max( (j - i) * min(height[i], height[j]) )
        n = len(height)
        i, j = 0, n - 1
        V = 0 # 容积非负数
        # 容积由两者之间的矮的那一个决定, 因此最高那个, 每次只移动矮的那一个
        while i <= j:
            h = min(height[i], height[j])
            V = max(V, h * (j - i))
            if h == height[i]:
                i += 1
            else:
                j -= 1
        return V





