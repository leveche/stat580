
for N in G:
	G.node[N]['nvisits'] = 0

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

def fourStepwalk():
	retcounter = 0
	viscounter = 0
	K = 2**20
	for i in range(K):
		w = random_walk(4,'00')
		if '00' == w[len(w)-1]:
			retcounter += 1
		w.pop(0)
		if '00' in w:
			viscounter += 1
	print float(retcounter)/float(K), float(viscounter)/float(K)

