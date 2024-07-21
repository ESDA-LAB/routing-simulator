import heapq

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def FindRoute(self, start, end):
        # Έλεγχος εγκυρότητας των σημείων εκκίνησης και τερματισμού
        if not (0 <= start[0] < self.rows and 0 <= start[1] < self.cols) or \
           not (0 <= end[0] < self.rows and 0 <= end[1] < self.cols):
            return None

        # Ορισμός αρχικών τιμών
        distance = {(i, j): float('inf') for i in range(self.rows) for j in range(self.cols)}
        distance[start] = 0
        heap = [(0, start)]
        
        # Κύρια επανάληψη του αλγορίθμου Dijkstra
        while heap:
            current_distance, current_node = heapq.heappop(heap)

            # Ανάκτηση γειτονικών κελιών
            neighbors = [(current_node[0] + i, current_node[1] + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

            for neighbor in filter(lambda x: 0 <= x[0] < self.rows and 0 <= x[1] < self.cols, neighbors):
                new_distance = distance[current_node] + self.graph[neighbor[0]][neighbor[1]]

                # Εάν βρεθεί μια καλύτερη διαδρομή, ενημερώνουμε την απόσταση
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        # Επιστροφή της συντομότερης διαδρομής προς τον στόχο
        return distance[end]

# Παράδειγμα ενός πίνακα 16x16
graph_16x16 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    # Προσθέστε τις υπόλοιπες γραμμές του πίνακα με τις αντίστοιχες τιμές
]

# Δημιουργία αντικειμένου Dijkstra με τον πίνακα 16x16
dijkstra = Dijkstra(graph_16x16)

# Κλήση της μεθόδου FindRoute για την αναζήτηση συντομότερης διαδρομής
start_point = (0, 0)
end_point = (15, 15)
shortest_distance = dijkstra.FindRoute(start_point, end_point)

print(f"The shortest distance from {start_point} to {end_point} is: {shortest_distance}")
