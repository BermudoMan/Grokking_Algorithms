states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

arr = [1, 2, 2, 3, 3, 3]

stations = {
	'kone': set(['id', 'nv', 'ut']),
	'ktwo': set(['wa', 'id', 'mt']),
	'kthree': set(['or', 'nv', 'ca']),
	'kfour': set(['nv', 'ut']),
	'kfive': set(['ca', 'az']),
}

final_stations = set()

while states_needed:
	best_station = None
	states_covered = set()
	for station, states_for_station in stations.items():
		covered = states_needed & states_for_station
		if len(covered) > len(states_covered):
			best_station = station
			states_covered = covered

		states_needed -= states_covered
		final_stations.add(best_station)

print(final_stations)