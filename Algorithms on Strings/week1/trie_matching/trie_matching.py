# python3
import os
import sys


def build_trie(patterns):
	# print(patterns)
	tree = dict()
	key = 0
	for pattern in patterns:
		parent = 0
		for i in range(len(pattern)):
			if parent not in tree.keys():
				key += 1
				tree[parent] = {pattern[i]: key}
				# print(1, pattern, pattern[i], parent, key)
				parent += 1
			elif pattern[i] not in tree[parent].keys():
				key += 1
				tree[parent][pattern[i]] = key
				# print(2, pattern, pattern[i], parent, key)
				parent = key
			elif pattern[i] in tree[parent].keys():
				parent = tree[parent][pattern[i]]
				# print(3, pattern, pattern[i], parent, key)
	# print(tree)
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
	match = False
	v = 0
	# print("in", i)
	while True:
		if v not in tree.keys():
			# print("    match", match)
			return match
		if i >= length:
			return -1
		symbol = text[i]
		if symbol in tree[v].keys():
			# print("    continue", i)
			if match is False:
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
	main()
	# run_tests()
