import time

# 문제접근 : 공포도가 1인 사람은 혼자서도 그룹을 떠날 수 있기 때문에 빼주어야 한다고 생각하고, 
# 나머지는 오름차순으로 정렬하여 바로 앞사람의 공포도 값에 맞게 묶음을 묶어
# 여행을 가고 공포도보다 남은 모험가의 수가 적은 경우 break한다.

n = int(input())
fear = list(map(int, input().split()))

start = time.time()
index = 0
group_num = 0
fear.sort()

while True:
    if (index >= len(fear)) or (fear[index] > (len(fear) - index)):
        break

    if fear[index] == 1:
        group_num += 1
        index += 1
        print("[1]")
        continue
    step = 1
    # 생각 중 1, 2, 3, 4 인 경우 1은 들어가고 2에서 3을 넣으면 또 하나를 더 더해야 한다. 그럼 4가 들어가면 집단이 생성되지 않는다.
    
    
print(group_num)


end = time.time()
print(f"{end - start:.2f} sec")