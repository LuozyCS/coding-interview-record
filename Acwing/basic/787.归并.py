# 归并排序
# 快排：先分大小排序，再递归。归并：先递归排序，再合二为一。
# 分界点为中间位置的点，难点在于合并。而快排难点在于划分。
# 双指针。
# 平均nlogn （需要合并logn次，n除以2的logn次幂为1）
# 稳定的排序

n = int(input())
nums = list(map(int, input().split()))

res = [0]*n

def megre_sort(nums, l, r):
    if (l >= r): return

    mid = (l + r)//2

    megre_sort(nums, l, mid)
    megre_sort(nums, mid+1, r)
    k = 0
    i = l
    j = mid + 1

    while (i <= mid and j <= r):
        if nums[i] <= nums[j]:
            res[k] = nums[i]
            k += 1
            i += 1

        else:
            res[k] = nums[j]
            k += 1
            j += 1
    while i <= mid: 
        res[k] = nums[i]
        k += 1
        i += 1
    while j <= r: 
        res[k] = nums[j]
        k += 1
        j += 1
    nums[l:r + 1] = res[0:(r-l + 1)]
    
if __name__ == "__main__":
    megre_sort(nums, 0, n - 1)
    for i in nums:
        print(i, end=" ")

# 这个输出很重要