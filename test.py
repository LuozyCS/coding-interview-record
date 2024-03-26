'''
7

1 1 1 2 2 2 3 

'''
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    
    res = [0] * 4 # 默认4位

    for i in range(n):
        for j, k in enumerate(bin(arr[i])[2:]):
            res[j] += k
    ans = 0
    for i, j in enumerate(res):
        ans += (j % 3) * pow(2, 4 - i)
    print(ans)

main()