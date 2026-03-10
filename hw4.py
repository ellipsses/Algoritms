from itertools import combinations

# Создаем граф
nodes = [1, 2, 3, 4, 5, 6, 7] # вершины
edges = [ # ребра
    (1, 2), (1, 3),
    (2, 3), (2, 4), (2, 5),
    (3, 6), (3, 7),
    (4, 7),
    (5, 7),
    (6, 7)
]


def is_independent_set(node_set): # проверка является ли множество независимым (когда между двумя вершинами нет ребра)
    for node1, node2 in combinations(node_set, 2): # комбинации вершин по 2 без повторений и порядок не важен
        if (node1, node2) in edges or (node2, node1) in edges:
            return False
    return True


def find_maximum_independent_set(): # находим макс независимое множество
    max_set = []
    for size in range(2, len(nodes) + 1): # перебираем кол-во вершин, не может быть меньше 2 независимых
        for combination in combinations(nodes, size): # составляем комбинации из вершин длины от 2 до 7
            if is_independent_set(combination):
                if len(combination) > len(max_set):
                    max_set = list(combination)
    return max_set


max_independent_set = find_maximum_independent_set()
print(f"Максимальное независимое множество: {max_independent_set}")
print(f"Размер: {len(max_independent_set)} узла(ов)")

print(f"\nПроверка на соседей:")
for node in max_independent_set:
    neighbors = []
    for edge in edges:
        if edge[0] == node:
            neighbors.append(edge[1])
        elif edge[1] == node:
            neighbors.append(edge[0])

    # Проверяем, есть ли среди соседей узлы из получившегося независимого множества
    neighbors_in_set = [n for n in neighbors if n in max_independent_set]

    if neighbors_in_set:
        print(f"Узел {node}: соседи {neighbors}, ошибка! Соединен с {neighbors_in_set}")
    else:
        print(f"Узел {node}: соседи {neighbors}, ок (не соединен с другими узлами множества)")


# оценка по времени: O(2^n × n²) - кол-во комбинаций умножаем на проверку каждой комбинации
# для n = 7, 2^n × n² составит 6,272, по времени примерно 0.001 сек
# но для n = 30, 2^n × n² составит уже 966,367,641,600, что по времени уже около 30 минут
