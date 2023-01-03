import time
# 기본적인 동서남북 움직임 구현 문제
# 그냥 구현하니 지저분하고 다른 자료구조를 배우면 더 깔끔하게 나타낼 수 있을 것 같다.
n = int(input())
move = list(map(str,input().split()))
start = time.time()

    #동R,서L,남D,북U
x = 1
y = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for m in move:
    if m == "R":
        if x == n:
            continue
        x += dx[0]
    elif m == "L":
        if x == 1:
            continue
        x += dx[1]
    elif m == "D":
        if y == n:
            continue
        y += dy[2]
    elif m =="U":
        if y == 1:
            continue
        y += dy[3]
print(f"{y} {x}")

end = time.time()
print(f"{end - start:.2f} sec")