import networkx as nx
import pylab
import random
import matplotlib.pyplot as plt
# import uuid

def offspring(node,gen):
	num = random.choice([0,1,1,2])
	print 'node', node, 'in gen', gen, 'will have', num, 'offspring'
	for i in range(num):
		o = 16*(node/16 +1) + 4*(node/4 + 1) + i
		for j in range(5):
			if (o in g):
				o += 1
		g.add_node(o)
		g.node[o]['gen']=gen+1
		g.add_edge(node,o)
	print map (lambda x: g.node[x]['gen'], g.successors(node))
	return g.successors(node)

def activenodes(gen):
	return filter (lambda x:g.node[x]['gen']==gen,g.nodes())

def evolve(maxgen):
	for j in range(maxgen):
		print 'an=',activenodes(j)
		if ([]==activenodes(j)):
			print 'extinction!'
			return j
		for o in activenodes(j):
			print 'o=', o
			offspring (o,j)
	print 'pop did not become extinct'
	return j

g = nx.DiGraph()
g.add_node(1)
g.node[1]['gen']=0
ext = 0
for pop in range(10):
	if (11 > evolve(12)):
		print 'starting pop', pop+1
		ext += 1
print ext
# print g.nodes()
#nx.draw(g)
# plt.show()

raise SystemExit
