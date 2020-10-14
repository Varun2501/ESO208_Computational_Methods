import numpy as np

def Thomas(a, b, n):

	l = np.zeros(n)
	u = np.zeros(n)
	d = np.zeros(n)

	for i in range(n):
		d[i] = a[i][i]

	for i in range(1, n):	
		u[i-1] = a[i-1][i]
	
	for i in range(0, n-1):
		l[i+1] = a[i+1][i]

	alpha = np.zeros(n)
	beta = np.zeros(n)

	alpha[0] = d[0]
	beta[0] = b[0]

	for i in range(1, n):
		alpha[i] = d[i] - (l[i]*u[i-1])/alpha[i-1]
		beta[i] = b[i] - (l[i]*beta[i-1])/alpha[i-1]

	x = np.zeros(n)
	x[n-1] = beta[n-1]/alpha[n-1]

	for i in range(n-2, -1, -1):
		x[i] = (beta[i] - u[i]*x[i+1])/alpha[i]

	print(l, d, u)
	print(x)

n = 4
a = np.asarray([2, -1, 0, 0, -1, 2, -1, 0, 0, -1, 2, -1, 0, 0, -1, 1]).reshape(n, n)
b = np.asarray([0, 0, 1, 0]).reshape(n, 1)
Thomas(a, b, n)
