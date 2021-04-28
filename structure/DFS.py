# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!


#1. 시작노드(루트노드)부터 탐색
# 2. 현재 방문한 노드를 vistedㅇ에 추가
# 3. 현재 방문한 노드오 ㅏ인접한 노드 중 방문하지 않은 노드에 방문

def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for node in adjacent_graph[cur_node] :
        if node not in visited_array :
            dfs_recursion(adjacent_graph, cur_node, visited_array)
    return

""" dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
 """


# 1. 루트노드를 스택에 넣는다
# 2. 현재 스택의 노드를 빼서 visteid에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가
# 4. 반복
# 5. 스택이 비면 탐색을 종료
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []

    while stack:
        cur = stack.pop()
        visited.append(cur)
        for node in adjacent_graph[cur]:
            if node not in visited :
                stack.append(node)
    return visited


print(dfs_stack(graph, 1)) 