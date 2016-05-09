# f = '/Users/mac28/Desktop/CourseraAlgorythms/Week3/kargerMinCut.txt'

# nodes = {}
# with open(f) as data:
# 	for line in data:
# 		component = line.split()
# 		nodes[int(component[0])] = [int(item) for item in component[1:]]
# print nodes
# x = []
# for i in nodes:
# 	x.append(len(nodes[i]))

# print min(x)
f = '/Users/mac28/Desktop/CourseraAlgorythms/Week4/SCC1.txt'
graph = {}

with open(f) as data:
	for line in data:
		component = line.split()
		if int(component[0]) in graph:
			graph[int(component[0])][0].append(int(component[1]))
		else:
			graph[int(component[0])] = [int(component[1])],[],[]
n = len(graph)
rangelist = list(reversed(range(n+1)))
del rangelist[-1]
print rangelist
