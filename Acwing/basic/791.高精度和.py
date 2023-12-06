n = int(input())
m = int (input())

print (n + m)

# 因为python数字理论上可以无限大，所以可以这么做
# 用cpp的话需要数组输入再进位加

# #include <iostream>
# using namespace std;

# const int N = 100010;
# int A[N], B[N], C[N];

# int Add(int a[], int b[], int c[], int cnt) {

#     int t = 0;//t表示进位

#     for (int i=1; i<=cnt; i++) {
#         t += a[i] + b[i];//进位加上a和b第i位上的数
#         c[i] = t % 10;//c的值就是进位的个位数
#         t /= 10;//把t的个位数去掉只剩下十位数，即只剩下这个位置的进位
#     }
#     if (t) c[++cnt] = 1;//如果t==1，表示还有一个进位，要补上

#     return cnt;
# }

# int main() {

#     string a, b;
#     cin >> a >> b;  


#     //A和B倒着放进int数组，因为有进位，倒着放容易处理
#     int cnt1 = 0;
#     for (int i=a.size()-1; i>=0; i--)
#         A[++cnt1] = a[i] - '0';

#     int cnt2 = 0;
#     for (int i=b.size()-1; i>=0; i--)
#         B[++cnt2] = b[i] - '0';

#     int tot = Add(A, B, C, max(cnt1, cnt2));

#     //因为A和B是倒着放的，所以C也要倒着输出
#     for (int i=tot; i>=1; i--)
#         cout << C[i];
# }

# //作者：lyclyc_NSP
# //链接：https://www.acwing.com/solution/content/10016/
