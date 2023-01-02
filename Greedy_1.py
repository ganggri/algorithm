import time
start = time.time()

a, b = map(int,(input().split()))
count = 0

while a != 1:           # a의 값이 1이 된다면 종료
    if(a % b == 0):     # a를 b로 나눈 나머지가 0이면 b로 나눈 후 a값 할당 후 카운트 +1
        a = a // b
        count += 1
    else:
        a = a - 1       # 나머지가 0이 아닌 경우 a의 값을 -1을 한 후 카운트 +1
        count += 1
print(count)

end = time.time()
print(f"{end - start:.5f} sec")