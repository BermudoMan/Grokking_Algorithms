#cycle_variant
def sum(arr):
	total = 0
	for x in arr:
		total += x
	return total

print sum([1,2,3,4])


#rec_variant
def sum_rec(arr2):
	if len(arr2) == 1:
		return arr2[0]
	return  arr2[0] + sum_rec(arr2[1:])

print sum_rec([1, 2, 4, 3])


#max value in the list
def max_search(arr3, max=None):
	if max is None:
		max = arr3.pop()
	current = arr3.pop()
	if current > max:
		max = current
	if arr3:
		return max_search(arr3, max)
	return max

print max_search([1,5,3,7,1])