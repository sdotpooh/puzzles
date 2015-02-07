__author__ = "Sean R. Vinas"
__date__ = "29 December 2014"
__doc__ = """ Find the number of steps in the shortest way from the entrance
on the first floor to the exit on the last floor, including entrance and exit.
Moving between levels is one step."""


from sys import argv
from queue import Queue


def node_floor_row_column(size, puzzle):
    """ Convert the string puzzle into a dictionary detailing the significant info of the puzzle.

    :param size: int detailing the size of each row, column and floor related to the puzzle
    :param puzzle: string of length == size*size*size
    :return: a dict containing int keys and tuple values. Each tuple value field == (legend, floor, row, column)
      legend = a char consisting of either: ' ' or 's' or 'f' or 'o'
      floor = int > -1
      row = int > -1
      column > -1
    """
    wall_char = '*'
    start_char = 's'
    stop_char = 'f'
    node_positions = dict()
    n = 0
    nodes = 0
    for floor in range(size):
        for row in range(size):
            for column in range(size):
                if puzzle[n] != wall_char:
                    if floor == 0 and ((row == 0 or row == size-1) or (column == 0 or column == size-1)):
                        node_positions[(start_char, floor, row, column)] = nodes
                    elif floor == size-1 and ((row == 0 or row == size-1) or (column == 0 or column == size-1)):
                        node_positions[(stop_char, floor, row, column)] = nodes
                    else:
                        node_positions[(puzzle[n], floor, row, column)] = nodes
                    nodes += 1
                n += 1
    return node_positions


def make_graph(nodes):
    """ Constructs a graph dictionary of all the nodes.

    :param nodes: dictionary value == tuple, keys == int.
      Each tuple value field == (legend, floor, row, column)
      legend = a char consisting of either: ' ' or 's' or 'f' or 'o'
      floor = int > -1
      row = int > -1
      column > -1
    :return: start, stop, graph
    start == int > -1
    stop == int > -1
    graph ==  a dictionary where keys == int > -1, values == list of ints > -1
    """
    graph = dict()
    hole_char = 'o'
    start_char = 's'
    stop_char = 'f'
    step_char = ' '
    legend = step_char + hole_char + start_char + stop_char
    start = 0
    stop = 0
    for info, node in nodes.items():
        desc, floor, row, col = info
        # find dict keys on the same floor, row but adjacent columns
        keys = list(filter(lambda x: x[0] in legend and x[1] == floor and x[2] == row and x[3] in [col+1, col-1],
                           nodes))
        # find dict keys on the same floor, column but adjacent rows
        keys.extend(list(filter(lambda x: x[0] in legend and x[1] == floor and x[2] in [row+1, row-1] and x[3] == col,
                                nodes)))
        if desc == hole_char:
            # find dict key of a node 1 floor below
            info_below = list(filter(lambda x: x[0] in legend and x[1] == floor-1 and x[2] == row and x[3] == col,
                                     nodes))
            keys.extend(info_below)
            # Need to connect above node also!!! Find dict key of node above floor and map
            node_below = nodes[info_below[0]]
            if node_below in graph:
                graph[node_below].append(node)
            else:
                graph[node_below] = [node]
        # Make the graph connections
        w = [nodes[k] for k in keys]
        if len(w) > 0:
            if node not in graph:
                graph[node] = w
            else:
                graph[node].extend(w)

        if desc == start_char:
            start = node
        elif desc == stop_char:
            stop = node
    nodes.clear()
    return start, stop, graph


def breadth_first_search(start, stop, graph):
    """ Breadth first search of graph to find distance between start and stop node

    :param start: Node
    :param stop: Node
    :param graph: dictionary of nodes
    :return: distance == int > -1. 0 == none exists
    """
    visited = dict()
    distances = dict()
    queue = Queue()
    queue.put(start)
    distances[start] = 1
    while not queue.empty():
        current_node = queue.get()
        visited[current_node] = 1
        distance = distances[current_node]
        for node in graph[current_node]:
            if node not in visited:
                queue.put(node)
                visited[node] = 1
                distances[node] = distance + 1
                if node == stop:
                    return distance + 1
    return 0


def main():
    with open('input.txt', 'r') as f:
        lines = (lines.rstrip('\n') for lines in f)
        for line in lines:
            size, puzzle = line.split(';')
            nodes = node_floor_row_column(int(size), puzzle)
            start, stop, graph = make_graph(nodes)
            print(breadth_first_search(start, stop, graph))
            graph.clear()


if __name__ == "__main__":
    main()
