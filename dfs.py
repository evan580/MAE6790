#change1
from plot import PlotGenerator
import matplotlib.pyplot as plt
import numpy as np

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
CONCENTRATION_10 = {
	(0, 1): 0.776, (1, 0): 0.776,
	(0, 2): 1.309, (2, 0): 1.309,
	(1, 3): 0.689, (3, 1): 0.689,
	(1, 6): 2.033, (6, 1): 2.033,
	(3, 4): 0.746, (4, 3): 0.746,
	(4, 5): 0.615, (5, 4): 0.615,
	(5, 2): 0, (2, 5): 0,
	(3, 8): 1.547, (8, 3): 1.547,
	(4, 9): 0.555, (9, 4): 0.555,
	(5, 10): 0, (10, 5): 0,
	(6, 7): 0.313, (7, 6): 0.313,
	(7, 8): 0.978, (8, 7): 0.978,
	(8, 9): 0.171, (9, 8): 0.171,
	(9, 10): 0.001, (10, 9): 0.001,
	(6, 11): 0.477, (11, 6): 0.477,
	(7, 12): 0.14, (12, 7): 0.14,
	(9, 13): 0.04, (13, 9): 0.04,
	(10, 14): 0, (14, 10): 0,
	(11, 12): 3.724, (12, 11): 3.724,
	(12, 13): 0.08, (13, 12): 0.08,
	(13, 14): 0, (14, 13): 0,
	(11, 15): 0.576, (15, 11): 0.576,
	(12, 16): 0.627, (16, 12): 0.627,
	(13, 17): 0.655, (17, 13): 0.627,
	(14, 18): 0, (18, 14): 0,
	(15, 16): 0.92, (16, 15): 0.92,
	(16, 17): 2.252, (17, 16): 2.252,
	(17, 18): 0.03, (18, 17): 0.03,
	(15, 19): 1.869, (19, 15): 1.869,
	(16, 20): 0.542, (20, 16): 0.542,
	(17, 21): 0.036, (21, 17): 0.036,
	(18, 22): 0, (22, 18): 0
}
W_D = 1
W_C = 1000


class PathFinder:
	def __init__(self, distance, start_node):
		self.optimal_path = []
		self.optimal_cost = 0
		self.visited = set()
		self.visited.add(start_node)
		self.max_distance = distance
		self.start_node = start_node

	def dfs(self, node, distance_travelled, path, concentration):
		if distance_travelled > self.max_distance or self.all_visited():
			cost = self.compute_cost(path, concentration)
			if cost > self.optimal_cost:
				self.optimal_cost = cost
				self.optimal_path = list(path)
			return

		for next_node in GRAPH[node]:
			if next_node in self.visited:
				continue
			path.append(next_node)
			self.visited.add(next_node)
			self.dfs(next_node, distance_travelled+ROUTE[(node, next_node)], path, concentration)
			path.pop()
			self.visited.remove(next_node)

	def compute_cost(self, path, concentration):
		cost = -1
		for i in range(len(path)-1):
			start = path[i]
			end = path[i+1]
			cost += W_D * concentration[(start, end)] - W_C * ROUTE[(start, end)]
		return cost

	def find_optimal_path(self, concentration):
		self.dfs(self.start_node, 0, [self.start_node], concentration)
		return self.optimal_path

	def all_visited(self):
		if len(self.visited) == len(GRAPH):
			return True
		return False


# t_f = 240
# distance = 5 * t_f / 60
# pathFinder = PathFinder(distance, 0)
# path = pathFinder.find_optimal_path(CONCENTRATION_10)
# cost = pathFinder.optimal_cost
# print(path, cost)

path = [0, 2, 5, 10, 14, 18, 22]

plot1 = PlotGenerator(1)
plot1.plot.xlabel('x - axis, (m)') 
plot1.plot.ylabel('y - axis, (m)')
plot1.plot.title('Concentration along each route when all leaked')
plot1.plot.show()

plot2 = PlotGenerator(2)
plot2.plot.xlabel('x - axis, (m)') 
plot2.plot.ylabel('y - axis, (m)')
# plot2.plot.title(f'Optimal path for time limit of {t_f} minutes, with total cost of {int(cost)}')
plot2.plot_path(path)
plot2.plot.title('sub-optimal path with distance limit of 10000m, cost is 794.9')
plot2.plot.show()

# cost of 10 percent concentration
# t_f = 30
# distance = 5 * t_f / 60
# pathFinder = PathFinder(distance, 0)
# path1 = pathFinder.find_optimal_path(CONCENTRATION_10)
# cost = pathFinder.optimal_cost
# print(path1, cost)
# t_f = 45
# distance = 5 * t_f / 60
# pathFinder = PathFinder(distance, 0)
# path2 = pathFinder.find_optimal_path(CONCENTRATION_10)
# cost = pathFinder.optimal_cost
# print(path2, cost)
# t_f = 120
# distance = 5 * t_f / 60
# pathFinder = PathFinder(distance, 0)
# path3 = pathFinder.find_optimal_path(CONCENTRATION_10)
# cost = pathFinder.optimal_cost
# print(path3, cost)
# t_f = 240
# distance = 5 * t_f / 60
# pathFinder = PathFinder(distance, 0)
# path4 = pathFinder.find_optimal_path(CONCENTRATION_10)
# cost = pathFinder.optimal_cost
# print(path4, cost)

# plt.figure(3)
# C_full1, C_101 = np.array([]), np.array([])
# C_full1, C_101 = np.array([]), np.array([])
# C_full1, C_101 = np.array([]), np.array([])
# C_full1, C_101 = np.array([]), np.array([])
# for i in range(len(path1)-1):
# 	start, end = path1[i], path1[i+1]
# 	C_full.append(CONCENTRATION[(start, end)])
# 	C_10.append(CONCENTRATION_10[(start, end)])
# for i in range(len(path2)-1):
# 	start, end = path2[i], path2[i+1]
# 	C_full.append(CONCENTRATION[(start, end)])
# 	C_10.append(CONCENTRATION_10[(start, end)])
# for i in range(len(path3)-1):
# 	start, end = path3[i], path3[i+1]
# 	C_full.append(CONCENTRATION[(start, end)])
# 	C_10.append(CONCENTRATION_10[(start, end)])
# for i in range(len(path4)-1):
# 	start, end = path4[i], path4[i+1]
# 	C_full.append(CONCENTRATION[(start, end)])
# 	C_10.append(CONCENTRATION_10[(start, end)])

# plt.plot()



