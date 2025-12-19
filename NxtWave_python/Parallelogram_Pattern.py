N, T = map(int, input().split())
for i in range(1, N):
    spaces = (N-i-1) * T
    print(' '*spaces + "*"*N)