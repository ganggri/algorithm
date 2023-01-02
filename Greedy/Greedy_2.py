# 입력이 주어지는대로 곱하기나 더하기 연산자를 넣어 최대한 큰 수로 만들기 연산순서는 무조건 좌에서 우로 간다.
# 문제 접근 : 0또는 1을 곱하지만 않는다면 더하기 연산자는 곱하기보다 커질 수 없다.
#           그리고 큰수를 먼저 곱해주고 나머지 1이나 0을 더해준다면 가장 큰 수가 될 수 있을것이다.
import time, sys

nums = list(map(int,sys.stdin.readline().rstrip()))
start = time.time()
    # 변경내용 : 1이나 0이 없을 경우 정렬 안함.

# 문제에서 두가지의 숫자를 각각 계산하기 때문에 여기서 앞 뒤의 문자를 0이나 1이 아니면 전부 순서대로 곱한 후
# 나머지 숫자는 더한다. 하지만 내림차순으로 정렬하였기에 0이나 1을 매번 체크하지 않고 리스트를 분할한다.
total = 1

if 1 in nums or 0 in nums:
    nums = sorted(nums,reverse=True)            # 입련된 정수를 내림차순 정렬
    location = nums.index(1) if 1 in nums else nums.index(0)
    over = nums[:location]
    under = nums[location:]
    for i in range(0,len(over)):
        total *= over[i]
    for i in under:
        total += i
else:
    for i in range(0,len(nums)):
        total *= nums[i]
print(total)

end = time.time()
print(f"{end - start:.2f} sec")