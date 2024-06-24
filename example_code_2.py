# Δημιουργία πίνακα 16x16 με κόστος 1 για κάθε κελί
graph_16x16 = [
    [1]*16 for _ in range(16)
]

# Ορισμός εμποδίων με άπειρο κόστος
graph_16x16[5][5] = graph_16x16[5][6] = graph_16x16[6][5] = graph_16x16[6][6] = float('inf')

# Δημιουργία παραμέτρων εισόδου
start_point = (0, 0)
end_point = (15, 15)
obstacle_list = [(5, 5), (5, 6), (6, 5), (6, 6)]  # Συντεταγμένες εμποδίων
map_dimensions = (16, 16)

params = ShortestPathParams(start=start_point, destination=end_point, obstacles=obstacle_list, map_size=map_dimensions)

# Δημιουργία αντικειμένου DijkstraShortestPath με τον πίνακα 16x16
dijkstra = DijkstraShortestPath(graph_16x16)

# Κλήση της μεθόδου FindRoute για την αναζήτηση συντομότερης διαδρομής
shortest_distance = dijkstra.FindRoute(params)
print(f"The shortest distance from {start_point} to {end_point} is: {shortest_distance}")
