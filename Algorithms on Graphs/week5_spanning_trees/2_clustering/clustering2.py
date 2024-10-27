# Uses python3
import math
import sys


def distance(xi, yi, xj, yj):
	return math.sqrt(math.pow(xi - xj, 2) + math.pow(yi - yj, 2))


def clustering(n, adj, weight, k):
	X = set()
	T = set()
	X.add(0)
	
	while len(X) != n:
		crossing = set()
		for u in X:
			for v in adj[u]:
				if v not in X:
					crossing.add((u, v))
		edge = sorted(crossing, key=lambda e: weight[e[0]][e[1]])[0]
		T.add(edge)
		X.add(edge[1])
	
	
	T = sorted(T, key=lambda e: weight[e[0]][e[1]])
	print(len(T), T)
	
	for _ in range(k - 2):
		T.pop(len(T) - 1)
	
	print(len(T), T)
	d = T.pop(len(T) - 1)
	print(len(T), T)
	print(d)
	return weight[d[0]][d[1]]


def run_tests():
	test_data = (
		(
			(12,),
			(7, 6),
			(4, 3),
			(5, 1),
			(1, 7),
			(2, 7),
			(5, 7),
			(3, 3),
			(7, 8),
			(2, 8),
			(4, 4),
			(6, 7),
			(2, 6),
			(3,),
		),
		(
			(8,),
			(3, 1),
			(1, 2),
			(4, 6),
			(9, 8),
			(9, 9),
			(8, 9),
			(3, 11),
			(4, 12),
			(4,),
		),
	)
	for td in test_data:
		x = []
		y = []
		for t in td[1:-1]:
			x.append(t[0])
			y.append(t[1])
		k = td[-1][0]
		n = len(x)
		adj = [[] for _ in range(n)]
		weight = [[0] * n for _ in range(n)]
		for i in range(n):
			adj[i] = list(v for v in range(n) if v != i)
			for j in range(n):
				if i != j:
					w = distance(x[i], y[i], x[j], y[j])
					weight[i][j] = w
					weight[j][i] = w
		
		print("{0:.9f}".format(clustering(n, adj, weight, k)))


def main():
	user_input = sys.stdin.read()
	data = list(map(int, user_input.split()))
	n = data[0]
	data = data[1:]
	x = data[0:2 * n:2]
	y = data[1:2 * n:2]
	data = data[2 * n:]
	k = data[0]
	
	adj = [[] for _ in range(n)]
	weight = [[0] * n for _ in range(n)]
	for i in range(n):
		adj[i] = list(v for v in range(n) if v != i)
		for j in range(n):
			if i != j:
				w = distance(x[i], y[i], x[j], y[j])
				weight[i][j] = w
				weight[j][i] = w
	
	print("{0:.9f}".format(clustering(n, adj, weight, k)))


if __name__ == '__main__':
	run_tests()
	
