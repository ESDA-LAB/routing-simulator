import heapq
from typing import List, Tuple

class ShortestPathParams:
    def __init__(self, start: Tuple[int, int], destination: Tuple[int, int], obstacles: List[Tuple[int, int]], map_size: Tuple[int, int]):
        self.start = start
        self.destination = destination
        self.obstacles = obstacles
        self.map_size = map_size
       
    def FindRoute(self, params: ShortestPathParams) -> int:
        """
        Μέθοδος για την εύρεση της συντομότερης διαδρομής.

        :param params: Παράμετροι εισόδου (start, destination, obstacles, map size).
        :return: Η συντομότερη διαδρομή (απόσταση) ή -1 αν δεν υπάρχει διαδρομή.
        """
        pass

class DijkstraShortestPath(ShortestPathInterface):
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def FindRoute(self, params: ShortestPathParams) -> int:
        start = params.start
        end = params.destination
        obstacles = params.obstacles
        map_size = params.map_size

        # Δημιουργία πίνακα αποστάσεων και σύνολο επισκεμμένων κόμβων
        distance = {(i, j): float('inf') for i in range(map_size[0]) for j in range(map_size[1])}
        distance[start] = 0
        visited = set()
        
        # Χρήση ουράς προτεραιότητας για την αποθήκευση των κόμβων προς επεξεργασία
        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == end:
                return current_distance

            neighbors = [(current_node[0] + i, current_node[1] + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

            for neighbor in filter(lambda x: 0 <= x[0] < map_size[0] and 0 <= x[1] < map_size[1], neighbors):
                if neighbor in obstacles or neighbor in visited:
                    continue

                new_distance = current_distance + self.graph[neighbor[0]][neighbor[1]]

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        return -1  # Αν δεν υπάρχει διαδρομή
