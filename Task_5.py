import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque
# from matplotlib import colors as mcolors

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def build_heap_tree(heap, index=0):
    #TODO Реалізація функції побудови дерева бінарної купи (Взяти з попереднього завдання)
    if index < len(heap):
        node = Node(heap[index])
        node.left = build_heap_tree(heap, index*2+1)
        node.right = build_heap_tree(heap, index*2+2)
        return node

def generate_color(step, total_steps):
    
    
    base_color = [135, 206, 250]  # світло-блакитний (skyblue) у форматі RGB
    darken_factor = step/(1.67 *total_steps)  # Наскільки темнішим має бути кожен наступний вузол
    new_color = [int(c * (1 - darken_factor)) for c in base_color]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'
    


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0
    while stack:
        # Вилучаємо вершину зі стеку
        root = stack.pop()
        if root not in visited and root is not None:
            print(root.val, end=' ')
            # Відвідуємо вершину
            visited.add(root)
            step+=1
            colors[root.id]=generate_color(step, total_steps)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed([root.left, root.right]))       
    return colors


def bfs_visualize(root, total_steps):
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([root])

    colors = {}
    step = 0

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        root=queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
           
        if root not in visited and root is not None:
            # Якщо не була відвідана, друкуємо її
            print(root.val, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(root)
            step+=1
            colors[root.id]=generate_color(step, total_steps)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set([root.left,root.right]) - visited)

    return colors


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_list)

    # Обрахунок кількості кроків (вузлів)
    total_steps = count_nodes(heap_tree_root)

    # DFS візуалізація
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    # BFS візуалізація
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)
