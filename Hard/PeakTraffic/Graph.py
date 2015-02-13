""" A Python Class
A simple undirected Python graph class.
"""


from queue import Queue


class Graph:

    def __init__(self):
        """ initializes a graph object """
        self.nodes = set()  # Useful set operations like union and intersect for graph algorithms
        self.graph = dict()

    def __str__(self):
        """ Print the graph in a more readable format for terminal size."""
        line = ''
        for node in self.graph.keys():
            if self.graph[node]:
                line += str(node) + ' : ['
                last = len(self.graph[node]) - 1
                for i, edge in enumerate(self.graph[node]):
                    if i != last:
                        line += str(edge) + ', '
                    else:
                        line += str(edge)
                line += ']\n'
        return line

    def node(self, node):
        if node is None:
            return
        if node not in self.nodes:
            self.nodes.add(node)
            self.graph[node] = None

    def edges(self, node):
        if node in self.nodes:
            return self.graph[node]
        else:
            return None

    def add_edges(self, node_a, node_b):
        # Must be nodes before becoming an edge
        if node_a in self.nodes and node_b in self.nodes:
            # Add a loop
            if node_a == node_b:
                if self.graph[node_a] is None:
                    self.graph[node_a] = [node_a]
                elif node_a not in self.graph[node_a]:
                    self.graph[node_a].append(node_b)
            # Haven't added these edges yet, not a loop
            if self.graph[node_a] is None:
                self.graph[node_a] = [node_b]
            elif node_b in self.graph[node_a]:
                pass
            else:
                self.graph[node_a].append(node_b)
            if self.graph[node_b] is None:
                self.graph[node_b] = [node_a]
            elif node_a in self.graph[node_b]:
                pass
            else:
                self.graph[node_b].append(node_a)

    def degree(self, node):
        if node in self.nodes:
            # loops counted twice!
            if node in self.nodes and node in self.graph[node]:
                return len(self.graph[node]) + 1
            else:
                return len(self.graph[node])

    def connected(self, node_a, node_b):
        if node_a in self.nodes and node_b in self.nodes:
            return node_a in self.graph[node_b] if self.graph[node_b] is not None else False
        else:
            return False

    def bfs_distance(self, start, stop):
        """ Breadth first search of graph to find distance between start and stop node."""
        if start in self.nodes and stop in self.nodes:
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

    def neighbor(self, node):
        if node in self.graph and self.graph[node] is not None:
            return [n_node for n_node in self.graph[node] if n_node]

    def bron_kerbosch_2(self, current, prospective, processed):
        """ Bron-Kerbosch algorithm for finding max cliques."""
        if not any((prospective, processed)):
            #if len(current) > 2:
                # Only if the clique has 3 or more nodes
            yield sorted(current)
        for node in prospective[:]:
            current_node = current + [node]
            prospective_node = [n for n in prospective if n in self.neighbor(node)]
            processed_node = [n for n in processed if n in self.neighbor(node)]
            for each_current_node in self.bron_kerbosch_2(current_node, prospective_node, processed_node):
                #if len(each_current_node) > 2:
                    # Only if the clique has 3 or more nodes
                yield sorted(each_current_node)
            prospective.remove(node)
            processed.append(node)



if __name__ == '__main__':
    g = Graph()
    g.node('a')
    g.node('b')
    g.node('c')
    g.node('d')
    g.node('e')
    g.add_edges('a', 'b')
    g.add_edges('a', 'c')
    g.add_edges('a', 'd')
    g.add_edges('b', 'c')
    g.add_edges('b', 'd')
    g.add_edges('c', 'd')
    g.add_edges('e', 'b')
    g.add_edges('e', 'd')

    print(g)
    cliques = g.bron_kerbosch_2([], list(g.graph.keys()), [])
    for max_cliques in sorted(cliques):
        sorted_max_cliques = sorted(max_cliques)
        print(*sorted_max_cliques, sep=', ')