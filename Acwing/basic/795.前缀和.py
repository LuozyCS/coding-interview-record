n, m = map(int,input().split())
nums = list(map(int, input().split()))

if __name__ == "__main__":
    
    preSum = [0]*(n + 1)
    for i in range(n):
        preSum[i+1] = preSum[i] + nums[i]

    for i in range(m):
        l , r = map(int, input().split())
        print (preSum[r] - preSum[l - 1])

