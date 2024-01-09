# 写了单链表就来看看双链表
# 双链表就是双向链表
# 非常妙的做法：一开始默认有个头和尾，假的头尾在里面 


N = 100010
val = [0] * 100010
back = [0] * 100010
next = [0] * 100010
#初始化
# 不写head 和 tail
# next[0]存头节点，back[1]存尾节点
next[0], back[1], cur = 1, 0, 2

# 实际上有个假的头尾，我人为设计的，便于操作

# 默认是往右侧插入一个数
def add(k, x):
    global val, back, next, cur;
    # 对当前节点处理
    val[cur] = x 
    next[cur] = next[k]
    back[cur] = k
    # 对后节点的back处理
    back[next[k]] = cur
    # 对前节点的next处理
    next[k] = cur
    cur += 1

# 将第 k 个插入的数删除
def remove(k):
    next[back[k]] = next[k]
    back[next[k]] = back[k]

def main():
    global val, back, next, cur
    m = int(input())
    while(m):
        m -= 1;
        s = list(input().split(" "))
        opt = s[0]
        if(opt == "L"):
            x = int(s[1])
            add(0, x)
        elif(opt == "R"):
            x = int(s[1])
            add(back[1], x)
        elif(opt == "D"):
            k = int(s[1])
            # 这里+1 是因为我们默认有个假的头节点。下面也一样
            remove(k + 1)
        elif(opt == "IL"):
            k = int(s[1])
            x = int(s[2])
            add(back[k + 1], x)
        else:
            k = int(s[1])
            x = int(s[2])
            add(k + 1, x)
    i = next[0]
    # i != 1   即，i没有到尾节点
    while(i != 1):
        print(val[i], end=" ")
        i = next[i]
main()
