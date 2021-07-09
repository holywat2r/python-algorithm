# N개의 데이터를 가진 배열 A,B 를 K번 만큼 바꾸어 A배열의 합의 최대로 만들기
# 가장작은 A배열과 B의 가장 큰 값을 바꾼다?

# 1. 배열 a와 b 값을 받아들인다
# 2. n,k값을 받아들인다
# 3. 정렬 후 맨 앞꺼 변경

n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort() # b.sort(reversed = True)
         # for i in range(k):
         #      if a[i] < b[i]:
         #          a[i], b[i] = b[i], a[i]
         #      else:
         #          break
         # print(sum(a))

y = -1

for i in range(k):
    if a[i] < b[y]:
        a[i],b[y] = b[y],a[i]
        y -= 1
    else:
        y-= 1

print(sum(a)) 
