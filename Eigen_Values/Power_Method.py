import numpy as np

def PowerMethod(a, z, n):

	z  = a@z
	print(z)
	e = 1
	lamb = 1

	while e>= 0.0001:
		
		max_ = abs(z[0])
		idx = 0
		for i in range(1, n):
			if abs(z[i]) > max_:
				idx = i
		
		lamb_new = z[idx]

		y = z/lamb_new
		e = abs((lamb_new - lamb)/lamb_new)
		lamb = lamb_new

		z = a@y

	print(lamb)

n = 3
a = np.asarray([-2, -4, 2, -2, 1, 2, 4, 2, 5]).reshape(n, n)
z = np.asarray([1, 1, 1]).reshape(n, 1)

PowerMethod(a, z, n)
print(a)

