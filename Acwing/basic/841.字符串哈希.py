# 和模拟散列表差不多
# 第一反应是前缀和
# 字符串前缀哈希法
'''
    直接看y总视频就懂了
    思路：
    https://www.acwing.com/solution/content/24738/
    ABCDE 与 ABC 的前三个字符值是一样，只差两位，
    乘上P的二次方把 ABC 变为 ABC00，再用 ABCDE - ABC00 得到 DE 的哈希值。
    然后因为这个字符串转为P进制的数，这个数很大，就要用一个mod来取余(模)。
    把这个很大的数映射到一个很小的数的范围内。

    注意
    1: 不能映射成0，否则A AA 都会映射成0
'''

n, m = map(int, input().split())
s = input()
pre_hash, pre = [0] * (n + 1), [1] * (n + 1)
mod = 2 ** 64
def get(l, r):
    global pre_hash, pre, mod
    # 这里就可以解释为什么需要pre数组，因为不一定是十进制。当然也可以写成是131 ** (r - l + 1) 但是可能会有重复的冗余计算  直接算一次存好快一点
    return (pre_hash[r] - pre_hash[l - 1] * pre[r - l + 1])% mod
def main():
    global pre_hash, pre, mod
    # 把字符串看成P进制的数，这里P取131 是因为取得的字符的为ascii码，数值<=127，为了尽可能保证获取的hash值的唯一性，因此需要让s为一个大于127的质数，而为了提高散列密度，又要使s尽可能小，因此，大于127的最小质数，就是131。这个值具有最佳的散列质量和散列密度。
    # 就是840所说的，取一个大于n的最小质数
    # p取131或者13331，那么mod取2^64，这个是经验值
    p = 131
    
    # 这里不能用前缀和，加法不能唯一的表示一个字符串，y总这里用的是进制
    for i in range(1, n + 1):
        # 下面这两句为什么要取模？
        # 直接原因：因为这个字符串转为P进制的数，这个数很大，就要用一个mod来取余
        # 根本原因？理由？从i = 1开始带入进去，第一个字符就会被取模从而生成第一个hash值
        # 比如ABC字符串，AB的字符串就会是在A的hash值的基础上构造的，A * p + B再取模得到第二个hash值
        pre_hash[i] = (pre_hash[i - 1] * p + ord(s[i - 1])) % mod
        pre[i] = (pre[i - 1] * p) % mod
    for _ in range(m):
        l1, r1, l2, r2 = map(int, input().split())
        if get(l1, r1) == get(l2, r2):
            print('Yes')
        else:
            print('No')

main()