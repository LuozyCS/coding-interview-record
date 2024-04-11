'''简单 (这个问题的变种不简单)

我写了两种方法
'''

# 这种方法应对每个数出现三次, 找出现一次的方法也可以
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = [0] * 16
        for num in nums:
            if num >= 0:
                bits = bin(num)[2:].zfill(16)
            else:
                bits = bin(num)[3:].zfill(16)
                bits = '1' + bits[1:] # 1代表负数
            # print(bits)
            for i, bit in enumerate(bits):
                # print(bits, bit, i)
                sum[i] += int(bit)

        res = 0
        for i in range(16):
            sum[i] = sum[i] % 2
        for i in range(15, 1, -1):
            res += sum[i] * (2 ** (15 - i))
        # print(sum)
        return res if not sum[0] else -res
            
# 异或的传递性(交换结合)
# 因为其他都是双数, 所以相当于0000 与 abcd 异或, 而0 与 其他数异或都表示其他数本身
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
    # reduce:((((1+2)+3)+4)+...n)