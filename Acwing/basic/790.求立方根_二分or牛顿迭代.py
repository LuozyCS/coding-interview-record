# 普通二分 直接找
n = float(input())
def bsearch(l, r):
    while r - l > 1e-8: #浮点数二分法的循环条件是r-l<1e-8,其中8是因为题目中要保留6位小数
        mid = float((l + r) /2)
        if mid*mid*mid >= n:
            r = mid
        else:
            l = mid
    return l

l = bsearch(-10000, 10000)
print("{:.6f}".format(l))

# 其实也可以用牛顿迭代法。