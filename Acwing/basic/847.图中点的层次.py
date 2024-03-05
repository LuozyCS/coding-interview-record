'''bfs问题
有向图

和走迷宫差不多，第一反应就是dx dy那个数组，但是树形应该不太一样。

错误点：
1.字典类型里如果相当做hash用一开始要用数组赋值，不然后续无法append。
2.为什么一定要记录state有没有访问过？难道bfs的特点不就是第一个遇到的一定是最小值吗？
    原因：因为有环，所以可能会重复访问，所以要记录。
    具体例子：A->B, B->A, B->C。
    A开始，先访问B，然后此时距离是A0，B1.
    然后pop B， AC入对，先入A，然后再入C。
    A再pop一次，距离就变成了B1 + 1 = 2了。
    然后再找到C，距离就变成了A2 + 1 = 3了。
    然而实际上AC是2。
'''
from collections import deque

def bfs(start):
    global graph, n, dist
    queue = deque([start])
    # queue = [start]
    state = [False] * (n + 1)
    state[start] = True
    # 不能遇到最优解
    while queue:
        t = queue.popleft()
        # t = queue.pop(0)
        if t not in graph: continue
        if t == n: 
            print(dist[n])
            return
        for i in graph[t]:
            if state[i]: continue
            state[i] = True
            queue.append(i)
            dist[i] = dist[t] + 1
            if i == n:
                print(dist[n])
                return
    print("-1")


if __name__ == "__main__":
    global graph, n, dist
    n, m = map(int, input().split())

    # 并不需要二维数组存，因为已经确定是从一个固定点到其他所有点的距离了
    # dist = [[0] * (n + 10) for _ in range(n + 10)]

    dist = [0] * (n + 10)
    graph = {}
    for _ in range(m):
        a, b = map(int, input().split())
        if a not in graph:
            # 忘记提醒了，字典里这里要记得用数组，不然后续无法append
            graph[a] = [b]
        else:
            graph[a].append(b)

    bfs(1)

