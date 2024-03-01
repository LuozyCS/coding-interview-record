# dfs,其实就是递归
N = 10
path = [0] * N
state = [0] * N
n = 0

def dfs(x):
    global path, state, n
    if x == n:
        print(path[:n])
        return
    for i in range(n):
        if state[i] == 0:
            path[x] = i
            state[i] = 1
            dfs(x + 1)
            state[i] = 0

def  main():
    n = int(input())
    dfs(0)
main()