import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return path[::-1], distances[end]

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

graph = {
    "North Nazimabad": {"Saddar": 4, "Bahadurabad": 9, "DHA 6": 7},
    "Saddar": {"North Nazimabad": 4, "Bahadurabad": 5, "DHA 6": 10},
    "Bahadurabad": {"North Nazimabad": 9, "Saddar": 5, "Sea View": 12},
    "DHA 6": {"North Nazimabad": 7, "Saddar": 10, "Clifton": 6},
    "Clifton": {"DHA 6": 6, "Sea View": 9, "Boat Basin": 5},
    "Boat Basin": {"Clifton": 5, "Tariq Road": 3},
    "Sea View": {"Clifton": 9, "Tariq Road": 7, "Bahadurabad": 12},
    "Tariq Road": {"Sea View": 7, "Boat Basin": 3, "Gulshan Iqbal": 4},
    "Gulshan Iqbal": {"Tariq Road": 4}
}
path, cost = dijkstra(graph, 'North Nazimabad', 'Gulshan Iqbal')
print("Algorithm Use: Dijkstra’s Algorithm")
print(f"Shortest Path: {path}")
print(f"Total Distance: {cost} km")








