
from collections import deque



def person_is_seller(name):
	return name[-1] == 'm'

def searching():
	graph = {}
	graph['you'] = ['alice', 'bob', 'claire']
	graph['bob'] = ['anuj', 'peggy']
	graph['alice'] = ['peggy']
	graph['claire'] = ['tom', 'jonny']

	search_queue = deque()
	search_queue += graph['you']

	searched = []

	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + ' is a mango seller!')
				return True
			else:
				try:
					print(person + ' is not a mango seller')
					search_queue += graph[person]
					searched.append(person)
				except:
					print(person)
	return False

searching()
