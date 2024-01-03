# 仍然是双指针的做法，参考799

n, m, x = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
# 防list out of range bug

# 这个逻辑要清楚
def main():
    j = 0
    for i in range(n):
        while (N[i] + M[j]) > x:
            j -= 1
        while j < m - 1 and (N[i] + M[j]) < x:
            j += 1
        if (N[i] + M[j]) == x:
            print (i, j)
            break
    return

main()