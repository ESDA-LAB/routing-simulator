from bellman_ford_shortest_path import BellmanFordShortestPath

# Δημιουργία πίνακα 16x16 με κόστος 1 για κάθε κελί
graph_16x16 = [
    [1]*16 for _ in range(16)
]

# Ορισμός εμποδίων με άπειρο κόστος
obstacle_positions = [(5, 5), (5, 6), (6, 5), (6, 6)]
for x, y in obstacle_positions:
    graph_16x16[x][y] = float('inf')

# Ορισμός παραμέτρων
start_point = (0, 0)
end_point = (15, 15)
map_dimensions = (16, 16)

# Δημιουργία αντικειμένου BellmanFordShortestPath με τον πίνακα 16x16
bellman_ford = BellmanFordShortestPath(graph_16x16)

# Κλήση της μεθόδου FindRoute για την αναζήτηση συντομότερης διαδρομής
shortest_distance = bellman_ford.FindRoute(start_point, end_point, obstacle_positions, map_dimensions)
print(f"The shortest distance from {start_point} to {end_point} is: {shortest_distance}")
