import unittest
from Graph import Graph

__author__ = 'sean vinas'


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_node(self):
        g = self.graph
        self.assertDictEqual(g.graph, dict())
        self.assertSetEqual(g.nodes, set())
        g.node('a')
        self.assertIn('a', g.nodes)
        self.assertIn('a', g.graph.keys())
        g.node('b')
        self.assertIn('b', g.nodes)
        self.assertIn('b', g.graph.keys())
        """ Add a None node, does nothing."""
        g.node(None)
        self.assertNotIn(None, g.nodes)
        g.node(1)
        self.assertIn(1, g.nodes)
        self.assertIn(1, g.graph.keys())

    def test_edges(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.add_edges('a', 'b')
        self.assertIn('a', g.graph.keys())
        self.assertIn('b', g.graph.keys())
        self.assertEqual(2, len(g.graph.keys()))

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
        self.assertNotIn('c', g.graph.keys())
        self.assertNotIn('d', g.graph.keys())
        self.assertNotIn('c', g.graph.values())
        self.assertNotIn('d', g.graph.values())
        g.add_edges('c', 'c')
        self.assertNotIn('c', g.graph.keys())
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

    def test_neighbor(self):
        g = self.graph
        g.node('a')
        g.node('b')
        g.node('c')
        g.add_edges('a', 'b')
        self.assertIn('a', g.neighbor('b'))
        self.assertEqual(1, len(g.neighbor('b')))
        self.assertNotIn('c', g.neighbor('b'))
        g.add_edges('c', 'b')
        self.assertIn('c', g.neighbor('b'))
        self.assertEqual(2, len(g.neighbor('b')))
        self.assertIsNone(g.neighbor('e'))

if __name__ == '__main__':
    unittest.main()