import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    p = [float(x) for x in data[1:]]
    
    dp = [0.0] * (N + 1)
    dp[0] = 1.0
    
    for i in range(N):
        p_head = p[i]
        p_tail = 1.0 - p_head
        
        for j in range(i + 1, -1, -1):
            head_contrib = dp[j - 1] * p_head if j > 0 else 0.0
            tail_contrib = dp[j] * p_tail
            dp[j] = head_contrib + tail_contrib
            
    ans = sum(dp[j] for j in range((N // 2) + 1, N + 1))
    print(f"{ans:.10f}")

if __name__ == '__main__':
    solve()
