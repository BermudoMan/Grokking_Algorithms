#endless
def countdown(i):
	print(i)
	countdown(i-1)

# countdown(123)


def countdown2(i):
	print(i)
	if i <= 1:
		return
	else:
		countdown2(i-1)

countdown2(15)
