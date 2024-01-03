# 仍然是双指针
# 难点是理解题目的含义，所谓“子序列”容易有歧义

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
def main():
    if n > m:
        print ("No")
        return
    i = 0
    for j in range(m):
        if B[j] == A[i]:
            i += 1
        if i == n: 
            print ("Yes")
            return
    if i != n: print ("No")
    return

main()