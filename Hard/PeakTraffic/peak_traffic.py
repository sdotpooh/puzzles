""" Peak Traffic codeeval.com puzzle.
Max cliques in graph.
"""
__author__ = 'Sean Vinas'
__date__ = '14 February 2015'


class Graph:

    def __init__(self):
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
        if node not in self.graph:
            self.graph[node] = set()

    def add_edges(self, node_a, node_b):
        self.graph[node_a].add(node_b)

    def neighbors(self, node):
        return self.graph[node]

    def bron_kerbosch(self, current, prospective, processed):
        """ Bron-Kerbosch algorithm to find max cliques.
        But with a clique containing > 2 nodes.
        """
        if not any((prospective, processed)):
            if len(current) > 2:  # At least 3 nodes in a clique
                yield sorted(current)
        for node in prospective:
            for clique in self.bron_kerbosch(
                    current.union({node}),
                    prospective.intersection(self.neighbors(node)),
                    processed.intersection(self.neighbors(node))):
                yield clique
            prospective.discard({node})
            processed.union({node})


def main():
    g = Graph()
    with open('input.txt', 'r') as f:
        lines = filter(None, (line.rstrip('\n') for line in f))
        for line in lines:
            date, node_a, node_b = line.split('    ')
            g.node(node_a)
            g.node(node_b)
            g.add_edges(node_a, node_b)
    nodes = {node for node in g.graph.keys() if any(node)}
    cliques = {tuple(clique) for clique in g.bron_kerbosch(set(), nodes,
                                                           set())}
    print('Graph')
    print('Node: [Edges]')
    print(g)
    print('Max Cliques (greater than 2 nodes):')
    for clique in sorted(cliques):
        last = len(clique) - 1
        for n, node in enumerate(clique):
            print(node) if n == last else print(node, end=', ')


if __name__ == '__main__':
    main()