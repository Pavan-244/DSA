N = 10
triangle = [[] for _ in range(N)]
num = 1
for col in range(N):
    for row in range(col, N):
        triangle[row].append(num)
        num += 1
for row in triangle:
    print(*row)


    
    