###initial data
graph = {
	'start': {
		'A': 10,
	},
	'A': {
		'C': 20,
	},
	'B': {
		'A': 1,
	},
	'C': {
		'end': 30,
		'B': 1
	},
}

infinity = float('inf')
costs = {'A': 10, 'B': infinity, 'C': infinity, 'D': infinity, 'end': infinity}

parents = {'A': 'start', 'B': None, 'C': None, 'D': None, 'end': None}


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