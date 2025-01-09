from typing import List, Tuple
from shortest_path_interface import ShortestPathInterface
import heapq

class DijkstraShortestPath(ShortestPathInterface):
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def FindRoute(self, start: Tuple[int, int], end: Tuple[int, int], obstacles: List[Tuple[int, int]], 
                  map_size: Tuple[int, int]) -> int:
        distance = [[float('inf')] * self.cols for _ in range(self.rows)]
        distance[start[0]][start[1]] = 0
        pq = [(0, start)]  # Min-Heap με βάση την απόσταση

        while pq:
            curr_distance, (x, y) = heapq.heappop(pq)

            if (x, y) == end:
                return curr_distance

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.graph[nx][ny] != float('inf'):
                    new_distance = curr_distance + self.graph[nx][ny]
                    if new_distance < distance[nx][ny]:
                        distance[nx][ny] = new_distance
                        heapq.heappush(pq, (new_distance, (nx, ny)))

        return -1  # Αν δεν βρεθεί διαδρομή

