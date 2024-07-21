from typing import List, Tuple

class ShortestPathInterface:
    def FindRoute(self, start: Tuple[int, int], end: Tuple[int, int], obstacles: List[Tuple[int, int]],
                  map_size: Tuple[int, int]) -> int:
        """
        Μέθοδος για την εύρεση της συντομότερης διαδρομής.

        :param start: Το αρχικό σημείο (συντεταγμένες).
        :param end: Το σημείο προορισμού (συντεταγμένες).
        :param obstacles: Λίστα με τις συντεταγμένες των εμποδίων.
        :param map_size: Το μέγεθος του χάρτη (συντεταγμένες).
        :return: Η συντομότερη διαδρομή (απόσταση).
        """
        pass

class DijkstraShortestPath(ShortestPathInterface):
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def FindRoute(self, start: Tuple[int, int], end: Tuple[int, int], obstacles: List[Tuple[int, int]],
                  map_size: Tuple[int, int]) -> int:
        distance = {(i, j): float('inf') for i in range(map_size[0]) for j in range(map_size[1])}
        distance[start] = 0
        visited = set()
        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            neighbors = [(current_node[0] + i, current_node[1] + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

            for neighbor in filter(lambda x: 0 <= x[0] < map_size[0] and 0 <= x[1] < map_size[1], neighbors):
                if neighbor in obstacles:
                    continue

                new_distance = distance[current_node] + self.graph[neighbor[0]][neighbor[1]]

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        return distance[end]

# Παράδειγμα χρήσης
graph_16x16 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    # Προσθέστε τις υπόλοιπες γραμμές του πίνακα με τις αντίστοιχες τιμές
]

dijkstra = DijkstraShortestPath(graph_16x16)

start_point = (0, 0)
end_point = (15, 15)
obstacle_list = [(5, 5), (5, 6), (6, 5), (6, 6)]
map_dimensions = (16, 16)

shortest_distance = dijkstra.FindRoute(start_point, end_point, obstacle_list, map_dimensions)
print(f"The shortest distance from {start_point} to {end_point} is: {shortest_distance}")
