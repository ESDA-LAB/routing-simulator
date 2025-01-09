from typing import List, Tuple
from shortest_path_interface import ShortestPathInterface

class BellmanFordShortestPath(ShortestPathInterface):
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def FindRoute(self, start: Tuple[int, int], end: Tuple[int, int], obstacles: List[Tuple[int, int]], 
                  map_size: Tuple[int, int]) -> int:
        distance = {(i, j): float('inf') for i in range(map_size[0]) for j in range(map_size[1])}
        distance[start] = 0

        edges = []
        for i in range(map_size[0]):
            for j in range(map_size[1]):
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < map_size[0] and 0 <= nj < map_size[1]:
                        edges.append(((i, j), (ni, nj), self.graph[ni][nj]))

        for _ in range(map_size[0] * map_size[1] - 1):
            for (u, v, weight) in edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        for (u, v, weight) in edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                return -1

        return distance[end] if distance[end] != float('inf') else -1
