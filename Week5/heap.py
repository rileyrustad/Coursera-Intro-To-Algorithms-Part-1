heap = [4,4,8,9,4,12,9,11,13,]

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


print heapify(11,heap)


