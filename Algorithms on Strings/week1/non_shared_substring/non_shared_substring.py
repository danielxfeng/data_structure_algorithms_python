# python3
import os
import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class Node:
	def __init__(self, label=''):
		"""
        Node for the trie class.
        """
		self.children = {}
		self.label = label  # label leading up to this node
		self.type = 1  # which string are its children nodes a suffix of
		# P.S a node is of type 1 if all children are type 1 else its type 2
		self.visited = False  # dfs
		self.parent = None


class SuffixTree:
	def __init__(self, s):
		self.root = Node()
		self.root.children[s[0]] = Node(s)
		self.add(s)
	
	def add(self, word):
		"""
        Add all suffixes to the trie, compressing it. There are 3 scenarios:
        1. Inserting a new word into the trie, could be at root or at any internal
        node.
        2. Adding a prefix to an existing node.
        3. Inserting a word in a partial match.
        """
		for i in range(1, len(word)):
			cur = self.root
			j = i
			while j < len(word):
				if word[j] in cur.children:
					child = cur.children[word[j]]
					label = child.label
					k = j + 1
					while k - j < len(label) and word[k] == label[k - j]:
						k += 1
					if k - j == len(label):  # label is exhausted, so move to next one
						cur = child
						j = k
					else:  # either split a node or add prefix
						c_exist, c_new = label[k - j], word[k]
						mid = Node(label[:k - j])
						mid.children[c_new] = Node(word[k:])
						child.label = label[k - j:]
						mid.children[c_exist] = child
						cur.children[word[j]] = mid
				else:  # scenario 1 -> create new node
					cur.children[word[j]] = Node(word[j:])
	
	def shortest_uncommon_string(self):
		"""
        Returns the shortest uncommon string of 2 strings.
        """
		leaves_1 = []
		self.explore(self.root, leaves_1)
		results = []
		for leaf in leaves_1:
			# print("leaf", leaf.label, leaf.parent.type)
			char = ''
			substring = ''
			cur = leaf.parent
			if leaf.label[0] == '#' and cur.type == 2:
				# right labels that are #t$ onwards.
				continue
			elif cur.type == 2:  # just right labels
				char += leaf.label[0]
			while cur != self.root:  # move upwards
				substring = cur.label + substring
				cur = cur.parent
			substring += char
			results.append(substring)
		# print(results)
		result = min(results, key=lambda x: len(x))
		return result
	
	def explore(self, cur, leaves_1):
		"""
        Explore all the unvisited outgoing nodes of a node, check the
        type and add to leaves if the type is as desired.
        """
		cur.visited = True
		
		if len(cur.children) == 0:  # leaf
			if '#' not in cur.label:  # string 2
				cur.type = 2
			else:
				leaves_1.append(cur)
		else:  # internal node
			for char, node in cur.children.items():
				if not node.visited:
					node.parent = cur
					self.explore(node, leaves_1)
			for char, node in cur.children.items():
				if node.type == 2:
					cur.type = 2
	# print("explore", cur.label, cur.type)


def solve(p, q):
	text = p + '#' + q + '$'
	tree = SuffixTree(text)
	return tree.shortest_uncommon_string()


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		if "3" not in f:
			continue
		with open(f, 'r') as fs:
			text = fs.read().strip()
		text = text.split("\n")
		ans = solve(text[0], text[1])
		sys.stdout.write(ans + '\n')


def get_files():
	files = []
	path = os.path.join(os.getcwd(), "sample_tests")
	for file in os.listdir(path):
		if file.split(".")[-1] == "a":
			continue
		files.append(os.path.join(path, file))
	return files


def main():
	p = sys.stdin.readline().strip()
	q = sys.stdin.readline().strip()
	ans = solve(p, q)
	sys.stdout.write(ans + '\n')


if __name__ == '__main__':
	main()
# run_tests()
