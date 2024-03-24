'''贪心


没秒

理解错题目了  等待时间是不包括自己打水时间的



'''

if __name__ == "__main__":
    N = int(input())

    arr = list(map(int, input().split()))

    arr.sort(key = lambda x:x)

    l = len(arr)
    res = 0
    for i in range(1, N):
        res += arr[i - 1] * (l - i) 

    print(res) 