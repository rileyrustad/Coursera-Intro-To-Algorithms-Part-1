
f = '/Users/mac28/Desktop/CourseraAlgorythms/Week6/2sum.txt'
graph = {}

with open(f) as data:
	for line in data:
		graph[int(line)] = None


# def sum2(graph):
# 	x = range(-10000,10001)
# 	counter = 0
# 	while 
# 	for i in x:

def sum3(graph):
	counter = 0
	whilecounter = -10000
	while whilecounter < 10001:
		for i in graph:
			if (whilecounter - i) in graph and (whilecounter - i) != i:
				counter +=1
				break
		whilecounter += 1
	return counter

print sum3(graph)





	# 	component = line.split()
	# 	if int(component[0]) in graph:
	# 		graph[int(component[0])][0].append(int(component[1]))
	# 	else:
	# 		graph[int(component[0])] = [int(component[1])],[],[]
	# print graph