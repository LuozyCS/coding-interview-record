n = (input().split())
nums = list(map(int,input().split()))

def revers(nums):

    if len(nums) < = 1: return 0
    mid = len(nums)//2
    L = nums[:mid]
    R = nums[mid:]
    ans = revers(L) + revers(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            nums[k] = R[j]
            ans += len(L) - i
            k += 1
            j += 1
        else:
            nums[k] = L[i]
            k += 1
            i += 1
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1
    return ans

if __name__ == "__main__":
    print(revers(nums))