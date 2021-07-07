# 깊이 우선 탐색 (Depth-First-Search)
# 스택자료구조 또는 재귀 함수를 이용
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
# 2. 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문
#    처리. 방문하지 않은 인접 노드가 있다면 스택에서 최상단 노드를 꺼낸다
# 3. 2번이 수행 안될 때 까지 반복

# dfs 메서드를 정의
def dfs(graph,v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')

#현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 인접 노드 표현한 2차원 리스트
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph,2,visited)