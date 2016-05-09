f = open('/Users/mac28/Desktop/CourseraAlgorythms/Week2/QuickSort.txt', 'r')
g = open('/Users/mac28/Desktop/CourseraAlgorythms/Week2/QuickSortOutput.txt','w')

a = f.readlines()
b = []
for line in a:
	x = line.strip()
	b.append(int(x))
b = [3,8,1,5,2,4,7,6]


# def Partition(A,s,r):



def QuickSortFirst(A):
	n = len(A)
	print 'n is ' + str(n)
	i = 1
	j = 1
	if n == 1:
		return A
	elif n == 0:
		return 0
	else:
		p = A[0]
		print 'the first element is p = ' +str(p)
		print A
		while j < n:
			if p > A[j]:
				print'The first element ' + str(p) +' is greater than A[j] '+str(A[j])
				if j == 1:
					print'we would, but it is first... no need to swap'
					j += 1
					i += 1
				else:
					A[i],A[j] = A[j],A[i]
					print 'swap them'
					print A
					j += 1
					i += 1
			else:
				print 'the first element '+ str(p) +' is less than A[j] '+str(A[j]) + ', so move on'
				j += 1
		print 'i is '+str(i)
		print 'j is '+str(j)
		A[0],A[i-1] = A[i-1],A[0]
		print A
		print 'length of A is ' + str(len(A))
		if len(A) == 2:
			print "blah"
			return A
		else:
			B = QuickSortFirst(A[:i-1])
			print "B is " + str(B)
			if len(A[i:]) >= 1:
				print "length of C is " + str(A[i:])
				
				C = QuickSortFirst(A[i:])
				print "C is "+ str(C)
				Final = B.append(A[0])
				Final.append(C)
				return Final
			else:
				print "c is zero, don't append"
				Final = B.append(A[0])
				print Final
				return Final
			return Final




print QuickSortFirst(b)





