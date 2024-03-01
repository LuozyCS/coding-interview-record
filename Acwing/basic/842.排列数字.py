# dfs,其实就是递归
N = 10
path = [0] * N
# True Flase也可以
state = [0] * N
n = 0

def dfs(x):
    global path, state, n
    if x == n:
        for i in range(n):
            print (path[i] , end = " ")
        print()
        return
    for i in range(n):
        if state[i] == 0:
            path[x] = i + 1
            state[i] = 1
            dfs(x + 1)
            state[i] = 0

def  main():
    global n
    n = int(input())
    dfs(0)
main()