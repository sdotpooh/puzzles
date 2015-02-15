import unittest
from Graph import Graph

__author__ = 'sean vinas'


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_node(self):
        g = self.graph
        self.assertDictEqual(g.graph, dict())
        g.node('a')
        self.assertIn('a', g.graph)
        g.node('b')
        self.assertIn('b', g.graph)
        g.node(None)
        self.assertNotIn(None, g.graph)
        g.node(1)
        self.assertIn(1, g.graph)

    def test_edges(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.add_edges('a', 'b')
        self.assertIn('a', g.graph)
        self.assertIn('b', g.graph)
        self.assertEqual(2, len(g.graph))

    def test_add_edges(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.add_edges('a', 'b')
        self.assertIn('b', g.graph['a'])
        self.assertIn('a', g.graph['b'])
        g.add_edges('a', 'a')
        self.assertIn('a', g.graph['a'])
        g.add_edges('a', 'a')
        self.assertEqual(2, len(g.graph['a']))
        g.add_edges('b', 'b')
        self.assertEqual(2, len(g.graph['b']))
        self.assertIn('b', g.graph['b'])
        g.add_edges('a', 'b')
        self.assertEqual(2, len(g.graph['a']))
        self.assertEqual(2, len(g.graph['b']))
        # Adding edges before nodes
        g.add_edges('a', 'd')
        g.add_edges('c', 'a')
        self.assertEqual(2, len(g.graph['b']))
        self.assertNotIn('c', g.graph)
        self.assertNotIn('d', g.graph)
        self.assertNotIn('c', g.graph.values())
        self.assertNotIn('d', g.graph.values())
        g.add_edges('c', 'c')
        self.assertNotIn('c', g.graph)
        self.assertNotIn('c', g.graph.values())

    def test_degree(self):
        g = self.graph
        g.node('a')
        g.add_edges('a', 'a')
        self.assertEqual(2, g.degree('a'))
        g.node('b')
        g.add_edges('a', 'b')
        self.assertEqual(3, g.degree('a'))
        self.assertEqual(1, g.degree('b'))
        # If a node isn't in the graph, return None
        self.assertEqual(None, g.degree('c'))

    def test_connected(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.node('c')
        g.add_edges('a', 'b')
        self.assertTrue(g.connected('a', 'b'))
        self.assertFalse(g.connected('a', 'c'))
        self.assertFalse(g.connected('a', 'd'))
        self.assertFalse(g.connected('d', 'a'))

    def test_neighbor(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.node('c')
        g.add_edges('a', 'b')
        self.assertIn('a', g.neighbors('b'))
        self.assertEqual(1, len(g.neighbors('b')))
        self.assertNotIn('c', g.neighbors('b'))
        g.add_edges('c', 'b')
        self.assertIn('c', g.neighbors('b'))
        self.assertEqual(2, len(g.neighbors('b')))
        self.assertIsNone(g.neighbors('e'))

    def test_def_bron_kerbosch(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.node('c')
        g.node('d')
        g.node('e')
        g.node('f')
        g.add_edges('a', 'b')
        g.add_edges('a', 'c')
        g.add_edges('b', 'c')
        g.add_edges('d', 'e')
        g.add_edges('f', 'd')
        g.add_edges('f', 'e')
        nodes = {node for node in g.graph.keys() if any(node)}
        cliques = {tuple(clique) for clique in g.bron_kerbosch(set(), nodes,
                                                               set())}
        self.assertEqual({('a', 'b', 'c'), ('d', 'e', 'f')}, cliques)
        # Add an independent loop. Causes max recursive depth.
        # Need a work around!
        # g.add_edges('f', 'f')
        # Detect if any loop, if none, then run bron_kerbosch?

    def test_bfs_distance(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.node('c')
        g.add_edges('a', 'b')
        self.assertEqual(2, g.bfs_distance('a', 'b'))
        g.add_edges('b', 'c')
        self.assertEqual(3, g.bfs_distance('a', 'c'))
        self.assertEqual(0, g.bfs_distance('a', 'a'))
        self.assertEqual(0, g.bfs_distance('a', 'x'))
        g.add_edges('a', 'a')
        self.assertEqual(2, g.bfs_distance('a', 'b'))


if __name__ == '__main__':
    unittest.main()