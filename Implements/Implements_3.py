# 문자열 재정렬
# 숫자와 문자열을 무작위로 공백없이 입력하면 문자열은 오름차순, 숫자는 합하여 뒤에 붙는다.
# 문제해결 : 먼저 들어온 문자열을 전부 오름차순으로 정렬해주면 숫자가 먼저 정렬되어 앞으로 가기에
#          가장 먼저 숫자가 아닌 문자가 나올 때까지 인덱스를 체크하고 첫 문자가 나온다면
#          문자열과 숫자를 분리하여 숫자는 합한 후 마지막에 전부 붙여서 출력하면 해결된다.
all = input()
all = sorted(all)

for check in range(len(all)):
    if not (all[check] <= '9' and all[check] >= '0'):
        break
nums = all[:check]
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(''.join(all[check:])+str(sum(nums)))