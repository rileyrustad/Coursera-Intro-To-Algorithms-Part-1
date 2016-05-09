f = open('/Users/mac28/Desktop/CourseraAlgorythms/Week1/IntegerArrayTest.txt', 'r')
g = open('/Users/mac28/Desktop/CourseraAlgorythms/Week1/IntegerArrayTestOutput.txt','w')

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
	#return d
# list1 = [1,4,6,7,9]
# list2 = [2,3,5,8,10]
# print merge(list1,total1,list2,total2)

invs = 0
def merge_sort(invs,alist):
	invs = 0
#base case: separete down to 1 element lists
	if len(alist) > 1:
		#separate list into 2 parts
		first = alist[0:len(alist)/2]
		second = alist[len(alist)/2:]
		print first
		print second		
		#recursively call merge_sort on lists
		merge_sort(invs, first)
		merge_sort(invs, second)
		print first
		print second
		#merge the two lists
		final = merge(first, second)
		print final
		return final
r = [2,1,4,3]



# def just_merge_sort(alist):
# #base case: separete down to 1 element lists
# 	if len(alist) > 1:
# 		#separate list into 2 parts
# 		first = alist[0:len(alist)/2]
# 		second = alist[len(alist)/2:]
# 		print "split the array"
# 		print first
# 		print second		
# 		#recursively call merge_sort on lists
# 		if len(first) == 1 and len(second) == 1:
# 			final = merge(first,second)
# 			print "they both are 1, merge them"
# 			print final
# 			return final
# 		elif len(first) == 1 and len(second) == 2:
# 			secondmerge = just_merge_sort(second)
# 			final = merge(first,secondmerge)
# 			print "there is one and two, merge them after merge the 2"
# 			print final
# 			return final
# 		else:
# 			firstmerge = just_merge_sort(first)
# 			secondmerge = just_merge_sort(second)
# 			print "print the merged arrays"
# 			print firstmerge
# 			print secondmerge
# 			#merge the two lists
# 			print "merge those"
# 			final = merge(firstmerge, secondmerge)
# 			print final
# 			return final
# 	else:
# 		return
# r = [10,9,8,7,6,5,4,3,2,1]
# print "print array"
# print r
# print just_merge_sort(r)



# split the list into single element lists
# merge them together
# keep track of how many inversions you find


'''note to future Riley. add an arguement called total to merge_sort. 
merge collects the number of inversions and merge sort adds them together.
maybe re-add those print statements to see if the adding is going as it should
make sure youre adding all the way down the first array when sorting from the second'''

# 
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
print merge_sort_count([6,5,4,3,2,1],0)
term100 = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]

print merge_sort_count(term100,0)[1]

