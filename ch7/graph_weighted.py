###initial data
graph = {
	'start': {
		'A': 6,
		'B': 2
	},
	'A': {
		'end': 1
	},
	'B': {
		'A': 3,
		'end': 5
	},
	'end': {}
}

infinity = float('inf')
costs = {'A': 6, 'B': 2, 'C': infinity}

parents = {'A': 'start', 'B': 'start', 'end': None}


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
	neighbors = graph[node]
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