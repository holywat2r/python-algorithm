# bfs 메서드 구현
def bfs(x,y):
    #deque 라이브러리 사용
    queue = deque()
    queue.append((x,y)) # x,y로 이루어진 튜플 데이터를 담기
    # 큐가 반복될 때까지 반복하기

    while queue:
        x, y = queue.popleft()
        # 현 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n - 1][m - 1]

from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))



