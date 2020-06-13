n = int(input())
goods = []
for _ in range(n):
  s = input()
  goods.append(s)
goods = set(goods)
print(len(goods))
