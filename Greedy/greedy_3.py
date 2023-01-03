import time

# 문제접근 : 오름차순으로 정렬하여 바로 공포도를 기준으로 오름차순으로 진행하며
#          모험을 가고 모험가의 인원이 마지막 인원의 공포도보다 같거나 높은경우 그룹을 결성

n = int(input())
ppl_fear = list(map(int, input().split()))

start = time.time()

group_num = 0
ppl_fear.sort()
count = 1

for fear in ppl_fear:
    if count >= fear:           # 현재 속한 인원이 마지막 인원의 공포도보다 높을 시
        group_num += 1          # 그룹에 추가 및 현재 속한 인원 초기화
        count = 1
        continue
    count += 1

print(group_num)

end = time.time()
print(f"{end - start:.2f} sec")
