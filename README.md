# 🗺️ Dijkstra's Shortest Path (Karachi Route Finder)

An implementation of **Dijkstra's Algorithm** to find the shortest route
between two locations in a city, using a weighted graph of Karachi areas
and the distances (in km) between them.

## 📋 Overview

1. The city is modeled as a **weighted graph** — each node is an area (e.g. `North Nazimabad`, `Saddar`, `Clifton`), and each edge weight is the distance (km) between two connected areas
2. `dijkstra(graph, start, end)` finds the shortest path and total distance between `start` and `end` using a **min-heap priority queue** (`heapq`)
3. The algorithm tracks the shortest known distance to every node and the previous node on that shortest path, reconstructing the full route once the destination is reached

## 🧠 How It Works

- `distances` — dictionary tracking the shortest known distance from `start` to every node (initialized to infinity, except `start` = 0)
- `previous_nodes` — tracks which node led to the shortest distance for each node, used to rebuild the path at the end
- `priority_queue` — a min-heap of `(distance, node)` pairs, always processing the closest unvisited node next
- Once `end` is popped from the queue, the path is reconstructed by walking backward through `previous_nodes`

## 🗺️ The Graph (Karachi Areas)

| From              | Connects To                                      |
| ------------------ | -------------------------------------------------- |
| North Nazimabad     | Saddar (4), Bahadurabad (9), DHA 6 (7)             |
| Saddar              | North Nazimabad (4), Bahadurabad (5), DHA 6 (10)   |
| Bahadurabad         | North Nazimabad (9), Saddar (5), Sea View (12)     |
| DHA 6                | North Nazimabad (7), Saddar (10), Clifton (6)      |
| Clifton              | DHA 6 (6), Sea View (9), Boat Basin (5)            |
| Boat Basin           | Clifton (5), Tariq Road (3)                        |
| Sea View             | Clifton (9), Tariq Road (7), Bahadurabad (12)       |
| Tariq Road           | Sea View (7), Boat Basin (3), Gulshan Iqbal (4)    |
| Gulshan Iqbal        | Tariq Road (4)                                     |

*(Numbers in parentheses are distances in km.)*

## ▶️ Running It

```bash
python3 Shortest_Path_Dijkstra.py
```

**Output:**

```
Algorithm Use: Dijkstra's Algorithm
Shortest Path: ['North Nazimabad', 'DHA 6', 'Clifton', 'Boat Basin', 'Tariq Road', 'Gulshan Iqbal']
Total Distance: 25 km
```

## 🛠️ Tech Stack

- **Python 3**
- `heapq` — standard library min-heap used as the priority queue

## 🚀 Possible Extensions

- Handle the case where `start` or `end` doesn't exist in the graph, or no path exists (currently returns `None` silently if `end` is never reached)
- Take `start`/`end` as command-line or user input instead of hardcoding them
- Visualize the graph and highlight the shortest path using `networkx` + `matplotlib`
- Support real-world map data (e.g. via OpenStreetMap) instead of manually defined distances
