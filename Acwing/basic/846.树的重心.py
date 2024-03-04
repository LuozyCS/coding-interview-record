'''树的重心
dfs、树形DP
感觉有点难，但是标号是简单

重心定义：
重心是指树中的一个结点，如果将这个点删除后，
剩余各个连通块中点数的最大值最小，那么这个节点被称为树的重心。

思路：
我们只需要去遍历，删掉每一个点然后去找各个连通块的大小。
此时问题变成在删掉每个点之后如何快速的计算出各个连通块的大小。
那么就需要用到dfs。

dfs的好处就是可以知道每个点的子树大小。

然后有个技巧，就是我们删掉的点，我们只需要算该点的子树大小，
然后用总的点数减去子树大小，再减去1，就是剩下的连通块大小。
'''

N = 100010
ans = N # 用来存储最大连通块的最小值
graph = {}
n = 0
state = [False] * N

def dfs(x):
    global ans, graph, n
    state[x] = True
    max_size = 0
    node_sum = 0 # 以x为根节点的子树的数量，不包含本身
    for i in graph[x]:
        if not state[i]:
            s = dfs(i) # 返回的是以i为根节点的子树数量，需要包含i节点，因为这里需要的只是排除x节点以外的子树，i当然是需要的
            node_sum += s # 用于后面算n - node_sum - 1
            max_size = max(max_size, s) # 这里比的是以x为删除点，剩下的所有子树里谁最大
    max_size = max(max_size, n - node_sum - 1)
    ans = min(max_size, ans)
    
    return node_sum + 1 # 见33行注释

def main():
    global ans, graph, n
    n = int(input())
    for i in range(n - 1):
        a, b = map(int, input().split())
        # 字典一定要这么写不然会key error
        # 无向图。ab要正反存一遍
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    dfs(1) 
    print(ans)

main()