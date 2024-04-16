###initial data
graph = {
	'start': {
		'A': 2,
		'B': 2,
	},
	'A': {
		'C': 2,
		'end': 2,
	},
	'B': {
		'A': 2,
	},
	'C': {
		'end': 2,
		'B': -1
	},
}

infinity = float('inf')
costs = {'A': 2, 'B': 2, 'C': infinity, 'D': infinity, 'end': infinity}

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

	try:
		neighbors = graph[node]
	except:
		break
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		print(n, new_cost)
		try:
			if costs[n] > new_cost:
				costs[n] = new_cost
				parents[n] = node
		except:
			print('without cost!')
	processed.append(node)
	node = find_lowest_cost_node(costs)

print(new_cost)