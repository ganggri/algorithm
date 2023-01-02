import time
start = time.time()

# 공포도가 1인 사람은 혼자서도 그룹을 떠날 수 있기 때문에 빼주어야 한다고 생각하고, 
# 나머지는 

n = int(input())
fear = list(map(int,input().split()))



end = time.time()

print(f"{end - start:.2f} sec")