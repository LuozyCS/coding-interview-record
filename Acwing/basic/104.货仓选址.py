'''贪心
不是平均  是中位数

绝对值不等式证明
https://www.acwing.com/video/316/ 
'''

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    
    nums.sort()
    res = 0
    for i in range(N):
        # 这里偷懒取N/2
        # 实际上应该考虑中位数,偶数就是两个中间任意一点,技术就是中位数
        res += abs(nums[i] - nums[int(N/2)])

    print(res)
    
main()
