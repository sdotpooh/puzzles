__author__ = 'seanvinas'
__date__ = '12 February 2015'
""" A Python Class
A simple undirected Python graph class.
"""

class Graph:

    def __init__(self):
        """ initializes a graph object """
        self.nodes = set()
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
        return self.graph[node]

    def add_edges(self, node_a, node_b):
        # Add a loop
        if node_a == node_b and node_a in self.nodes:
            self.graph[node_a] = [node_b]
        # Haven't added these edges yet, not a loop
        if self.graph[node_a] is None:
            self.graph[node_a] = [node_b]
        elif node_b in self.graph[node_a]:
            pass
        else:
            self.graph[node_a].append(node_b)


    def degree(self, node):
        if node in self.nodes:
            # loops counted twice!
            if node in self.nodes and node in self.graph[node]:
                return len(self.graph[node]) + 1
            else:
                return len(self.graph[node])

    def connected(self, node_a, node_b):
        if node_a in self.nodes and node_b in self.nodes:
            return node_a in self.graph[node_b]
        else:
            return False

    def neighbor(self, node):
        if node in self.graph:
            return [n_node for n_node in self.graph[node] if n_node]

    def bron_kerbosch_2(self, current, prospective, processed):
        """ Bron-Kerbosch algorithm for finding max cliques."""
        if not any((prospective, processed)):
            if len(current) > 2:
                # Only if the clique has 3 or more nodes
                yield sorted(current)
        for node in prospective[:]:
            current_node = current + [node]
            prospective_node = [n for n in prospective if n in self.neighbor(node)]
            processed_node = [n for n in processed if n in self.neighbor(node)]
            for each_current_node in self.bron_kerbosch_2(current_node, prospective_node, processed_node):
                if len(each_current_node) > 2:
                    # Only if the clique has 3 or more nodes
                    yield sorted(each_current_node)
            prospective.remove(node)
            processed.append(node)


def main():
    g = Graph()
    with open('input.txt', 'r') as f:
        lines = filter(None, (line.rstrip('\n') for line in f))
        for line in lines:
            date, node_a, node_b = line.split('    ')
            g.node(node_a)
            g.node(node_b)
            g.add_edges(node_a, node_b)
    print(g)
    # Make a list of all nodes that have edges excluding if edges is None
    nodes = [node for node, edge in g.graph.items() if edge is not None]
    cliques = g.bron_kerbosch_2([], nodes, [])
    for max_cliques in sorted(cliques):
        print(*max_cliques, sep=', ')


if __name__ == '__main__':
    main()