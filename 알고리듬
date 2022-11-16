# 11047
N, K = map(int, input().split())
coin_list = []

for i in range(N):
  coin_list.append(int(input()))
coin_list = list(map(int, coin_list))

count = 0
for j in reversed(range(N)):
  if K == 0:
    break
  if coin_list[j] < K:
    count += K // coin_list[j]
    K %= coin_list[j]

print(count)
