'''迪杰斯特拉：
从起始点到所有点的最短路径。求1到n的最短距离，如果无法走到输出-1。图中可能有自环或者重边。

而且是带权重的路径。本质是贪心来做的。dijstra并不是按照bfs搜索的。

为什么贪心找到的一定是最短？
因为每次找到的点都是到起始点最近的点。如果有更短的路径，那么这个点就不会被选中。

不举例子了，直接看算法课的ppt吧，我自己做的那个。

反正不是bfs。但是可以用优先队列来做，也可以用集合的方法来做。
优先队列不是FIFO的，而是堆实现的。

'''

# ***** 优先队列做法 ***** #
import heapq
def dijstra_priority_q(start):
    global dist, g, n
    priority_q = []
    
    # 初始化起始点的距离为0，并将起始点加入优先队列
    dist[start] = 0
    heapq.heappush(priority_q, (0, start))

    while priority_q:
        # 取出当前距离最短的点
        curr_dist, curr_node = heapq.heappop(priority_q)

        # 如果当前点已经找到最短距离，则跳过
        if curr_dist > dist[curr_node]: continue

        # 遍历当前点的邻居节点
        for neighbor, edge_weight in g[curr_node]:
            # 计算从起始点经过当前点到达邻居节点的距离
            new_dist = dist[curr_node] + edge_weight

            # 如果新的距离比已知的距离短，则更新最短距离并将邻居节点加入优先队列
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(priority_q, (new_dist, neighbor))

    if dist[n] != float('inf'):
        print(dist[n])
    else:
        print("-1")
    

# ***** 集合做法 ***** #
def dijstra_set(start):
    global dist, g, n
    # 复杂度集合做法是O(n^2)的，优先队列是O(nlogn)的
    # 那么集合的做法直接双循环就好了
    
    s = set() # 已经找到最短距离的点
    # 一开始忘了初始化1为0，导致后面debug了很久都是inf
    dist[1] = 0
    t = start
    # 记得左闭右开
    for i in range(1, n + 1):
        t = -1
        for j in range(1, n + 1):
            if j not in s and (t == -1 or dist[j] < dist[t]):
                # 为了找到当前没有访问过的，而且距离1号点最短的点。
                t = j
        if t == -1:  continue
        s.add(t)
        # 然后根据从t点出发到各个点的距离更新最短距离，如果t点到不了那个点当然是不改变
        for node, d in g[t]:
            dist[node] = min(dist[node], dist[t] + d)
    if dist[n] == float('inf'): print("-1")
    else: print(dist[n])
        

# ***** 主函数 ***** #
if __name__ == "__main__":
    global dist, g, n
    
    n, m = map(int, input().split())
    dist = [float('inf')] * (n + 1)
    # 先创建一个空的，免得后面没有，虽然这样比较trivial但是可以避免很多问题
    g = {_:[] for _ in range(2 * n)}
    for _ in range(m):
        a, b, d = map(int, input().split())
        if a not in g:
            g[a] = [(b,d)]
        elif (b,d) not in g[a]:
            g[a].append((b,d))

    # dijstra_priority_q(1)
    dijstra_set(1)
         
