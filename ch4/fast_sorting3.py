from time import sleep


def print_items(list):
	for item in list:
		print(item)

def print_items2(list):
	for item in list:
		sleep(1)
		print(item)


print_items([2,4,6,8,10])
# print_items2([2,4,6,8,10])



def m_table(array):
	result = []
	row = []
	for x in range(len(array)):
		for y in array:
			result.append(y*array[x])
	return result

print(m_table([2,3,7]))