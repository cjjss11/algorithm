N = int(input())
people = []
for _ in range(N):
    w,h = map(int,input().split())
    people.append([w,h])
for i in range(N):
    cnt = 0
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    print(cnt+1,end=' ')