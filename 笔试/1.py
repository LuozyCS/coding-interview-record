# 小红有π个正方形，正方形的边长分别是4:，第;个正方形的四个顶点坐标为 (0,0),(qī,0),(0,q;),(qi,q;)。
# 小红想知道二维平面内是否存在一个点，恰好被k个正方形覆盖。
# 如果存在，输出"YES"，否则输出"NO"。

def is_covered(n, k, lengths):
    
    lengths.sort()
    lengths.reverse()
    cnt = []
    exist = set()
    print(lengths)
    for length in lengths:
        # 该边长下重叠的正方形数量
        if length in exist:
            cnt[-1] += 1
        else:
            exist.add(length)
            cnt.append(1)
    print(cnt)
    for c in cnt:
        if k - c > 0:
            k -= c
            continue
        elif k - c == 0:
            return "YES"
        else:
            return "NO"
    

if __name__ == "__main__":
    t = int(input().strip())
    res = []
    for _ in range(t):
        tmp = list(map(int, input().strip().split()))
        n, k = tmp[0], tmp[1]
        lengths = list(map(int, input().strip().split()))
        
        if n < k:
            res.append("NO")
            continue
        
        res.append(is_covered(n, k, lengths))

    for _ in res:
        print(_)

    