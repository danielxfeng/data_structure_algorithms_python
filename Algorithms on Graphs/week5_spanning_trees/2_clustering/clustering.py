# Uses python3
import sys


def clustering(x, y, k):
	# print(x, y, k)
	
	length = len(x)
	parents = list(range(length))
	
	edges = [(-1, (None, None))] * ((length * (length - 1)) // 2)# + length)
	i = 0
	for e in range(length):
		for u in range(length):
			if e >= u:
				continue
			edges[i] = (get_distance(x[e], y[e], x[u], y[u]), (e, u))
			i += 1
	
	edges = sorted(edges, key=lambda x: x[0])
	# print("There are %d vertices and %d edges" % (length, len(edges)))
	
	results = []
	for (d, (s, e)) in edges:
		fps = find(s, parents)
		fpe = find(e, parents)
		# print("Going", d, (s, fps), (e, fpe))
		if fps != fpe:
			union(s, e, fps, fpe, parents)
			# print("added", d, (s, fps), (e, fpe))
			# print(parents)
			results.append((d, (s, fps), (e, fpe)))
	
	results = sorted(results, key=lambda x: x[0], reverse=True)
	# print("There are %d distances in the results" % len(results))
	# print(results)
	return results[k - 2][0]


def find(v, parents):
	while v != parents[v]:
		v = parents[v]
	return v


def union(s, e, fps, fpe, parents):
	if fps < fpe:
		parents[e] = fps
		up(fpe, fps, parents)
	else:
		parents[s] = fpe
		up(fps, fpe, parents)
	return


def up(fp, tar, parents):
	while parents[fp] != tar:
		fp = parents[fp]
		parents[fp] = tar
	return


def get_distance(ax, ay, bx, by):
	return abs(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5)


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
		print("{0:.9f}".format(clustering(x, y, k)))


def main():
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	data = data[1:]
	x = data[0:2 * n:2]
	y = data[1:2 * n:2]
	data = data[2 * n:]
	k = data[0]
	print("{0:.9f}".format(clustering(x, y, k)))


if __name__ == '__main__':
	main()
	# run_tests()
