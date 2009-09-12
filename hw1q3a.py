from scipy import *

P = array ( ( (0,2,2,0,0,0),\
		(1,0,1,1,1,0),\
		(1,1,0,0,1,1),\
		(0,2,0,0,2,0),\
		(0,1,1,1,0,1),\
		(0,0,2,0,2,0) ) )
M = diag ((1,1,1,1,1,1))
p = (1./9.,2./9.,2./9.,1./9.,2./9.,1./9.)
for i in range (4):
	M = dot(M,P/4.)
	print M
	print M[0][0] # / 4.**(i+1)
	o = dot (p,M)
	print o, o.sum()

for i in range(4,100):
	M = dot(M,P/4.)

print M, M.sum(axis=1)

print linalg.eig((P/4.),left=True,right=False)

s= array( (0.13608276, 0.28867513,  0.25819889, -0.53152694, -0.44758526, 0.23616826) )

print s - dot (transpose(P/4.),s)
