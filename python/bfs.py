# bfs = 너비 우선 탐색
# 큐 자료구조를 이용
# 1. 시작 노드를 큐에 삽입하고 방문 처리를 한다
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드 인접 노드 중에서 방문하지 않는 노드를
#    모두 큐에 넣고 방문 처리
# 3. 더이상 2번의 과정을 수행할 수 없을 때 까지 반복

from collections import deque

# bfs 메서드를 정의 
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리 
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 원소 하나 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ') 

        for i in graph[v]:
            #아직 방문 하지 않은 인접 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현하는 2차원 리스트
graph = [
    [],
    [2,3,8], #각각 노드와 연결된 인접한 노드에 대한 설명
    [1,7], # 2번 노드가 연결
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드 방문 정보 표현 리스트
visited = [False] * 9
# 정의된 bfs함수 호출
bfs(graph,1,visited)