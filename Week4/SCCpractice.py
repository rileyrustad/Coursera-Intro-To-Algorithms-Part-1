
f = '/Users/mac28/Desktop/CourseraAlgorythms/Week4/SCC1.txt'
graph = {}

with open(f) as data:
	for line in data:
		component = line.split()
		if int(component[0]) in graph:
			graph[int(component[0])][0].append(int(component[1]))
		else:
			graph[int(component[0])] = [int(component[1])],[],[]
	print graph

'''I want to input a sorted graph that I will work from high to low, 
	starting with the highest node.
	I want the output to be the total nodes that have been explored, and the
	number of nodes that have been explored in this iteration. then I will 
	append this number to an ongoing list that will pop the top 5 numbers '''

def HiLoDFS(graph, node, explored):
	explored1 = [node]
	stack = [node]
	while len(stack) > 0:
		v = stack.pop(0)
		print 'v is ' + str(v)
		for i in graph[v][0]:
			if i not in explored1:
				stack = [i] + stack
				explored1.append(i)
				print 'stack is ' + str(stack)
				print 'explored is ' + str(explored1)
	return explored + explored1, len(explored1)	

explored = [10,11,12,13]


print HiLoDFS(graph, 6, explored)
