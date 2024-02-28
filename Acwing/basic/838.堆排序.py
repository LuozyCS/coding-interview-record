N = 100010
heap = [0] * N
nums = [0] * N
size = 0 # 从1开始计算

def down(x):
    global heap, size
    while x * 2 <= size:
        # 保证t是左右子树中最小的
        t = x
        if heap[x * 2] < heap[t]:
            t = x * 2
        # 并不需要同时判断右子树是否存在或者右子树是否比t小，因为可以保证t是左右子树中最小的
        if x * 2 + 1 <= size and heap[x * 2 + 1] < heap[t]:
            t = x * 2 + 1
        # t == x为什么要break？因为t == x说明左右子树都比x大，不需要再下沉了
        if t == x:
            break
        heap[x], heap[t] = heap[t], heap[x]
        x = t

def up(x):
    global heap
    # x // 2 > 0是为了防止越界
    while x // 2 > 0 and heap[x] < heap[x // 2]:
        heap[x], heap[x // 2] = heap[x // 2], heap[x]
        x = x // 2

def main():
    global size, heap, nums
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    # 从小到大输出，小根堆
    for i in range(n):
        size += 1
        heap[size] = nums[i]
        up(size)
    # print(heap)
    for _ in range(m):
        print(heap[1], end=' ')
        heap[1] = heap[size]
        size -= 1
        down(1)

main()