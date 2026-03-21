import sys
input = sys.stdin.readline

# 최대 N이 100이니까 미리 계산
dp = [0] * 101

dp[1] = dp[2] = dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N])