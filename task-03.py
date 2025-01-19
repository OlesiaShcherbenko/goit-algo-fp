import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        """Додає ребро між вершинами u та v з вагою weight."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Для неорієнтованого графа

    def dijkstra(self, start):
        """Алгоритм Дейкстри для пошуку найкоротших шляхів."""
        # Ініціалізація
        min_heap = []
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        heapq.heappush(min_heap, (0, start))  # (відстань, вершина)
        visited = set()

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            # Оновлення відстаней для сусідів
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        return distances