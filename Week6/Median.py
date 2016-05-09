f='/Users/mac28/Desktop/CourseraAlgorythms/Week6/Median.txt'
start = []
start2 = []



with open(f) as data:
	for line in data:
		a = line.split()
		start.append(a)
for i in start:
	start2.append(int(i[0]))
	# start2.append[i[0]]


heap = [4,4,8,9,4,12,9,11,13,]
newheap = []

def highheapify(x, heap):
	heap = [0]+heap
	heap.append(x)

	i = len(heap)-1
	while i > 0:
		if heap[i] > heap[i//2]:
			break
		elif heap[i] < heap[i//2]:
			heap[i], heap[i//2] = heap[i//2], heap[i]
		i = i//2
	return heap[1:]

def highextract_min(heap):
	heap2 = heap[:]
	a = heap2.pop(0)
	b = heap2.pop()
	heap2 = [0]+[b]+heap2
	i = 1
	while i * 2 + 1 <= len(heap2):
		m = highminChild(heap2,i)
		if heap2[i]>heap2[m]:
			heap2[i],heap2[m] = heap2[m],heap2[i]
		i = m
	return a, heap2[1:]

def highminChild(heap, i):
	if i * 2 + 1 > len(heap)-1:
		return i * 2
	else:
		if heap[i*2] < heap[i*2+1]:
			return i * 2
		else:
			return i * 2 + 1

heap = [4,4,8,9,4,12,9,11,13,15]

def lowheapify(x, heap):
	heap = [0]+heap
	heap.append(x)
	i = len(heap)-1
	while i > 1:
		if heap[i] < heap[i//2]:
			break
		elif heap[i] > heap[i//2]:
			heap[i], heap[i//2] = heap[i//2], heap[i]
		i = i//2
	return heap[1:]

def lowextract_min(heap):

	a = heap.pop(0)
	b = heap.pop()
	heap = [0]+[b]+heap

	i = 1

	while i * 2 + 1 <= len(heap):
		m = lowminChild(heap,i)
		if heap[i]<heap[m]:
			heap[i],heap[m] = heap[m],heap[i]
		i = m
	return a, heap[1:]

def lowminChild(heap, i):
	if i * 2 + 1 > len(heap)-1:
		return i * 2
	else:
		if heap[i*2] > heap[i*2+1]:
			return i * 2
		else:
			return i * 2 + 1

def firstChooseHighLow(start2,high,low,medians):
	trial = []
	medians.append(start2[0])
	trial.append(start2.pop(0))
	trial.append(start2.pop(0))
	a = max(trial)
	b = min(trial)
	medians.append((a+b)/2)

	high.append(a)
	low.append(b)
	medians.append

	return high,low, start2, medians

def chooseHighLow(i,high,low):
	if i > high[0]:
		high = highheapify(i,high)
	elif i < low[0]:
		low = lowheapify(i,low)
	elif i < high[0] and i > low[0]:
		high = highheapify(i,high)
	return high,low

def medmaint(start2):
	high = []
	low = []
	medians = []
	high,low,start2,medians = firstChooseHighLow(start2,high,low,medians)
	for i in start2:
		high,low = chooseHighLow(i,high,low)
		high,low,median= evening(high,low)
		medians.append(median)
	return medians



		

			#how do they get odd? when they do, is it always on the high side?





def evening(high,low):
	if len(high) > len(low)+1:
		a, high = highextract_min(high)
		low = lowheapify(a,low)
		median = (high[0]+low[0])/2
	elif len (high) == len(low)+1:
		median = high[0]
	elif len(high) == len(low):
		median = (high[0]+low[0])/2
	elif len(high)+1 == len(low):
		median = low[0]	
	elif len(high)+1 < len(low):
		a, low = lowextract_min(low)
		high = highheapify(a,high)
		median = (high[0]+low[0])/2
	return high, low, median

blah = medmaint(start2)


def sumMedians(blah):
	counter = 0
	for i in blah:
		counter += i
	return counter % 10000
print sumMedians(blah)










