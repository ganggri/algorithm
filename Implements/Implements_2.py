# 왕실의 나이트
# 8*8의 체스판 위에 나이트가 움직일 수 있는 경우의 수 구하기
# 문제접근 : 그냥 8가지의 경우의수 순회하며 구하기..?
# 알파벳 to num은 dict type으로 치환
# 알파벳 to num을 아스키로 치환 후 할 수 있음
# y = int(ord(all[1])) - int(ord('a')) + 1 이런식으로

all = input()
x = all[0]
y = int(all[1])

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [-1,1,-1,1,2,-2,2,-2]
d = {"a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8}

x = d[x]
count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue
    count += 1
print(count)