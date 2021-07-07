# dfs 혹은 bfs를 이용하여 문제 풀기
# 연결 요소를 통해 문제 풀이
# 특정 노드에서 방문 할 수 있는 모든 노드들을 방문 처리

# 특정한 지점의 주변 상 하 좌 우를 살펴본 뒤에 주변 지점 중에서 값이 0 이면서
# 아직 방문하지 않은 지점이 있다면 해당 지점을 방문

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 넘어가는 경우 즉시 종료를 위한 if문
    if x <= -1 or x >= row or y <= -1 or y >= column:
        return False
    if graph[x][y] == 0:
        graph[x][y] == 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)



# 가로와 세로를 입력 받음
row, column = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(row):
        graph.append(list(map(int,input())))

result = 0
for i in range(row):
    for j in range(column):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)