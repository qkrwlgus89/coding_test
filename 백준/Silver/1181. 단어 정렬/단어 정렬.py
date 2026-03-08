n = int(input())

words = []

for i in range(n):
    word = input()
    words.append(word)

words = list(set(words))   # 중복 제거

words.sort(key=lambda x: (len(x), x))  # 길이 → 사전순 정렬

for w in words:
    print(w)