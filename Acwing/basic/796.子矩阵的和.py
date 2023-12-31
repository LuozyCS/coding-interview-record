a = [[0] * 1010 for i in range(1010)]
s = [[0] * 1010 for i in range(1010)]

def main():
    global a
    global s
    n, m, q = list(map(int, input().split()))

    for i in range(n):
        rows = list(map(int, input().split()))
        for j in range(m):
            a[i][j] = rows[j]

    for i in range(n):
        for j in range(m):
            s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + a[i][j]

    while(q != 0):
        x1, y1, x2, y2 = list(map(int, input().split()))
        print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])
        q -= 1
main()


