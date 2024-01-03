# 这题用双指针,讲解：https://www.acwing.com/solution/content/74880/
# 不包含重复的意思是,不一定需要连续重复,这一段数字中,重复出现两个2比如2,1,2也算是重复子序列。
# 所以1,2,2,3,5的最长连续不重复子序列是3.

'''
/
1 2 3 4 5 2 7 8 9
j i
首先 i=0,j=0 i一直往前走,j还是在0的位置,因为没有重复数字,
res=5,当i=5时是2,有重复数字,则此时s[a[5]] = 2,则执行s[a[j]]-,s[a[0]]- = 0;j = 1;
此时s[a[5]]仍然等于2,j=j+1=2,继续往前移动,所有数的次数都归为0,
直到j到i的位置j=5,s[a[j]]-=s[a[5]]- = 1,则接下来i就可以往前走了,
最终得到最长不包含重复的数的连续区间。
/
'''

# 以下是我一开始写的，实际上是O(n^2)的复杂度，因为j每次都重置回i的位置，但这个实际上是没必要的。
# 双指针是O(2n),因为j和i都只走一遍。
# n = int(input())
# nums = list(map(int, input().split()))

# def main():
#     max_len = 0
#     for i in range(n - 1):
#         tmp_len = 1
#         tmp = nums[i]
#         record = [0] * 100000
#         for j in range(i + 1, n):
#             record[tmp] += 1
#             if record[nums[j]] >= 1:
#                 break
#             else:
#                 tmp = nums[j]
#                 tmp_len += 1
#         if max_len < tmp_len : max_len = tmp_len
#     print(max_len)
#     return

# main()

# 真正的双指针做法
n = int(input())
nums = list(map(int, input().split(' ')))
# 一定要多给10，不要头铁，边界条件就是这么恶心
record = [0] * 100010


def main():
    global nums
    global record
    ans = 0
    j = 0
    for i in range(n):
        record[nums[i]] += 1
        while j <= i and record[nums[i]] > 1:
            record[nums[j]] -= 1
            j += 1
        ans = max(ans, i - j + 1)
    print(ans)
    return
main()
