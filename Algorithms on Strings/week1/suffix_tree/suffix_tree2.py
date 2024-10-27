# python3
import os
import sys


class Node(object):
	def __init__(self, label):
		self.label = label
		self.out = {}


def suffixTree(text):
	nodes = []
	root = Node(None)
	root.out[text[0]] = Node(text)
	# print("root", root.label, root.out["A"].label)
	if not root.out[text[0]] in nodes:
		nodes.append(root.out[text[0]])
		
	for i in range(1, len(text)):
		curr_node = root
		j = i
		while j < len(text):
			if text[j] in curr_node.out:
				child = curr_node.out[text[j]]
				label = child.label
				k = j + 1
				while k - j < len(label) and text[k] == label[k - j]:
					k += 1
				if k - j == len(label):
					curr_node = child
					j = k
				else:
					c_exist, c_new = label[k - j], text[k]
					mid = Node(label[:k - j])
					if mid not in nodes:
						nodes.append(mid)
						mid.out[c_new] = Node(text[k:])
					if not mid.out[c_new] in nodes:
						nodes.append(mid.out[c_new])
					mid.out[c_exist] = child
					child.label = label[k - j:]
					curr_node.out[text[j]] = mid
					break
			
			else:
				curr_node.out[text[j]] = Node(text[j:])
				if not curr_node.out[text[j]] in nodes:
					nodes.append(curr_node.out[text[j]])
	
	return nodes


def build_suffix_tree(text):
	# print("text", text)
	result = []
	nodes = suffixTree(text)
	
	for node in nodes:
		result.append(node.label)
	
	return result


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		result = build_suffix_tree(text)
		print("\n".join(result))


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
	result = build_suffix_tree(text)
	print("\n".join(result))


if __name__ == '__main__':
	main()
	# run_tests()
