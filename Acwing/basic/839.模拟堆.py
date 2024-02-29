# 比起手写堆多了一个第k个数的操作
# 比手写堆难了不少，需要一个hp和ph数组
N = 100010
heap = [0] * N
size = 0
hp = [0] * N

def down(x):

def up(x):


def main():
    n = int(input())
    for _ in range(n):
        s = list(input().split(" "))
        if s[0] == "I":
            size += 1
            heap[size] = int(s[1])
            up(size)
        elif s[0] == "PM":
            print(heap[1])
        elif s[0] == "DM":
            heap[1] = heap[size]
            size -= 1
            down(1)
        elif s[0] == "D":
            k = int(s[1])
            heap
        elif s[0] == "C":
            
main()