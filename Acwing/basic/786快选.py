# 快速选择算法 复杂度O(n) 比快排快
# 注意是需要第k大的数！
# 先选一个x，然后比较len（left）和k，len（left）> k 就不用算right了。
# 还要注意，当len（left）< k，对于right ，k变成了k- len（left）（按情况可能再减len（middle））

n, k =int(input().split())
nums =list(map(int, input().split()))

def quick_sort(nums, k):

    if(len(nums) <=1): return nums

    privot = nums[len(nums)//2]
    left =[x for x in nums if x < privot]

    if (k <= len(left)):
        return quick_sort(left, k)

    if (k > len(left)):
        mid =[x for x in nums if x == privot]
        right =[x for x in nums if x> privot]
        return quick_sort(left, k) + mid + quick_sort(right)



if __name__ =="__main__":
    out =quick_sort(nums, int(k))
    print(out[int(k) - 1])