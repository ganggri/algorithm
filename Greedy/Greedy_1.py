import time

n, k = map(int,(input().split()))
start = time.time()

count = 0

while n >= k:                    # n이 k보다 작다면 나눌 수 없기에 탈출
    check = (n // k) * k
    count += n - check
    n = check / k
    count += 1

count += n - 1
print(int(count))

end = time.time()
print(f"{end - start:.2f} sec")
