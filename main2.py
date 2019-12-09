import math
import copy
import sys
import random


GRAPH = {
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
ROUTE = {
	(0, 1): 1, (1, 0): 1,
	(0, 2): 5, (2, 0): 5,
	(1, 3): 2.5, (3, 1): 2.5,
	(1, 6): 1, (6, 1): 1,
	(3, 4): 1.5, (4, 3): 1.5,
	(4, 5): 1, (5, 4): 1,
	(5, 2): 1, (2, 5): 1,
	(3, 8): 1, (8, 3): 1,
	(4, 9): 1, (9, 4): 1,
	(5, 10): 1, (10, 5): 1,
	(6, 7): 1, (7, 6): 1,
	(7, 8): 1.5, (8, 7): 1.5,
	(8, 9): 1.5, (9, 8): 1.5,
	(9, 10): 1, (10, 9): 1,
	(6, 11): 1, (11, 6): 1,
	(7, 12): 1, (12, 7): 1,
	(9, 13): 1, (13, 9): 1,
	(10, 14): 1, (14, 10): 1,
	(11, 12): 1, (12, 11): 1,
	(12, 13): 3, (13, 12): 3,
	(13, 14): 1, (14, 13): 1,
	(11, 15): 1, (15, 11): 1,
	(12, 16): 1, (16, 12): 1,
	(13, 17): 1, (17, 13): 1,
	(14, 18): 1, (18, 14): 1,
	(15, 16): 1, (16, 15): 1,
	(16, 17): 3, (17, 16): 3,
	(17, 18): 1, (18, 17): 1,
	(15, 19): 1, (19, 15): 1,
	(16, 20): 1, (20, 16): 1,
	(17, 21): 1, (21, 17): 1,
	(18, 22): 1, (22, 18): 1
}
CONCENTRATION = {
	(0, 1): 1497.9, (1, 0): 1497.9,
	(0, 2): 794.9, (2, 0): 794.9,
	(1, 3): 3544.8, (3, 1): 3544.8,
	(1, 6): 2041.6, (6, 1): 2041.6,
	(3, 4): 2782.2, (4, 3): 2782.2,
	(4, 5): 115.3, (5, 4): 115.3,
	(5, 2): 0, (2, 5): 0,
	(3, 8): 1022.2, (8, 3): 1022.2,
	(4, 9): 695.2, (9, 4): 695.2,
	(5, 10): 0, (10, 5): 0,
	(6, 7): 475.6, (7, 6): 475.6,
	(7, 8): 1255, (8, 7): 1255,
	(8, 9): 3275.4, (9, 8): 3275.4,
	(9, 10): 21.8, (10, 9): 21.8,
	(6, 11): 903.8, (11, 6): 903.8,
	(7, 12): 1140.9, (12, 7): 1140.9,
	(9, 13): 806.8, (13, 9): 806.8,
	(10, 14): 0, (14, 10): 0,
	(11, 12): 3233.8, (12, 11): 3233.8,
	(12, 13): 1558.1, (13, 12): 1558.1,
	(13, 14): 1.4, (14, 13): 1.4,
	(11, 15): 1387.5, (15, 11): 1387.5,
	(12, 16): 1273, (16, 12): 1273,
	(13, 17): 678.9, (17, 13): 678.9,
	(14, 18): 0, (18, 14): 0,
	(15, 16): 1622.2, (16, 15): 1622.2,
	(16, 17): 5693, (17, 16): 5693,
	(17, 18): 534.7, (18, 17): 534.7,
	(15, 19): 1866.6, (19, 15): 1866.6,
	(16, 20): 1019.4, (20, 16): 1019.4,
	(17, 21): 715.8, (21, 17): 715.8,
	(18, 22): 0, (22, 18): 0
}
SPEED_RANGE = range(1, 11)
W_C = 0.8
W_D = 0.02

class Node:
	def __init__(self):
		self.state = None

		self.children = []
		self.parent = None

		self.num_wins = 0
		self.num_visits = 0

	def is_fully_expanded(self):
		neighbors = GRAPH[self.state.label]
		if len(self.children) == len(neighbors) * len(SPEED_RANGE):
			# print(len(self.children), neighbors)
			return True
		return False

	def is_leaf(self):
		if len(self.children) == 0:
			return True
		return False

	def get_next_random_node(self):
		new_state = self.state.advance_state_randomly()
		# print(new_state.label)
		new_node = Node()
		new_node.state = new_state
		new_node.parent = self
		self.children.append(new_node)
		# print(new_node.state.label)
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
		count = 0
		while label_choice in self.visited_label and count < 100000:
			label_choice = random.choice(GRAPH[cur_label])
			count += 1
		self.visited_label.add(label_choice)
		speed_choice = random.choice(SPEED_RANGE)
		self.path.append((cur_label, label_choice, speed_choice))
		new_state = State(label_choice, speed_choice, self.t_f, self.cur_time+ROUTE[(self.label, label_choice)]*1000/(speed_choice*0.278), list(self.path), copy.deepcopy(self.visited_label))
		self.visited_label.remove(label_choice)
		self.path.pop()
		# print(new_state.label, new_state.speed)
		return new_state

	def compute_cost(self):
		cost = 0
		# print(self.path)
		for i in range(len(self.path)):
			start = self.path[i][0]
			end = self.path[i][1]
			speed = self.path[i][2]
			cost += W_C * CONCENTRATION[(start, end)] - W_D * speed * 1000
		return cost



def selection(node):
	while node.is_fully_expanded():
		node = best_child(node, False)
	new_node = expand(node)
	if new_node is not None:
		return new_node
	return node
	# while node.state.is_terminal() is False or node.state.label == 0:
	# 	if node.is_fully_expanded():
	# 		node = best_child(node, False)
	# 	else:
	# 		new_node = expand(node)
	# 		return new_node
	# return node

def simulation(node):
	cur_state = node.state
	while cur_state.is_terminal() is False:
		cur_state = cur_state.advance_state_randomly()

	final_cost = cur_state.compute_cost()
	return final_cost

def expand(node):
	new_node = node.get_next_random_node()
	return new_node

def best_child(node, path_found):
	best_score = -sys.maxsize
	best_sub_node = None

	if path_found:
		C = 0
	else:
		C = 1 / math.sqrt(2.0)

	for sub_node in node.children:
		if path_found:
			score = sub_node.num_wins
		else:
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

def find_optimal_path(node):
	# print(node.children)
	while not node.is_leaf():
		node = best_child(node, True)

	return node.state.path

def monte_carlo_search_tree(node):
	max_cost = -sys.maxsize
	for i in range(10000):
		expanded_node = selection(node)
		cost = simulation(expanded_node)
		if cost > max_cost:
			max_cost = cost
			win_or_lose = 1
		else:
			win_or_lose = 0
		backup(expanded_node, win_or_lose)
	path = find_optimal_path(node)
	return path


def main():
	t_f = 240*60
	visited_label = set()
	visited_label.add(0)
	init_state = State(0, 0, t_f, 0, [], visited_label)
	init_node = Node()
	init_node.state = init_state
	path = monte_carlo_search_tree(init_node)
	print(path)


main()



