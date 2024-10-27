# python3
import os
import sys


def build_trie(patterns):
	# print(patterns)
	tree = dict()
	tree[0] = {}
	key = 1
	for pattern in patterns:
		for i in range(len(pattern)):
			current = tree[0]
			for letter in pattern:
				if letter in current:
					current = tree[current[letter]]
				else:
					current[letter] = key
					tree[key] = {}
					current = tree[key]
					key = key + 1
			current['$'] = {}
	print(tree)
	return tree


def solve(text, n, patterns):
	# print(text, n, patterns)
	tree = build_trie(patterns)
	# print(tree)
	result = []
	length = len(text)
	for i in range(length):
		res = prefix_trie_match(text, length, tree, i)
		if res >= 0:
			# print("add", res)
			result.append(res)
	
	return result


def prefix_trie_match(text, length, tree, i):
	match = -1
	v = 0
	# print("in", i)
	while True:
		if "$" in tree[v].keys():
			# print("    match", match)
			return match
		if i >= length:
			# print("    >=", match)
			return -1
		symbol = text[i]
		if symbol in tree[v].keys():
			# print("    continue", i)
			if match == -1:
				match = i
			v = tree[v][symbol]
			i += 1
		# print("        ", i, match)
		else:
			# print("    not match", i)
			return -1


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		data = text.split("\n")
		ans = solve(data[0], int(data[1]), data[2:])
		sys.stdout.write(' '.join(map(str, ans)) + '\n')


def get_files():
	files = []
	path = os.path.join(os.getcwd(), "sample_tests")
	for file in os.listdir(path):
		if file.split(".")[-1] == "a":
			continue
		files.append(os.path.join(path, file))
	return files


def main():
	text = sys.stdin.readline().strip()
	n = int(sys.stdin.readline().strip())
	patterns = []
	for i in range(n):
		patterns += [sys.stdin.readline().strip()]
	ans = solve(text, n, patterns)
	sys.stdout.write(' '.join(map(str, ans)) + '\n')


if __name__ == '__main__':
	# main()
	run_tests()
	
