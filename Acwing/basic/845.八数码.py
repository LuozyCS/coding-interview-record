# 还是属于BFS问题

# 第一个想法是能不能在一维数组里做，想起来之前对于取模的学习。
# x的index设为xi，xi//3就是行数，xi%3就是列数

'''一点思路都没有

困难到中等之间的题。还挺难的。

做题时的错误想法：
1.无法保证找出来的解决方案是否存在。
2.无法保证找到的解决方案时，前面顺序是否正确。

正解：
1.认真读题，如果不存在那就输出-1.
2.广度优先搜索，相当于遍历，是一层一层逐层往下搜索的。如果存在解决方案，那么一定能找到，而且找到的第一个解决方案就是最短的。
    因为我设置了if tmp not in dist:。所以一定是最短的。
3.无法保证前面的顺序是否正确：用哈希表，在python里就是字典
3.还有问题，导致我TLE。
  不能使用list的pop和append因为是O(n)的复杂度，要使用collections的deque是O(1)的复杂度。
'''


from collections import deque

def bfs(start):
    end = "12345678x"
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dist = {}
    dist[start] = 0
    # queue = [start]
    queue = deque([start])
    while queue:
        # t = queue.pop(0)
        t = queue.popleft()
        if t == end:
            print(dist[t])
            return
        k = t.find('x')
        x, y = k // 3, k % 3
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if a >= 0 and a < 3 and b >= 0 and b < 3:
                tmp = list(t)
                tmp[3 * a + b], tmp[k] = tmp[k], tmp[3 * a + b]
                tmp = ''.join(tmp)
                if tmp not in dist:
                    dist[tmp] = dist[t] + 1
                    # queue.append(tmp)
                    queue.append(tmp)
    print("-1")

start = input().replace(' ', '')
bfs(start)

