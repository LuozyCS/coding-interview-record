# 先按照l排序，然后遍历。
# 题目本身不难，难点在于如何理解为什么这样遍历的方式成立，不会漏掉某些区间。
# 因为第一步先对区间的l进行排序了,而且在第二个if里不断拓宽区间。
# 这样可以保证不漏掉。具体细节自己思考。

n = int(input())
arr = []
for _ in range(n):
    l, r = map(int, input().split())
    arr.append((l, r))

arr.sort(key = lambda x:x[0])

st = arr[0][0]
ed = arr[0][1]
num = 1
for i in range(1, n):
    if arr[i][1] <= ed:
        # 这段被合并
        continue
    if arr[i][0] <= ed and arr[i][1] >= ed:
        # 延长这个区间
        ed = arr[i][1]
    if  arr[i][0] > ed:
        # 多了一个区间合并不了
        num += 1
        st = arr[i][0]
        ed = arr[i][1]
print (arr)