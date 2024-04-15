###initial data
graph = {
	'start': {
		'A': 5,
		'B': 2
	},
	'A': {
		'C': 4,
		'D': 2
	},
	'B': {
		'A': 8,
		'D': 7
	},
	'C': {
		'end': 3,
		'D': 6
	},
	'D': {
		'end': 1
	}
}

infinity = float('inf')
costs = {'A': 5, 'B': 2, 'C': infinity, 'D': infinity, 'end': infinity}

parents = {'A': 'start', 'B': 'start', 'C': None, 'D': None, 'end': None}


###array for saving completed nods
processed = []

# print(graph, costs, parents)
# print(graph['start']['A'])


###alhorithm
def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]
	# print(cost)
	try:
		neighbors = graph[node]
	except:
		print('KeyError: end', cost, node)
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		try:
			if costs[n] > new_cost:
				costs[n] = new_cost
				parents[n] = node
		except:
			print('without cost!')
	processed.append(node)
	node = find_lowest_cost_node(costs)
print(new_cost)