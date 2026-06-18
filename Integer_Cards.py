import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    
    A = [int(x) for x in data[2:2+N]]
    
    idx = 2 + N
    operations = []
    for _ in range(M):
        b = int(data[idx])
        c = int(data[idx+1])
        operations.append((c, b))
        idx += 2
        
    operations.sort(key=lambda x: x[0], reverse=True)
    A.sort()
    
    card_ptr = 0
    for c, b in operations:
        for _ in range(b):
            if card_ptr < N and A[card_ptr] < c:
                A[card_ptr] = c
                card_ptr += 1
            else:
                break
        if card_ptr >= N or (card_ptr < N and A[card_ptr] >= c):
            if card_ptr >= N:
                break
                
    print(sum(A))

if __name__ == '__main__':
    solve()
