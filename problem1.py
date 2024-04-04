# 그리디 알고리즘 사용

# 1. 입력받기
N = int(input()) 
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

# 2. 끝나는 시간 기준으로 오름차순 정렬
arr.sort(key=lambda x : [x[1], x[0]])

# 3. 첫번째 회의 선택
end_time = arr[0][1]
ans = 1

# 4. 끝나는 시간보다 먼저 시작하는 회의 제거 
for i in range(1, N):
    start_time = arr[i][0]
    if start_time < end_time:
        continue
    end_time = arr[i][1] # 5. 다음회의선택
    ans += 1

print(ans)