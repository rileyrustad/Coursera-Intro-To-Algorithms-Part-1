
f = open('/Users/mac28/Desktop/CourseraAlgorythms/Week2/QuickSort.txt', 'r')

a = f.readlines()
b = []
for line in a:
	x = line.strip()
	b.append(int(x))
#b = [3,8,1,5,2,4,7,6]
# b = [b[-1]]+b
# print b
# b.pop()
# print b
def QuickSort2(A, m):
	
	if len(A) == 1:
		return A, m
	if len(A) == 2:
		m = m + 1
		return partition2(A), m
	else:
		p = FindMedian(A)
		pivot = A.index(p)
		A[0],A[pivot]=A[pivot],A[0]
		d,e,f,m = partition(A, m)
		if len(d) >= 1 and len(f) >= 1:
			D,m = QuickSort2(d,m)
			F,m = QuickSort2(f,m)
			D.append(e)
			Final = D + F
			return Final, m
		elif len(d) >= 1:
			D,m = QuickSort2(d,m)
			Final = D + [e]
			return Final, m
		elif len(f) >=1:
			F,m = QuickSort2(f,m)
			Final = [e] + F
			return Final, m
			
def partition(A, m):
	n = len(A)
	p = A[0]
	m = m + n -1
	i = 1
	j = 1
	while j < n:
		if p < A[j]:
			j += 1

		elif p > A[j]:
			if j == 1:
				j += 1
				i += 1
			else:
				A[i],A[j] = A[j],A[i]
				j += 1
				i += 1
	
	A[i-1],A[0] = A[0],A[i-1]
	return A[:i-1],A[i-1],A[i:], m

def partition2(A):
	p = A[0]
	if A[0] > A[1]:
		return [A[1],A[0]]
	elif A[0] < A[1]:
		return [A[0],A[1]]

def QuickSortFinal(A,m):
	F,m = QuickSort2(A,m)
	return m
def FindPivots(A):
	n = len(A)
	a = A[0]
	c = A[-1]
	if n % 2 == 0:
		b = A[(n/2)-1]
	elif n % 2 == 1:	
		b = A[(n/2)]
	return a,b,c
    
def FindMedian(A):
    a,b,c = FindPivots(A)
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c


print QuickSortFinal(b, 0)

