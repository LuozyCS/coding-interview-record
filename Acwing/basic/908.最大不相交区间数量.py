'''还是贪心

做法和上一个问题完全一样,虽然题目不一样
仔细思考
上一题选出来的区间都是不相交的,因此上一题的贪心结果一定是某种可行方案(不相交区间数量)
那么如何证明这种做法是最大的呢?ans

已知ans>=cnt,如何证明ant<=cnt

上一题中选出来的每个cnt对应一个区间的集合,在这个集合中所有的区间都是一定有交集的.

假设ans > cnt,意味着我们至少能选出cnt + 1个不相交的区间.
根据抽屉原理, 意味着某个区间内, 存在两个不相交的,这与我们的前提条件(存在一个点使得他们相交)相违背.

因此ans==cnt

######
我们回过头来看这两个问题, 其实选择最少的点让每个区间内都有一个点,就是在找不相交区间数量.(最少这个词有点迷惑视野)
'''

def main():
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(lambda x:x[1]) # 从小到大,按右端点排序
    
    cnt = 1
    right = arr[0][1]
    for i in range(1, N):
        if arr[i][0] < right:
            continue
        else:
            cnt += 1
            right = arr[i][1]
    print(cnt)
main()