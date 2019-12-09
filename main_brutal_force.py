import sys
import numpy as np


class Node:
	def __init__(self, label, speed):
		self.label = label
		self.speed = speed


def computeCost(path, w_c, w_d):
	cost = 0
	for i in range(len(path)):
		start = path[i][0]
		end = path[i][1]
		speed = path[i][2]
		cost += w_c * concentration[(start, end)] - w_d * speed
	return cost


def dfs(cur_node, visited_label, visited_node, cur_time, t_f, S, result, max_cost, w_c, w_d):
	if cur_time > t_f:
		cost = computeCost(S, w_c, w_d)
		if cost > max_cost[0]:
			max_cost[0] = cost
			result.append(list(S))
		return

	for next_label in graph[cur_node.label]:
		if next_label in visited_label:
			continue
		visited_label.add(next_label)
		for speed in range(1, 11, 2):
			if (next_label, speed) in visited_node:
				continue
			visited_node.add((next_label, speed))
			S.append([cur_node.label, next_label, speed])
			dfs(Node(next_label, speed), visited_label, visited_node, cur_time+Route[(cur_node.label, next_label)]*1000/(speed*0.278), t_f, S, result, max_cost, w_c, w_d)
			S.pop()
			visited_node.remove((next_label, speed))
		visited_label.remove(next_label)


start_node = Node(0, 0)
visited_label = set()
visited_node = set()
visited_label.add(0)
visited_node.add((0, 0))

graph = {
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
Route = {
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
concentration = {
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
t_f = 120*60
w_c = 0.8
w_d = 0.1

result = []
max_cost = [-sys.maxsize]
dfs(start_node, visited_label, visited_node, 0, t_f, [], result, max_cost, w_c, w_d)

print(result[-1], max_cost[0])

