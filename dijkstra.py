def find_the_lowest_cost_node(costs, searched):
	lowest_cost_node = None
	lowest_cost = float('inf')
	for node in costs:
		if costs[node] < lowest_cost and node not in searched:
			lowest_cost_node = node
			lowest_cost = costs[node]
	return lowest_cost_node

def dijkstra():
	searched = []	
	node = find_the_lowest_cost_node(costs, searched)
	while node is not None:
		neighbor = graph[node]
		for i in neighbor:
			neighbor_cost = costs[i]
			new_cost = costs[node] + neighbor[i]
			if neighbor_cost > new_cost:
				costs[i] = new_cost
				parents[i] = node
		searched.append(node)
		node = find_the_lowest_cost_node(costs, searched)

