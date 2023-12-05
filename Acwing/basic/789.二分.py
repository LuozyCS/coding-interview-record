line1 = list(map(int, input().split()))
n = line1[0]
m = line1[1]
nums = list(map(int, input().split()))

# 用二分去查找元素要求数组的有序性或者拥有类似于有序的性质。
# 对本题而言，一个包含重复元素的有序序列，要求输出某元素出现的起始位置和终止位置，翻译一下就是：
# 在数组中查找某元素，找不到就输出−1，找到了就输出不小于该元素的最小位置和不大于该元素的最大位置。
# 所以，需要写两个二分，一个需要找到>=x的第一个数，另一个需要找到<=x的最后一个数。

# 查找不小于x的第一个位置，较为简单：
def SL(l, r, x):
    while l < r:
        mid = (l + r)//2
        if nums[mid] >= x: r = mid
        else: l = mid +1
    return l

def SR(l, r, x):
    while l < r:
        mid = (l + r + 1)//2 # 重点 自己推一下 1 2 2 3 3 4，如果不+1就会死循环
        if nums[mid] <= x: l = mid
        else: r = mid -1 # 重点  因为mid本身不等于 就得往后一位
    return r
    
if __name__ == "__main__":
    for i in range(0, m):
        x = int(input())
        l = SL(0, n - 1, x)
        if nums[l] != x: 
            l = -1
            r = -1
        else: 
            r = SR(0, n - 1, x)

        print(l,r)
        



