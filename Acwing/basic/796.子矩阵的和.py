n, m, q = input().split()
# arr = np.ones((n, m))
# qs = np.ones((q, 4))
arr = [[]]
qs = [[]]
for i in range(int(n)):
    arr[i][:] = input().split()
for j in range(int(q)):
    qs[j][:] = input().split()
