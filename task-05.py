import uuid
import networkx as nx
import matplotlib.pyplot as plt
import time


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, visited=None):
    """Візуалізація дерева з оновленими кольорами."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

    if visited:
        print(f"Обхід: {', '.join(map(str, visited))}")


def rgb_color(step, total_steps):
    """Генерація кольору на основі порядку відвідування (від темного до світлого)."""
    intensity = int(255 * (step / total_steps))
    return f"#{intensity:02x}{(255 - intensity):02x}{intensity:02x}"  # RGB відтінки


def bfs_visualized(tree_root):
    """Обхід у ширину з візуалізацією."""
    queue = [tree_root]
    visited = []
    total_nodes = 0

    # Підрахунок загальної кількості вузлів
    temp_queue = [tree_root]
    while temp_queue:
        node = temp_queue.pop(0)
        total_nodes += 1
        if node.left:
            temp_queue.append(node.left)
        if node.right:
            temp_queue.append(node.right)

    step = 0
    while queue:
        node = queue.pop(0)
        visited.append(node.val)
        node.color = rgb_color(step, total_nodes)  # Оновлення кольору вузла
        draw_tree(tree_root, visited)
        time.sleep(1)  # Затримка для демонстрації кроку
        step += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs_visualized(tree_root):
    """Обхід у глибину з візуалізацією."""
    stack = [tree_root]
    visited = []
    total_nodes = 0

    # Підрахунок загальної кількості вузлів
    temp_stack = [tree_root]
    while temp_stack:
        node = temp_stack.pop()
        total_nodes += 1
        if node.right:
            temp_stack.append(node.right)
        if node.left:
            temp_stack.append(node.left)

    step = 0
    while stack:
        node = stack.pop()
        visited.append(node.val)
        node.color = rgb_color(step, total_nodes)  # Оновлення кольору вузла
        draw_tree(tree_root, visited)
        time.sleep(1)  # Затримка для демонстрації кроку
        step += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("Обхід у ширину:")
bfs_visualized(root)

# Скидання кольорів
root.color = "skyblue"
root.left.color = "skyblue"
root.left.left.color = "skyblue"
root.left.right.color = "skyblue"
root.right.color = "skyblue"
root.right.left.color = "skyblue"

print("Обхід у глибину:")
dfs_visualized(root)