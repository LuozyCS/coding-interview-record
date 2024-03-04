# 最左边应该是可以走的吧？那为啥不从0,0开始
# 题目里1,1的意思就是0,0

# 广度优先算法的实现，一般用优先队列实现
n, m = map(int, input().split())
# 这里要加100保证不会out of range
g = [[0] * (n+100) for _ in range(m + 100)]
dist = [[-1] * (n+100) for _ in range(m + 100)]
def bfs():
    global g, dist, n, m
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dist[0][0] = 0
    queue = [(0, 0)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            a, b = x + dx[i], y + dy[i] # 每一步只能往一个方向走一步
            # 横向移动小于n，纵向移动小于m，并且没有去过
            if a >= 0 and a < n and b >= 0 and b < m and g[a][b] == 0 and dist[a][b] == -1:
                dist[a][b] = dist[x][y] + 1
                queue.append((a, b))

    '''为什么就算有多条通路，它总能输出最小距离？
    1.因为当第一个点到达终点时，它一定是最短距离，并且会将终点变成墙（走过了就不是-1），那么其他点再也无法到达终点，也更新不了初始点到终点的距离。
    2.因为我们最终只取print(dist[n - 1][m - 1])，并且这个dist只会被最早到达的路径更新一次。
    '''
    print(dist[n - 1][m - 1])
            

def main():
    global g, dist, n, m
    
    for i in range(n): 
        g[i] = list(map(int, input().split()))
    bfs()
main()

