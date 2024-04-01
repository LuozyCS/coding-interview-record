'''简单

思考:
是并查集吗?
不是, 那个叫合并集合

这个好像是贪心?

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0]) # 按左端点排序

        ans = [intervals[0]]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                if intervals[i][1] <= right:
                    continue
                else:
                    right = intervals[i][1]
                    ans[-1][1] = right
            else:
                ans.append(intervals[i])
                right = intervals[i][1]
        return ans