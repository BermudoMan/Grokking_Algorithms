first_word = str(input())
second_word = str(input())

array = []

count = 0

for i in range(0, len(second_word)):
	for j in range(0, len(first_word)):
		if second_word[i] == first_word[j]:
			count += 1
			array.append(count)
		else:
			# array.append(0)
			try:
				count = max(array)
			except:
				print('not')

print(array)
