
f = open('/Users/mac28/Desktop/CourseraAlgorythms/Week2/100.txt', 'r')

a = f.readlines()
b = []
for line in a:
	x = line.strip()
	b.append(int(x))
#b = [3,8,1,5,2,4,7,6]

def QuickSort2(A, m):
	if len(A) == 1:
		print 'QuickSort2 on one element'+str(A)
		return A, m
	if len(A) == 2:
		m = m + 1
		print 'm is '+str(m)
		return partition2(A), m
	else:
		d,e,f,m = partition(A, m)
		print 'm is '+str(m)
		print d
		print e
		print f
		print len(d)
		print len(f)
		if len(d) >= 1 and len(f) >= 1:
			print'blah'
			D,m = QuickSort2(d,m)
			F,m = QuickSort2(f,m)
			D.append(e)
			Final = D + F
			return Final, m
		elif len(d) >= 1:
			print 'blah2'
			D,m  = QuickSort2(d,m)
			print e
			print D
			print D + [e]
			Final = D + [e]
			print Final
			return Final, m
		elif len(f) >=1:
			print 'blah3'
			F,m = QuickSort2(f,m)
			print '[e] is '+str([e])
			Final = [e] + F
			return Final, m
			
def partition(A, m):
	n = len(A)
	print 'n is '+str(n)
	p = A[-1]
	m = m + n -1
	i = 0
	j = 0
	while j < n-1:
		if p < A[j]:
			print 'looking at '+str(A[j])+' which is bigger than '+str(p)
			print 'j is '+str(j)
			j += 1
			print A
		elif p > A[j]:
			if j == 0:
				print 'first element, looking at '+str(A[j])+' which is smaller than '+str(p)+ ' no swap'
				print 'j is '+str(j)
				j += 1
				i += 1
				print A
			else:
				print 'looking at '+str(A[j])+' which is smaller than '+str(p)+ ' so swap'
				print 'j is '+str(j)
				A[i],A[j] = A[j],A[i]
				j += 1
				i += 1
				print A
	
	A[i],A[-1] = A[-1],A[i]
	print A
	return A[:i],A[i],A[i+1:], m

def partition2(A):
	p = A[-1]
	if A[0] > A[1]:
		print 'partition2 '+str(A)
		return [A[1],A[0]]
	elif A[0] < A[1]:
		print 'partition2 '+str(A)
		return [A[0],A[1]]

def QuickSortFinal(A,m):
	F,m = QuickSort2(A,m)
	print F
	return m


print QuickSortFinal(b, 0)


