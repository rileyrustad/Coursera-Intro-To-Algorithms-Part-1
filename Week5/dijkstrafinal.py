f = '/Users/mac28/Desktop/CourseraAlgorythms/Week5/dijkstraDATA2.txt'
graph = {}
heap = []

with open(f) as data:
	for line in data:
		component = line.split()
		x = []
		for i in component:
			a = i.split(',')
			y = []
			for z in a:
				y.append(int(z))
			x.append(y)
		p = x[0][0]
		graph[p] = []
		for i in x[1:]:
			graph[p].append(i)


def heapify(x, heap):
	heap.append(x)
	i = heap.index(x)
	while i > 0:
		if heap[i] < heap[i//2]:
			heap[i], heap[i//2] = heap[i//2], heap[i]
		i = i//2
	return heap
def extract_min(heap):
	print heap
	a = heap.pop(0)
	b = heap.pop()
	heap = [0]+[b]+heap
	print heap
	i = 1
	while i * 2 + 1 <= len(heap):
		print 'i is '+str(heap[i])
		m = minChild(heap,i)
		print'm is ' +str(heap[m])
		if heap[i]>heap[m]:
			print 'heap[i]>heap[m]'
			heap[i],heap[m] = heap[m],heap[i]
		i = m
		print heap
	return a, heap[1:]
def minChild(heap, i):
	if i * 2 + 1 > len(heap)-1:
		return i * 2
	else:
		if heap[i*2] < heap[i*2+1]:
			return i * 2
		else:
			return i * 2 + 1

def dijkstra(graph,s,v):
	distancegraph = {1:[0,1]}
	outwardgraph = {}
	explored =[]
	discovered = [1]
	counter = 2
	to_explore = s
	while counter > 0:
		distances = []
		for i in graph[to_explore]:
			discovered.append(i[0])
			outwardgraph.update({i[0]:[i[1]+distancegraph[to_explore][0],to_explore]})
		for edge in outwardgraph:
			distances.append(outwardgraph[edge][0])
		print distances
		m = min(distances)
		for edge in outwardgraph:
			if outwardgraph[edge][0] == m:
				to_explore = edge

			# for edge in discovered and not in explored:
			# # 	distances.append(distancegraph[edge][0])
			# # 	print distances
			# # 	minimum = min(distances)

			# explored.append(to_explore)
			# print discovered
			# to_explore = shortest new path
		# for i in graph[]
			

			# distancegraph.update({i[0]:i[1]})


		counter = counter - 1
	print distancegraph
	# return distancegraph[v]






	# 	if int(component[0]) in graph:
	# 		graph[int(component[0])][0].append(int(component[1]))
	# 	else:
	# 		graph[int(component[0])] = [int(component[1])],[],[]
	# print graph

'''we are trying to find the shortest path from s to v'''
def dijkstra2(graph,s,v):
	finalgraph = {}
	outwardgraph = {}
	to_explore = s
	counter = 2
	while to_explore != v:
		if finalgraph == {}:
			finalgraph = {s:[0,s]}
		distances = []
		for i in graph[to_explore]:
			if i[0] not in finalgraph:
				if i[0] in outwardgraph:
					if finalgraph[to_explore][0]+i[1] < outwardgraph[i[0]][0]:
						outwardgraph.update({i[0]:[finalgraph[to_explore][0]+i[1],to_explore]})
					else:
						outwardgraph.update({i[0]:[outwardgraph[i[0]][0],to_explore]})
				else:
					outwardgraph.update({i[0]:[finalgraph[to_explore][0]+i[1],to_explore]})
		for edge in outwardgraph:
			distances.append(outwardgraph[edge][0])
		m = min(distances)
		for edge in outwardgraph:
			if outwardgraph[edge][0] == m and edge not in finalgraph:
				to_explore = edge
		newvalue = outwardgraph.pop(to_explore)
		finalgraph[to_explore] = newvalue

	return finalgraph[to_explore][0]





print dijkstra2(graph,1,7)







