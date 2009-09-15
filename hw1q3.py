import networkx as nx
import random

G = nx.Graph()
G.add_nodes_from(['00','01','10','11','20','02'])
G.add_edges_from([('00','01'),('00','10'),('01','10'),	\
		('10','20'),('10','11'), 		\
		('01','11'),('01','02'),		\
		('20','11'),('11','02'),		\
		])

for N in G:
	G.node[N]['nvisits'] = 0
	G.node[N]['balls'] = 11111
	if (4 == len(G.neighbors(N))):
		G.node[N]['balls'] = 2 * G.node[N]['balls'] 
	G.node[N]['orig_balls'] = G.node[N]['balls']
	print N, G.node[N]

def random_step(N):
	nNeigh = len(G.neighbors(N))
	G.node[N]['nvisits'] += 1
	if ( 0 == nNeigh ):
		nextnode = N
	else:
		nextnode = G.neighbors(N)[random.randint(0,nNeigh-1)]
	return nextnode


def random_walk(k,N0):
	N = N0
	walk = [ N0 ]
	for i in range(k):
		N = random_step(N)
		walk.append(N)
	return walk

def calibrate():
	print random_walk(20,'11')

def fourStepwalk(K):
	retcounter = 0
	viscounter = 0
	for i in range(K):
		w = random_walk(4,'00')
		if '00' == w[len(w)-1]:
			retcounter += 1
		w.pop(0)
		if '00' in w:
			viscounter += 1
	return ( float(retcounter)/float(K), float(viscounter)/float(K) )

def shuffle_balls(K):
	for k in range(K):
		z = 1
		if ( 4 == G.neighbors(N) ):
			z = 2
		for n in G:
			if ( G.node[n]['balls'] ):
				G.node[random_step(n)]['balls'] += z
				G.node[n]['balls'] -= z
	diff = 0
	for n in G:
		diff += abs(G.node[n]['balls']-G.node[n]['orig_balls'])
		print G.node[n], diff
	return diff

shuffle_balls(100000)

# raise SystemExit
import pylab

walks = []
R = []
V = []
for i in range(7,17):
	walks.append(2**i)
for i in walks:
	(r,v) = fourStepwalk(i)
	R.append(abs(r-9./64.))
	V.append(abs(v-25./64.))

shuffles=[]
D=[]
for i in range(10,20):
	shuffles.append(i)
	D.append(shuffle_balls(i))

# pylab.subplot(211)
l=pylab.plot(walks,R,walks,V)
pylab.xlabel('no. of walks') 
pylab.ylabel('difference with predicted value')
pylab.legend(('return after 4 steps','revisit in 4 steps'))
pylab.show()

raise SystemExit

pylab.subplot(212)
m = pylab.plot(shuffles,D)
pylab.xlabel('no. of shuffles')
pylab.ylabel('total no. of moved balls')
pylab.show()
