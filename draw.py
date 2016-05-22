# needs mayavi2
# run with ipython -wthread
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def draw_simple(path):
	G = nx.Graph()
	fin = open(path,'r')
	graph = fin.readlines()
	print graph
	G = nx.Graph()
	for i in graph:
		edge = i.split(' ')
		if len(edge) < 2:
			edge = i.split('\t')
		G.add_edge(edge[0], edge[1])
	nx.draw(G)
	plt.show()

