fruits = set(['avocado', 'tomato', 'banana'])
vegetables = set(['beets', 'carrots', 'tomato'])
print(fruits)
print(vegetables)

print('merge', fruits | vegetables)
print('cross', fruits & vegetables)
print('minus', fruits - vegetables)
print('minus', vegetables - fruits)