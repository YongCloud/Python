# Compute pi by Monte Carlo method
from random import random
DOTS = 1000 * 1000
hits = 0

for i in range(DOTS):
	x,y = random(),random()
	dist = (x**2 + y**2) ** 0.5
	if dist <= 1.0:
		hits += 1

pi = 4 * (hits/DOTS)
print('pi: {:.16f}'.format(pi))
