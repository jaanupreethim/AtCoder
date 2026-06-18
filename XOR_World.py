A, B = map(int, input().split())

def get_xor_to_N(N):
    if N < 0:
        return 0
    rem = N % 4
    if rem == 0:
        return N
    elif rem == 1:
        return 1
    elif rem == 2:
        return N + 1
    else:
        return 0

result = get_xor_to_N(B) ^ get_xor_to_N(A - 1)
print(result)
