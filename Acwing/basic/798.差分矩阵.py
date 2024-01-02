# 注意差分矩阵是左上角的b之和为a，而不是上方所有的b！！！别搞错了
# 前缀和矩阵也是一样的道理
# 因此给差分矩阵+c其实是对右下角所有前缀和+c
# 参考图示：https://www.acwing.com/solution/content/32560/

# def insert(x1, y1, x2, y2, c):
#     b[x1][y1] += c
#     b[x1][y2 + 1] -= c
#     b[x2 + 1][y1] -= c
#     b[x2 + 1][y2 + 1] += c

# def main():
#     global a
#     global b
#     n, m, q = list(map(int, input().split()))
#     a = [[0] * m for i in range(n)]
#     b = [[0] * m for i in range(n)]
#     for i in range(n):
#         rows = list(map(int, input().split()))
#         for j in range(m):
#             a[i][j] = rows[j]

#     # 构造差分矩阵
#     for i in range(n):
#         for j in range(m):
#             if i == 0 and j == 0:
#                 b[i][j] = a[i][j]
#             elif i == 0 and j > 0:
#                 b[i][j] = a[i][j] - a[i][j - 1]
#             elif i > 0 and j == 0:
#                 b[i][j] = a[i][j] - a[i - 1][j]
#             else:
#                 b[i][j] = a[i][j] - a[i - 1][j] - a[i][j - 1] + a[i - 1][j - 1]
    
#     while(q != 0):
#         # print (q)
#         # 它的xy不对
#         y1, x1, y2, x2, c = list(map(int, input().split()))
#         x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
#         # print (x2, y2)
#         # print (m - 1, n - 1)
#         # insert(x1, y1, x2, y2, c)
#         if y2 == (n - 1) and x2 == (m - 1):
#             # print ("yes1")
#             b[y1][x1] += c
#         elif x2 < (m - 1) and y2 == (n - 1):
#             # print ("yes2")
#             # print(b[x1][y1])
#             b[y1][x1] += c
#             b[y2][x1 + 1] -= c
#         elif y2 < (n - 1) and x2 == (m - 1):
#             # print ("yes3")
#             b[y1][x1] += c
#             b[y1 + 1][x2] -= c
#         elif y2 < (n - 1) and x2 < (m - 1):
#             # print ("yes4")
#             b[y1][x1] += c
#             b[y2 + 1][x2 + 1] += c
#             b[y1][x2 + 1] -= c
#             b[y2 + 1][x1] -= c
#         q -= 1
        
#     # print(b)
#     for i in range(n):
#         for j in range(m):
#             if i == 0 and j > 0 :
#                  b[i][j] = b[i][j - 1] + b[i][j] 
#             elif i > 0 and j == 0:
#                  b[i][j] = b[i - 1][j] + b[i][j] 
#             elif i == 0 and j == 0:
#                  b[i][j] = b[i][j] 
#             elif i > 0 and j > 0:
#                 b[i][j] = b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1] + b[i][j] 

#     for i in range(n):
#         for j in range(m):
#             print(b[i][j], end=" ")
#         print(b)

# main()

# !!!!!!!!这一题里给的xy是x指第几行，y指的是第几列，反过来了！

a = [[0] * 1010 for i in range(1010)]
b = [[0] * 1010 for i in range(1010)]

def insert(x1, y1, x2, y2, c):
    b[x1][y1] += c
    b[x1][y2 + 1] -= c
    b[x2 + 1][y1] -= c
    b[x2 + 1][y2 + 1] += c

def main():
    global a
    global b
    n, m, q = list(map(int, input().split()))
    for i in range(n):
        rows = list(map(int, input().split()))
        for j in range(m):
            a[i + 1][j + 1] = rows[j]
            
    # 构造差分矩阵
    # 其实就是从ij到ij的地方加c，并且抵消前面的前缀和，使得前缀和为a。因为一开始就是0，所以这么做得到的一定是a。
    # 为什么不会有影响？因为对a做lrc操作的是，也不会影响前面。
    for i in range(n):
        for j in range(m):
            insert(i + 1, j + 1, i + 1, j + 1, a[i + 1][j + 1])

    while(q != 0):
        x1, y1, x2, y2, c = list(map(int, input().split()))
        insert(x1, y1, x2, y2, c)
        q -= 1

    for i in range(n):
        for j in range(m):
            b[i + 1][j + 1] = b[i][j + 1] + b[i + 1][j] - b[i][j] + b[i + 1][j + 1] 

    for i in range(n):
        for j in range(m):
            print(b[i + 1][j + 1], end=" ")
        print()

main()
