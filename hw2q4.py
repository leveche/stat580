import networkx as nx
import pylab
import random
from math import sqrt

def gen3board():
	G = nx.Graph()
	G.add_nodes_from(['11','12','13','21','22','23','31','32','33'])
	G.add_edges_from([('11','12'),('11','21'),	\
		('12','13'), ('12','22'),	\
		('13','23'),			\
		('21','22'),('21','31'),	\
		('22','23'),('22','32'),	\
		('23','33'),			\
		('31','32'),			\
		('32','33')			\
		])

	for N in G:
		G.node[N]['nvisits'] = 0
	return G

def genNboard(N):
	g = nx.Graph()
	for i in range (N):
		for j in range (N):
			g.add_node (11*j+i)
			g.node[11*j+i]['nvisits'] = 0
	for i in range (N):
		for j in range(N):
			if ((i+1) < N):
				g.add_edge((11*j+i),(11*j+i+1))
			if ((j+1) < N):
				g.add_edge((11*j+i),(11*(j+1)+i))
	return g

def random_step(G,N):
	nNeigh = len(G.neighbors(N))
	G.node[N]['nvisits'] += 1
	if ( 0 == nNeigh ):
		nextnode = N
	else:
		nextnode = G.neighbors(N)[random.randint(0,nNeigh-1)]
	return nextnode


def random_walk(G,k,N0):
	N = N0
	walk = [ N0 ]
	for i in range(k):
		N = random_step(N)
		walk.append(N)
	return walk

def random_walk_to_node(G,Kmax,Ni,Nf):
	N = Ni
	walk = [ Ni ]
	for i in range(Kmax):
		N = random_step(G,N)
		walk.append(N)
		if N == Nf:
			break
	return walk


# nx.draw(G)

def cornerToCornerWalks(N,n):
	G = genNboard(N)
	wlks = []
	for j in range(2**n):
		wlks.append(len(random_walk_to_node(G,10000,00,((N-1)*11+(N-1))))-1)
	return wlks

def investigateNboardWalks(m,M,n):
	sum 	= lambda x,y: x+y
	mean 	= lambda x: reduce(sum, x)/float(len(x))
	def sigma(lst):
		mu = mean(lst)
		return  sqrt (mean (map (lambda x: (x-mu)**2, lst)))
	mus = []
	for i in range(m,M):
		wlks = cornerToCornerWalks(i,n)
		mus.append(mean(wlks))
	return mus

mus = investigateNboardWalks(2,11,10)

pylab.subplot(211)
pylab.grid(True)
pylab.loglog(range(2,11),mus,basex=2,basey=2)
pylab.title('logarithmic-scale plot')
pylab.subplot(212)
pylab.plot(range(2,11),mus)
pylab.title('linear scale plot')

# pylab.xlabel('no. of walks') 
# pylab.ylabel('length of a walk')
# pylab.legend('mean')
pylab.show()
