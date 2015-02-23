__author__ = "Sean R. Vinas"
__date__ = "19 February 2014"
__doc__ = """ Codeeval puzzle Triangle pass.
Find the path with the greatest cumulative sum."""

from queue import Queue


class Graph:

    def __init__(self):
        self.graph = dict()

    def __str__(self):
        # Print the graph in a more readable format for terminal size.
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

    def parent(self, mom, son):
        if self.connected(mom, son) and mom[0] < son[0]:
            return True
        else:
            return False


def path_distance(graph):
    distance = dict()
    sorted_graph = sorted(graph.graph)
    start = sorted_graph[0]
    distance[start] = int(start[1])
    max_distance = int(start[1])
    for node in sorted_graph:
        for friend in graph.neighbors(node):
            if friend[0] > node[0]:
                if friend not in distance:
                    distance[friend] = distance[node] + int(friend[1])
                    if distance[friend] > max_distance:
                        max_distance = distance[friend]
                else:
                    if distance[friend] < distance[node] + int(friend[1]):
                        distance[friend] = distance[node] + int(friend[1])
                        if distance[friend] > max_distance:
                            max_distance = distance[friend]
    return max_distance


def input_to_graph(input_file):
    g = Graph()
    prev_nodes = list()
    s = 0
    with open(input_file, 'r') as f:
        lines = (lines.rstrip('\n') for lines in f)
        for line in lines:
            line = line.split()
            end = len(line)
            r = range(s, s + end)
            s += end
            nodes = list(zip(r, line))
            for n, node in enumerate(prev_nodes):
                g.node(nodes[n])
                g.add_edges(node, nodes[n])
                g.node(nodes[n + 1])
                g.add_edges(node, nodes[n + 1])
            prev_nodes = nodes
            for n in nodes:
                g.node(n)
    return g


def main():
    filename = 'input.txt'
    g = input_to_graph(filename)
    print(path_distance(g))


if __name__ == "__main__":
    main()