# 这题本身比较简单，主要是思考怎么模拟栈，其实就是向下生长即可

stack = [0] * 100000
top = 0
# stack[0]不存数据，当top = 0时表示栈为空
def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top > 0: top -= 1

def empty():
    global top
    if top != 0: print("NO")
    else: print("YES")
    
def query():
    global top
    if top != 0: print(stack[top])
    else: print("EMPTY")

def main():
    m = int(input())
    for _ in range(m):
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