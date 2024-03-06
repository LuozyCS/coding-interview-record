'''
就是BFS的一个应用

若一个由图中所有点构成的序列 A 满足：
对于图中的每条边 (x,y),x 在 A 中都出现在 y 之前，则称 A 是该图的一个拓扑序列。
1. 有向图才有拓扑序列。
2. 拓扑序列不唯一，也不是所有图都有拓扑序列（如果存在环一定不存在拓扑序列）。
3. 有向无环图一定存在拓扑序列，被称为拓扑图。

我的思路：
遍历所有边，保留符合拓扑序列的路径？

真实思路：拓扑排序
一个有向图，如果图中有入度为 0 的点，就把这个点删掉，同时也删掉这个点所连的边。
一直进行上面出处理，如果所有点都能被删掉，则这个图可以进行拓扑排序。

解释 任何入度为0的点可以作为起点。不会有任何一个点要求在他前面。
因此第一步就是入度为0的点入队列。
'''

from collections import deque

# 注意最终输出的拓扑序列只需要满足 “(x,y),x 在 A 中都出现在 y 之前” 。
# 因此按照思路不断的找入度为0的点即可。
# 如果同时为0说明两者不存在直接边关系。

def bfs():
    global n, m, g, in_degree
    res = [] # 拓扑序列
    queue = deque([])
    # print(in_degree)
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            res.append(i) 
    # print (res)
    while queue:
        t = queue.popleft()
        if t not in g: continue # ?
        for i in g[t]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
                res.append(i)
    if len(res) == n:
       for i in res:
           print(i, end=" ")
    else:
        print("-1")

if __name__ == "__main__":
    global n, m, g, in_degree
    n, m = map(int, input().split())
    in_degree = [0] * (n + 1)
    g = {}
    for _ in range(m):
        a, b = map(int, input().split())
        in_degree[b] += 1 # 别写反了
        if a in g:
            g[a].append(b)
        else:
            # 这里要记得= [b] 因为后面要append这里必须得是数组
            g[a] = [b]
    bfs()
    
