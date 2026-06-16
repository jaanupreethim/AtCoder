import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])

dp0 = int(input_data[1])
dp1 = int(input_data[2])
dp2 = int(input_data[3])

idx = 4
for i in range(1, N):
    a = int(input_data[idx])
    b = int(input_data[idx + 1])
    c = int(input_data[idx + 2])
    
    new_dp0 = a + max(dp1, dp2)
    new_dp1 = b + max(dp0, dp2)
    new_dp2 = c + max(dp0, dp1)
    
    dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2
    idx += 3

print(max(dp0, dp1, dp2))
