import matplotlib.pyplot as plt
import networkx as nx
from IPython.display import clear_output
import time
from collections import defaultdict, deque

def visualize_kahn(graph):
    G = nx.DiGraph(graph)
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []
    step = 0

    pos = nx.spring_layout(G)

    while queue:
        clear_output(wait=True)
        current = queue.popleft()
        result.append(current)
        in_degree_copy = in_degree.copy()

        plt.figure(figsize=(8, 6))
        color_map = []
        for node in G.nodes:
            if node in result:
                color_map.append('lightgreen')
            elif node in queue:
                color_map.append('lightblue')
            else:
                color_map.append('lightgray')

        nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=800, arrows=True)
        plt.title(f"Шаг {step}: обработка вершины {current}")
        plt.show()
        time.sleep(1)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

        step += 1
