# 这题虽然提示了栈，但是我基本没有思路
# 看了题解思路，就是让栈内保持单调增
# https://www.acwing.com/solution/content/27437/

stack = []
def main():
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N):
        while len(stack) != 0 and stack[-1] >= nums[i]:
            stack.pop()
        if len(stack) == 0:
            print("-1", end=" ")
            stack.append(nums[i])
        elif stack[-1] < nums[i]:
            print(stack[-1], end=" ")
            stack.append(nums[i])


main()