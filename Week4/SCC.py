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

def BFS(graph, node):
	explored = [node]
	queue = [node]
	while len(queue) > 0 :
		v = queue.pop(0)
		print 'v is ' + str(v)
		for i in graph[v][0]:
			if i not in explored:
				queue.append(i)
				explored.append(i)
				print 'queue is ' + str(queue)
				print 'explored is ' + str(explored)
	return explored



def DFS(graph, node, explored):
	explored1 = [node]
	explored2 = []
	stack = [node]
	while len(stack) > 0:

		v = stack.pop(0)
		print 'v is ' + str(v)
		for i in graph[v][0]:
			print graph[v][0]
			if i not in explored1:
				stack = [i] + stack
				explored1.append(i)
				explored2.append(i)
				print 'stack is ' + str(stack)
				print 'explored1 is ' + str(explored1)
				print 'explored2 is ' + str(explored2)
			else:
				print 'blah'
				explored2 = []

	return explored + explored1


print DFS(graph,8,[])
# print DFS(graph, 3)

# def discover_all(graph):
# 	n = len(graph)
# 	explored = []
# 	for i in graph:
# 		if i in explored
# 			explored = DFS(graph,i,explored)
		
# print discover_all(graph)

# def reverse_graph(graph):
# 	new_graph = {}
# 	for i in graph:
# 		for x in graph[i][0]:
# 			if x in new_graph:
# 				new_graph[x][0].append(i)
# 			else:
# 				new_graph[x] = [i],[],[]
# 	return new_graph 

# print reverse_graph(graph)


def Find_HiLoDFS(graph):
	n = len(graph)
	explored = []
	while 0 < n:
		if n not in explored:
			explored, number_explored = DFS(graph, n, explored)
		print n
		n = n - 1



# print HiLoDFS(graph)

# def SCC(graph):
# 	n = len(graph)


