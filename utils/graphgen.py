# Authors:
#  Irene Torrijos
#  Benjamin Maudet


import numpy as np
import networkx as nx


class GraphGenerator:
    def __init__(self, min_nodes=5, max_nodes=15, seed=None):
        np.random.seed(seed)
        self.min_nodes = min_nodes
        self.max_nodes = max_nodes

    def genweight(self, graph):
        # add weights to edges
        for node in graph.nodes:
            # get node parents
            parents = list(graph.predecessors(node))

            # generate N weights that sum to 1
            weights = np.random.dirichlet(np.ones(len(parents)))

            # add weights to edges
            for p in range(len(parents)):
                graph[parents[p]][node]["weight"] = weights[p]

    def generate(self, weighed=False):
        self.num_nodes = np.random.choice(range(self.min_nodes, self.max_nodes+1))

        # create empty graph
        graph = nx.DiGraph()

        # add nodes to the graph
        # graph.add_nodes_from(range(self.num_nodes))

        self.num_edges = np.random.randint(self.num_nodes, self.num_nodes*(self.num_nodes-1)//3)

        # add the nodes to ensure the graph is connected
        for i in range(self.num_nodes):
            graph.add_node(i)
            if i > 0:
                graph.add_edge(np.random.randint(0, i), i)

        # add edges
        for i in range(self.num_edges - len(graph.edges)):
            # random nodes
            source = np.random.randint(0, self.num_nodes)
            target = np.random.randint(0, self.num_nodes)

            # add edge (if not circle)
            if not nx.has_path(graph, target, source):
                graph.add_edge(source, target)

        if weighed:
            self.genweight(graph)


        # should not happen, but just in case
        if not nx.is_directed_acyclic_graph(graph):
            return self.generate()

        return graph




