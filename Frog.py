import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
h = [int(x) for x in input_data[1:]]

dp = [0] * N
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    cost1 = dp[i - 1] + abs(h[i] - h[i - 1])
    cost2 = dp[i - 2] + abs(h[i] - h[i - 2])
    dp[i] = min(cost1, cost2)

print(dp[N - 1])
