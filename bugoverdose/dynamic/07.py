# 01타일
# https://www.acmicpc.net/problem/1904
# 1 하나만으로 이루어진 타일 또는 0타일을 두 개 붙인 한 쌍의 00타일들만 사용 가능
# 예를 들어, N=1일 때 1만 만들 수 있고, N=2일 때는 00, 11을 만들 수 있다. (01, 10은 만들 수 없게 되었다.) 
# 또한 N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열을 만들 수 있다.

# 나의 정답


# =================================================================
# 시간초과
def permutation_count(a,b): # n_P_a // b!
    cur = 1
    for i in range(a+b,a,-1): # a+b_P_b # n!/(n-r)!
        cur *= i
    for i in range(b,0,-1): # 중복제거
        cur //= i
    return cur

answer = 0

N = int(input())

for n in range(0, N//2 + 1):
    answer += permutation_count(N - 2*n, n)

print(answer%15746)

# ex)
# 1,1,1,1,1,1,1,1,1,1 => 10! // 10! // (0)!
# 1,1,1,1,1,1,1,1,00 
# 1,1,1,1,1,1,00,00 
# 1,1,1,1,00,00,00 => 7! // 4! // (7-3)!
# 1,1,00,00,00,00
# 00,00,00,00,00

# =================================================================