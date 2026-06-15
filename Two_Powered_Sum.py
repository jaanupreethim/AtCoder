import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    P = int(input_data[1])
    
    # Precompute combinations (nCr) modulo P
    C = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % P
            
    # Precompute Stirling numbers of the second kind modulo P
    S = [[0] * (N + 1) for _ in range(N + 1)]
    S[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            S[i][j] = (j * S[i-1][j] + S[i-1][j-1]) % P
            
    # Compute T(k, j) = \sum_{c=1}^k (-1)^{c-1} S(k, c) 2^(j*c)
    T = [[0] * (N + 1) for _ in range(N + 1)]
    for j in range(N + 1):
        base = pow(2, j, P)
        pow_base = [1] * (N + 1)
        for c in range(1, N + 1):
            pow_base[c] = (pow_base[c-1] * base) % P
            
        for k in range(1, N - j + 1):
            val = 0
            for c in range(1, k + 1):
                term = (S[k][c] * pow_base[c]) % P
                if c % 2 == 0:
                    val = (val - term) % P
                else:
                    val = (val + term) % P
            T[k][j] = val

    # DP to find the number of completely non-zero valid subgraphs of size n
    dag = [0] * (N + 1)
    dag[0] = 1
    for n in range(1, N + 1):
        val = 0
        for j in range(n):
            val = (val + C[n][j] * T[n-j][j] % P * dag[j]) % P
        dag[n] = val
        
    # Sum up choices by accounting for elements that can remain 0
    ans = 0
    for m in range(N + 1):
        ans = (ans + C[N][m] * dag[m]) % P
        
    print(ans)

if __name__ == '__main__':
    solve()
