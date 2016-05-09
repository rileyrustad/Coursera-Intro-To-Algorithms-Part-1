f = open('/Users/mac28/Desktop/CourseraAlgorythms/Week2/100.txt', 'r')


a = f.readlines()
b = []
for line in a:
	x = line.strip()
	b.append(int(x))
print b



def QuickSort2(A):
	if len(A) == 1:
		print 'QuickSort2 on one element'+str(A)
		return A
	if len(A) == 2:
		return partition2(A)
	else:
		d,e,f = partition(A)
		print d
		print e
		print f
		print len(d)
		print len(f)
		if len(d) >= 1 and len(f) >= 1:
			print'blah'
			D = QuickSort2(d)
			F = QuickSort2(f)
			D.append(e)
			Final = D + F
			return Final
			return D
		elif len(d) >= 1:
			print 'blah2'
			D = QuickSort2(d)
			print e
			print D
			print D + [e]
			Final = D + [e]
			print Final
			return Final
		elif len(f >=1):
			print 'blah3'
			F = QuickSort2(f)
			return [e] + F
			
def partition(A):
	n = len(A)
	p = A[0]
	i = 1
	j = 1
	while j < n:
		if p < A[j]:
			print 'looking at '+str(A[j])+' which is bigger than '+str(p)
			j += 1
			print A

		elif p > A[j]:
			if j == 1:
				print 'first element, looking at '+str(A[j])+' which is smaller than '+str(p)+ ' no swap'
				j += 1
				i += 1
				print A
			else:
				print 'looking at '+str(A[j])+' which is smaller than '+str(p)+ ' so swap'
				A[i],A[j] = A[j],A[i]
				j += 1
				i += 1
				print A
	
	A[i-1],A[0] = A[0],A[i-1]
	print A
	return A[:i-1],A[i-1],A[i:]

def partition2(A):
	p = A[0]
	if A[0] > A[1]:
		print 'partition2 '+str(A)
		return [A[1],A[0]]
	elif A[0] < A[1]:
		print 'partition2 '+str(A)
		return [A[0],A[1]]




			
			
print QuickSort2([25, 22, 24, 23])


