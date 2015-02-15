""" A Python Class
A simple undirected Python graph class.
"""
from queue import Queue


class Graph:

    def __init__(self):
        self.graph = dict()

    def __str__(self):
        """ Print the graph in a more readable format for terminal size."""
        line = ''
        for node in self.graph.keys():
            if self.graph[node]:
                line += str(node) + ' : {'
                last = len(self.graph[node]) - 1
                for i, edge in enumerate(self.graph[node]):
                    if i != last:
                        line += str(edge) + ', '
                    else:
                        line += str(edge)
                line += '}\n'
        return line

    def node(self, node):
        if node not in self.graph and node is not None:
            self.graph[node] = set()

    def add_edges(self, node_a, node_b):
        if node_a in self.graph and node_b in self.graph:
            self.graph[node_a].add(node_b)
            self.graph[node_b].add(node_a)

    def degree(self, node):
        if node in self.graph:
            # loops counted twice!
            if node in self.graph and node in self.graph[node]:
                return len(self.graph[node]) + 1
            else:
                return len(self.graph[node])

    def connected(self, node_a, node_b):
        if node_a in self.graph and node_b in self.graph:
            return node_a in self.graph[node_b]

    def neighbors(self, node):
        return self.graph[node] if node in self.graph else None

    def bron_kerbosch(self, current, prospective, processed):
        """ Undirected graph Bron-Kerbosch algorithm to find max cliques.
        Will not work for self-loops will cause max recursion depth.
        """
        if not any((prospective, processed)):
            yield sorted(current)
        for node in prospective:
            for clique in self.bron_kerbosch(
                    current.union({node}),
                    prospective.intersection(self.neighbors(node)),
                    processed.intersection(self.neighbors(node))):
                yield clique
            prospective.discard({node})
            processed.union({node})

    def bfs_distance(self, start, stop):
        """ Breadth first search of graph to find distance between
        start and stop node.
        """
        if start in self.graph and stop in self.graph:
            visited = set()
            distances = dict()
            queue = Queue()
            queue.put(start)
            distances[start] = 1
            while not queue.empty():
                current_node = queue.get()
                visited.add(current_node)
                distance = distances[current_node]
                for node in self.graph[current_node]:
                    if node not in visited:
                        queue.put(node)
                        visited.add(node)
                        distances[node] = distance + 1
                        if node == stop:
                            return distance + 1
        return 0


if __name__ == '__main__':
    g = Graph()
    g.node('a')
    g.node('b')
    g.node('c')
    g.node('d')
    g.node('e')
    g.node('f')
    g.node('g')
    g.add_edges('a', 'b')
    g.add_edges('a', 'c')
    g.add_edges('a', 'd')
    g.add_edges('b', 'c')
    g.add_edges('b', 'd')
    g.add_edges('c', 'd')
    g.add_edges('e', 'b')
    g.add_edges('e', 'd')
    g.add_edges('f', 'g')
    print(g)
    nodes = {node for node in g.graph.keys() if any(node)}
    # Bron-Kerbosch will produce repeats, to avoid retain data in set.
    # Tuple used to keep entries immutable.
    cliques = {tuple(clique) for clique in g.bron_kerbosch(set(), nodes,
                                                           set())}
    print(cliques)