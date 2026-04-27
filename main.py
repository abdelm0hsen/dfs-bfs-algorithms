from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.adjacency = defaultdict(list)

    def add_edge(self, source: str, target: str) -> None:
        self.adjacency[source].append(target)
        self.adjacency[target].append(source)

    def bfs(self, start: str):
        visited = set([start])
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start: str):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            order.append(node)

            for neighbor in reversed(self.adjacency[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
        return order


def build_sample_graph() -> Graph:
    graph = Graph()
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("E", "F"),
        ("D", "G"),
    ]
    for source, target in edges:
        graph.add_edge(source, target)
    return graph


def main() -> None:
    graph = build_sample_graph()
    start_node = input("Start node (default A): ").strip() or "A"

    if start_node not in graph.adjacency:
        print(f"Node '{start_node}' does not exist in the graph.")
        return

    bfs_order = graph.bfs(start_node)
    dfs_order = graph.dfs(start_node)

    print("\nGraph Traversal Results")
    print("=" * 24)
    print(f"BFS order: {' -> '.join(bfs_order)}")
    print(f"DFS order: {' -> '.join(dfs_order)}")


if __name__ == "__main__":
    main()
