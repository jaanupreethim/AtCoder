import math

N = int(input().strip())
valid_K = set()

limit_N_minus_1 = int(math.isqrt(N - 1))
for i in range(1, limit_N_minus_1 + 1):
    if (N - 1) % i == 0:
        if i >= 2:
            valid_K.add(i)
        if (N - 1) // i >= 2:
            valid_K.add((N - 1) // i)

limit_N = int(math.isqrt(N))
for i in range(2, limit_N + 1):
    if N % i == 0:
        for k in (i, N // i):
            if k >= 2:
                temp_N = N
                while temp_N % k == 0:
                    temp_N //= k
                if temp_N % k == 1:
                    valid_K.add(k)

if N >= 2:
    valid_K.add(N)

print(len(valid_K))
