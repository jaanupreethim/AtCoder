import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    MOD = 998244353
    out = []
    
    for _ in range(T):
        N = int(input_data[idx])
        A = int(input_data[idx+1])
        B = int(input_data[idx+2])
        C = int(input_data[idx+3])
        D = int(input_data[idx+4])
        idx += 5
        
        delta = abs(A * D - C * B)
        if delta == 0:
            g_AC = math.gcd(A, C)
            g_BD = math.gcd(B, D)
            sum_i = (N * (N + 1) // 2) % MOD
            total_sum = (g_AC * sum_i + g_BD * (N % MOD)) % MOD
            out.append(str(total_sum))
            continue
            
        divisors = []
        for d in range(1, int(math.sqrt(delta)) + 1):
            if delta % d == 0:
                divisors.append(d)
                if d * d != delta:
                    divisors.append(delta // d)
        divisors.sort(reverse=True)
        
        count_multiples = {}
        exact_count = {}
        
        for g in divisors:
            g_A = math.gcd(A, g)
            if B % g_A != 0:
                count_multiples[g] = 0
                continue
            
            mod_sub = g // g_A
            A_sub = (A // g_A) % mod_sub
            B_sub = ((-B) // g_A) % mod_sub
            
            try:
                inv = pow(A_sub, -1, mod_sub)
                i0 = (B_sub * inv) % mod_sub
                
                multiples = 0
                for k in range(g_A):
                    rem = i0 + k * mod_sub
                    if rem == 0:
                        rem = g
                    
                    if (C * rem + D) % g == 0 and rem <= N:
                        multiples += (N - rem) // g + 1
                        
                count_multiples[g] = multiples
            except ValueError:
                count_multiples[g] = 0
        
        total_sum = 0
        for g in divisors:
            cnt = count_multiples.get(g, 0)
            for multiple in divisors:
                if multiple > g and multiple % g == 0:
                    cnt -= exact_count.get(multiple, 0)
            
            exact_count[g] = cnt
            total_sum = (total_sum + (cnt % MOD) * g) % MOD
            
        out.append(str(total_sum))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
