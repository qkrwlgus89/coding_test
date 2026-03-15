k, n = map(int, input().split())
lenton = []

for _ in range(k):
    x = int(input())
    lenton.append(x)

# 이분 탐색
start, end = 1, max(lenton)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    # mid 길이로 잘랐을 때 몇 개 만들 수 있는지 계산
    for length in lenton:
        count += length // mid
    
    if count >= n:  # 충분히 만들 수 있다면 길이를 늘려본다
        result = mid
        start = mid + 1
    else:  # 부족하다면 길이를 줄인다
        end = mid - 1

print(result)