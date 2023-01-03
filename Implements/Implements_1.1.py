import time
n = int(input())
move = list(map(str,input().split()))
start = time.time()

    #동R,서L,남D,북U
    # 1.0 버전보다 간결하게 문자열 리스트를 추가하여 구현하였다.
x = 1
y = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direct = ["R","L","D","U"]

for m in move:
    for i in range(len(direct)):
        if direct[i] == m:                          # movement match
            nx = x + dx[i]
            ny = y + dy[i]
    if ny > n or ny < 1 or nx > n or nx < 1:        # boundary check
        continue
    x, y = nx, ny


print(f"{y} {x}")

end = time.time()
print(f"{end - start:.2f} sec")