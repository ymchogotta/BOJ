input()
n = sorted(map(int, input().split()))

input()
m = list(map(int, input().split()))

for i in m:
    answer = 0
    first, last = 0, len(n) - 1
    while first <= last:
        mid = (first + last) // 2
        if n[mid] < i:
            first = mid + 1  # 여기서 +1을 안하면 시간초과 뜨던데 이유가 궁금합니다
        elif n[mid] > i:
            last = mid - 1   # 여기도 -1을 제거하면
        else:
            answer = 1
            break
    print(answer)
