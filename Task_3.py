import heapq

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edge("178", "177", weight=1)
G.add_edge("178", "176", weight=4)
G.add_edge("176", "120", weight=3)
G.add_edge("176", "175", weight=7)
G.add_edge("177", "115", weight=2)
G.add_edge("177", "110", weight=8)
G.add_edge("110", "97", weight=15)
G.add_edge("110", "96", weight=14)
G.add_edge("115", "80", weight=13)
G.add_edge("115", "75", weight=27)
G.add_edge("120", "40", weight=22)
G.add_edge("120", "50", weight=38)
G.add_edge("178", "175", weight=10)
G.add_edge("178", "50", weight=24)
G.add_edge("178", "80", weight=13)
G.add_edge("75", "97", weight=7)
G.add_edge("96", "97", weight=32)
G.add_edge("177", "175", weight=28)
G.add_edge("50", "40", weight=19)
G.add_edge("80", "178", weight=14)
#Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        print("priority_queue: ", priority_queue)
        print("shortest_paths:", shortest_paths)
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "178")
print(shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
