# needs mayavi2
# run with ipython -wthread
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import shutil

def draw_simple(path):
	G = nx.Graph()
	fin = open(path,'r')
	graph = fin.readlines()
	#print graph
	G = nx.Graph()
	for i in graph:
		edge = i.split(' ')
		if len(edge) < 2:
			edge = i.split('\t')
		G.add_edge(edge[0], edge[1])
	plt.figure(figsize=(40,40))
	nx.draw(G,
		node_size=4,
                node_color="red",
		)
	plt.savefig("fig1.png", dpi=100)
	shutil.copy('fig1.png','static/output/fig1.png')

