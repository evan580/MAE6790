import math
import copy

class Node:
	def __init__(self, label, speed):
		self.label = label # node's information
		self.speed = speed
		self.num_visits = 0 # statistic for Monte Carlo
		self.num_wins = 0
		self.parent = None # Tree structure
		self.children = []

	def is_fully_expanded(self, graph, speed_range):
		neighbors = graph[Node.label]
		if len(self.children) == len(neighbors) * len(speed_range):
			return True
		return False


class State:
	def __init__(self, t_f, w_c, w_d, start_node):
		self.path = [start_node]
		self.t_f = t_f
		self.w_c = w_c
		self.w_d = w_d
		self.visited_label = set()
		self.visited_node = set()
		self.visited_node.add((start_node.label, start_node.speed))
		self.visited_label.add(start_node.label)
		self.cur_node = self.path[-1]

		self.time_used = 0

	def is_terminal(self):
		if self.time_used > self.t_f:
			return True
		return False

	def compute_cost(self):
		cost = 0
		w_c = self.w_c
		w_d = self.w_d
		for i in range(1, len(self.path)):
			start = self.path[i-1].label
			end = self.path[i].label
			speed = self.path[i].speed
			cost += w_c * CONCENTRATION[(start, end)] - w_d * speed
		return cost

	def get_next_random(self, graph, speed_range):
		cur_node = self.path[-1]
		label_choice = random.choice(graph[cur_node.label])
		speed_choice = random.choice(speed_range)
		while (label_choice, speed_choice) in self.visited_node:
			label_choice = random.choice(graph[cur_node.label])
			speed_choice = random.choice(speed_range)




class Route:
	def __init__(self, t_f):
		self.graph = {
			0: [1, 2],
			1: [0, 3, 6],
			2: [0, 5],
			3: [1, 4, 8],
			4: [3, 5, 9],
			5: [2, 4, 10],
			6: [1, 7, 11],
			7: [6, 8, 12],
			8: [3, 7, 9],
			9: [4, 8, 10, 13],
			10: [5, 9, 14],
			11: [6, 12, 15],
			12: [7, 11, 13, 16],
			13: [9, 12, 14, 17],
			14: [10, 13, 18],
			15: [11, 16, 19],
			16: [12, 15, 17, 20],
			17: [13, 16, 18, 21],
			18: [14, 17, 22],
			19: [15],
			20: [16],
			21: [17],
			22: [18]
		}
		self.label_to_cartisian = []
		self.t_f = t_f
		self.concentration_field = {}
		self.visited_label = set()
		self.visited_node = set()


	def next_node(self, cur_node_label, cur_time):
		if cur_time > self.t_f:
			return None
		
		for node_label in self.graph[cur_node_label]:
			if node_label not in self.visited_label:
				for speed in range(1, 11):
					if (node_label, speed) not in self.visited_node:
						self.visited_label.add(node_label)
						self.visited_node.add((node_label, speed))
						return TreeNode(node_label, speed)

class Node:
	def __init__(self):
		self.state = None

		self.children = []
		self.parent = None

		self.num_wins = 0
		self.num_visits = 0

	def is_fully_expanded(self):
		neighbors = GRAPH[Node.label]
		if len(self.children) == len(neighbors) * len(SPEED_RANGE):
			return True
		return False

	def is_leaf(self):
		if len(self.children) == 0:
			return True
		return False

	def get_next_random_node(self):
		new_state = self.state.advance_state_randomly()
		new_node = Node()
		new_node.state = new_state
		new_node.parent = self
		self.children.append(new_node)
		return new_node

class State:
	def __init__(self, label, speed, t_f, cur_time, path, visited_label):
		self.label = label
		self.speed = speed
		self.cur_time = cur_time
		self.visited_label = visited_label
		self.path = path
		self.t_f = t_f

	def is_terminal(self):
		if self.cur_time > self.t_f:
			return True
		return False

	def advance_state_randomly(self):
		cur_label = self.label
		label_choice = random.choice(GRAPH[cur_label])
		while label_choice in self.visited_label:
			label_choice = random.choice(GRAPH[cur_label])
		self.visited_label.add(label_choice)
		speed_choice = random.choice(SPEED_RANGE)
		self.path.append((cur_label, label_choice, speed_choice))
		new_state = State(label_choice, speed_choice, self.t_f, cur_time+ROUTE[(self.label, label_choice)]*1000/(speed_choice*0.278), list(self.path), copy.deepcopy(self.visited_label))
		self.visited_label.remove(label_choice)
		self.path.pop()

		return new_state

	def compute_cost(self):
		cost = 0
		for i in range(1, len(self.path)):
			start = self.path[i-1][0]
			end = self.path[i][1]
			speed = self.path[i][2]
			cost += W_C * CONCENTRATION[(start, end)] - W_D * speed
		return cost



def selection(node):
	while node.is_leaf() is False:
		if node.is_fully_expanded():
			node = best_child(node)
		else:
			new_node = expand(node)
			return new_node
	return node

def simulation(node):
	cur_state = node.state
	while cur_state.is_terminal() is False:
		cur_state = cur_state.advance_state_randomly()

	final_cost = cur_state.compute_cost()
	return final_cost

def expand(node):
	new_node = node.get_next_random_node()
	return new_node

def best_child(node):
	best_score = -sys.maxsize
	best_sub_node = None

	C = 1 / math.sqrt(2.0)
	for sub_node in node.children:
		left = sub_node.num_wins / sub_node.num_visits
	    right = 2.0 * math.log(node.num_visits) / sub_node.num_visits
	    score = left + C * math.sqrt(right)

	    if score > best_score:
	    	best_score = score
	    	best_sub_node = sub_node

	return best_sub_node

def backup(node, win_or_lose):

	while node != None:
		node.num_visits += 1
		node.num_wins += win_or_lose
		node = node.parent

def monte_carlo_search_tree(node):

	for i in range(1000):
		expanded_node = selection(node)
		cost = simulation(expanded_node)
		backup(expanded_node, cost)


def main():
	t_f = 45*60
	init_state = State(0, 0, t_f, 0, [], set())
	init_node = Node()
	init_node.state = init_state
	monte_carlo_search_tree(init_node)
	path = find_optimal_path(init_node)






