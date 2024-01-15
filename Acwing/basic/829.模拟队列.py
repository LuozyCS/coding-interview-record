# 用什么数据结构模拟队列？感觉list有点麻烦
# 解决思路，仍然是用append进行入队列操作，list最后一个就是对尾部（对尾如队列，队头出队列），但是记录队头位置

# 应该不用初始化成100010
que = []
que_top = 0

def push(x):
    que.append(x)

def pop():
    global que_top
    que_top += 1

# 判断空的方法如下：只有que_top == len(que)时，即此时que[que_top]指向一个que外一个的位置时，为空队列
def empty():
    global que_top
    if que_top - len(que) - 1 == -1: print("YES")
    else: print("NO")
    
def query():
    if que_top - len(que) - 1 != -1: print(que[que_top])
    

def main():
    global que_top
    m = int(input())
    for _ in range(m):
        # print ("***")
        # print (que_top)
        # print (que)
        p = input().split()
        if p[0] == "push":
            push(int(p[1]))
        elif p[0] == "pop":
            pop()
        elif p[0] == "empty":
            empty()
        elif p[0] == "query":
            query()

main()
