def qsort(arr, l, r):
    if l == r:
        return
    i, j, x = l - 1, r + 1, arr[l + r >> 1]

    while i < j:
        while True:
            i += 1
            if arr[i] >= x:
                break;
        while True:
            j -= 1
            if arr[j] <= x:
                break;
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    qsort(arr, l, j)
    qsort(arr, j + 1, r)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    qsort(arr, 0, n - 1)
    for i in arr:
        print(i, end + " ")

"""
n =int(input())
nums =list(map(int, input().split()))

def quick_sort(nums):

    if(len(nums) <=1): return nums;

    privot =nums[len(nums)//2]
    left =[x for x in nums if x < privot]
    mid =[x for x in nums if x == privot]
    right =[x for x in nums if x> privot]
    #print (" ".join(list(map(str, left))) +","+ str(mid[0]) +","+" ".join(list(map(str, right))) )
    return quick_sort(left) +mid + quick_sort(right)


if __name__ =="__main__":
    nums =quick_sort(nums)
    print(" ".join(list(map(str, nums))))

"""