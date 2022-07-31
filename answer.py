import math

H,W = map(int,input().split())
oseroban = list(map(int,input().split()))
#oseroban = [list(int,input().split()) for _ in range(H)]
N = int(input())
n = math.ceil(math.log2(H*W))
num_list = [0]*n
num = []

N_2 = list(format(N,'b').zfill(n))

for i in range(H*W):
  if oseroban[i] == 0:
    w = list(format(i,'b').zfill(n))
    for j in range(n):
      if w[j] == '1':
        num_list[j] += 1
for k in range(n):
  if num_list[k] % 2 == 1:
    num.append("1")
  else:
    num.append("0")
num_s = "".join(num)
num_s.lstrip('0')
num_i = int(num_s,2)
print(num_i)

ans = []
for l in range(n):
  if num[l] == N_2[l]:
    ans.append("0")
  else:
    ans.append("1")

ans_s = "".join(ans)
ans_s.lstrip('0')
ans_i = int(ans_s,2)
print(ans_i+1)

if oseroban[ans_i] == 0:
  oseroban[ans_i] = 1
else:
  oseroban[ans_i] = 0

num_list = [0]*n
num = []

for i in range(H*W):
  if oseroban[i] == 0:
    w = list(format(i,'b').zfill(n))
    for j in range(n):
      if w[j] == '1':
        num_list[j] += 1
for k in range(n):
  if num_list[k] % 2 == 1:
    num.append("1")
  else:
    num.append("0")
num_s = "".join(num)
num_s.lstrip('0')
num_i = int(num_s,2)
print(num_i)