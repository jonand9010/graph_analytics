import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self, nodes = None, adjacency_matrix = None):
        self.nodes = nodes 
        self.adjacency_matrix = adjacency_matrix

    def get_adjacency_matrix(self, similarity_metric = 'norm'):
        num_nodes = self.nodes.shape[0]
        self.adjacency_matrix = np.zeros((num_nodes, num_nodes))
        for node_1 in range(num_nodes):
            for node_2 in range(node_1, num_nodes):
                self.adjacency_matrix[node_1, node_2] = self.get_similarity_score(self.nodes[node_1], self.nodes[node_2], similarity_metric)
                
        self.adjacency_matrix += self.adjacency_matrix.T

    def get_similarity_score(self, x, y, similarity_metric):
        if similarity_metric == 'norm':
            return np.linalg.norm(x - y)

    def binarize_edges(self, threshold = 0.5):
        self.adjacency_matrix[ self.adjacency_matrix > threshold] = 1
        self.adjacency_matrix[ self.adjacency_matrix < threshold] = 0

    def plot(self):
        nxGraph = nx.from_numpy_matrix(self.adjacency_matrix)
        nx.draw(nxGraph, node_size = 50,
                    width = 0.5,
                    alpha = 0.5)
    




