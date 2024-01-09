# 题目本身也不难
# 回忆python链表怎么写
# 删除、插入第k个数后面的数，只需要给每个数插入的时候记录一下是第k个数即可。
# 链接：https://www.acwing.com/solution/content/15276/
def add_to_head(x): # 将x添加到头节点
    global cur
    global head
    val[cur] = x
    # 若为空链表，则next[cur]指向空 -1。若不是空链表，则指向之前的头节点。
    next[cur] = head
    head = cur
    cur += 1

# 第k个输入的数其实也就是index=k的val和next，因为
# 首先 next和val是一一对应的；
# 其次，每插入一个新的数，val和next往后移一个位置。
def add(k, x): # 在第k个输入的数后面插入一个数x
    global cur
    # 这里只是把x存下来，因为val[cur]一定是空的，但是还没有指定哪个节点指向val[cur]
    val[cur] = x
    next[cur] = next[k]
    next[k] = cur
    cur += 1

def delete(k): # 删除第k个输入的数后面的数
    global head
    if k == 0: # 当k为0时，表示删除头结点
        head = next[head]
        return
    # 删除，在这里就是改变第k个数所指向的下个节点，改为下下个节点，直接跳过了。
    next[k] = next[next[k]]


N = 100010 # 操作次数的范围1≤M≤100000
val = [0] * N # 存放每个链表节点的值
next = [0] * N # 存放每个链表节点指向下一个节点的指针值，如果下一个为空，则为-1（见add_to_head）
head = -1  # head表示头节点的开始索引，当head为-1时，链表为空
cur = 1 # cur表示正在用链表中的那一个节点
# k = 0
m = int(input())
for _ in range(m):
    s, *p = input().split()
    if s == "I":
        k, x = map(int, p)
        add(k, x)
    elif s == "H":
        x = int(p[0])
        add_to_head(x)
    else:
        k = int(p[0])
        delete(k)

tail = head  # 从头节点开始遍历整个链表并输出每个节点的值
while tail != -1:
    print(val[tail], end=" ")
    tail = next[tail]

