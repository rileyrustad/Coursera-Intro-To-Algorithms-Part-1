import random
from math import log
f = '/Users/mac28/Desktop/CourseraAlgorythms/Week3/kargerMinCut.txt'

nodes = {}
with open(f) as data:
	for line in data:
		component = line.split()
		nodes[int(component[0])] = [int(item) for item in component[1:]]



def mincut(a):
	j = 0
	iterations = len(a)
	smallest_cut = len(a)**2
	while j < iterations:
		j += 1
		dict2 = a.copy()
		x = findcut(dict2)
		if x < smallest_cut:
			smallest_cut = x
	return smallest_cut

def findcut(a):
	while len(a) > 2:
		a = contract(a)
	b = a.items()[0]
	return len(b[1])

def contract(a):
	x = random.choice(a.keys())
	y = random.choice(a[x])
	for i in a[y]:
		a[i] = [z if z != y else x for z in a[i]]
	for i in a[y]:
		a[x].append(i)
	del a[y]
	a[x] = [z for z in a[x] if z != x]
	return a


print mincut(nodes)





