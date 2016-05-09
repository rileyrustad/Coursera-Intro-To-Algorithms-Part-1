f = open('/Users/mac28/Desktop/CourseraAlgorythms/Week1/IntegerArray.txt', 'r')
g = open('/Users/mac28/Desktop/CourseraAlgorythms/Week1/IntegerArrayOutput.txt','w')

a = f.readlines()
b = []
for line in a:
	line = line.strip()
	b.append(int(line))

def merge(first, firsttotal, second, secondtotal):
	c = len(first) + len(second)
	d = []
	i = 0
	j = 0
	total = firsttotal + secondtotal
	while i < len(first) and j < len(second):
		if first[i] < second[j]:
			d.append(first[i])
			i += 1
		else:
			d.append(second[j])
			j += 1
			total += len(first[i:])
	while i < len(first):
		d.append(first[i])
		i += 1
	while j < len(second):
		d.append(second[j])
		j += 1
	return d, total

def merge_sort_count(alist, total):
#base case: separete down to 1 element lists
	if len(alist) > 1:
		#separate list into 2 parts
		first = alist[0:len(alist)/2]
		second = alist[len(alist)/2:]		
		#recursively call merge_sort on lists
		if len(first) == 1 and len(second) == 1:
			final = merge(first, 0 , second, 0)
			return final
		elif len(first) == 1 and len(second) == 2:
			secondmerge, total = merge_sort_count(second, total)
			final = merge(first, 0, secondmerge, total)
			return final
		else:
			firstmerge, total1 = merge_sort_count(first, total)
			secondmerge, total2 = merge_sort_count(second, total)
			#merge the two lists
			final = merge(firstmerge, total1, secondmerge, total2)
			return final
		return final[1]
	else:
		return


print merge_sort_count(b,0)[1]