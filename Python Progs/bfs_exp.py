from collections import deque


def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:
        node = queue.popleft()  # Get the first node in the queue

        if node not in visited:
            print(node, end=" ")  # Visit the node
            visited.add(node)

            # Add all unvisited neighbors to the queue
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


# Example graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

bfs(graph, 3)  # Starting BFS from node 1
