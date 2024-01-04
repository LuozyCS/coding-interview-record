# 位运算  算了这个别管了 感觉基本不会问。
# 回忆：原码、补码、反码：https://www.cnblogs.com/goahead--linux/p/10904701.html

# Python偷懒版
N = int(input())
sequence = list(map(int, input().split()))


for i in range(N):
    res = 0
    sequence[i] = bin(sequence[i])
    for u in range(len(sequence[i])):
        if sequence[i][u] == '1':
            res += 1
    print(res, end = ' ')

# #include <iostream>
# using namespace std;

# int main()
# {
#     int t;
#     cin >> t;
#     while (t -- )
#     {
#         int res = 0;
#         int x;cin >> x;
#         for (int i = 32; i > 0; i --)
#         {
#             if (x >> i & 1) res ++ ;
#         }
#         cout << res << ' ';
#     }
#     return 0;
# }