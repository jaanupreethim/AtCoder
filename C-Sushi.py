N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

i = 0
j = 0
sushi_count = 0

while i < N and j < M:
    if B[j] <= 2 * A[i]:
        sushi_count += 1
        i += 1
        j += 1
    else:
        i += 1

print(sushi_count)
