# python3
import os
import sys


def find_occurrences(text, patterns):
	# print("Text", text)
	# print("Patterns", patterns)
	sa = build_suffix_array(text + "$")
	# lst = [text[i:] for i in sa]
	# print("sa", sa)
	# print("lst", lst)
	res = []
	for pattern in patterns:
		mini = 0
		maxi = len(sa) - 1
		
		while maxi - mini > 3:
			mid = (mini + maxi) // 2
			if pattern > text[sa[mid]:]:
				mini = mid + 1
			else:
				maxi = mid - 1
		
		start = mini
		
		maxi = len(sa) - 1
		pattern_add = pattern + "|"
		while maxi - mini > 3:
			mid = (mini + maxi) // 2
			if pattern_add < text[sa[mid]:]:
				maxi = mid - 1
			else:
				mini = mid - 1
		
		end = maxi
		
		if start > end:
			continue
		
		length = len(pattern)
		for i in range(start, end + 1):
			s = sa[i]
			if text[s: s + length] == pattern:
				res.append(sa[i])
		
	return res


def build_suffix_array(text):
	"""
	Build suffix array of the string text and
	return a list result of the same length as the text
	such that the value result[i] is the index (0-based)
	in text where the i-th lexicographically smallest
	suffix of text starts.
	"""
	# print(text)
	order = sort_char(text)
	class_ = compute_char_class(text, order)
	l = 1
	while l < len(text):
		order = sort_double(text, l, order, class_)
		class_ = update_classes(order, class_, l)
		l = 2 * l
	
	# result = []
	# Implement this function yourself
	return order


def sort_char(text):
	len_t = len(text)
	order = [0] * len_t
	sigma = sorted(set(text))
	count = [text.count(c) for c in sigma]
	
	for j in range(1, len(count)):
		count[j] += count[j - 1]
	for i, c in reversed(list(enumerate(text))):
		count[sigma.index(c)] -= 1
		order[count[sigma.index(c)]] = i
	# print("order1-1", order)
	return order


def compute_char_class(text, order):
	len_t = len(text)
	class_ = [0] * len_t
	class_[order[0]] = 0
	for i in range(1, len_t):
		if text[order[i]] != text[order[i - 1]]:
			class_[order[i]] = class_[order[i - 1]] + 1
		else:
			class_[order[i]] = class_[order[i - 1]]
	# print("class_", class_)
	return class_


def sort_double(text, l, order, class_):
	len_t = len(text)
	count = [0] * len_t
	new_order = [0] * len_t
	for i in range(len_t):
		count[class_[i]] += 1
	for j in range(1, len_t):
		count[j] += count[j - 1]
	for i in range(len_t - 1, -1, -1):
		start = (order[i] - l + len_t) % len_t
		cl = class_[start]
		count[cl] -= 1
		new_order[count[cl]] = start
	# print("order1-2", new_order)
	return new_order


def update_classes(order, class_, l):
	# print("order", order)
	# print("l", l)
	n = len(order)
	new_class = [0] * n
	new_class[order[0]] = 0
	for i in range(1, n):
		cur = order[i]
		prev = order[i - 1]
		mid = cur + l
		mid_prev = (prev + l) % n
		if class_[cur] != class_[prev] or class_[mid] != class_[mid_prev]:
			new_class[cur] = new_class[prev] + 1
		else:
			new_class[cur] = new_class[prev]
	return new_class


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		data = text.split("\n")
		text = data[0]
		patterns = data[2].split()
		occs = find_occurrences(text, patterns)
		print(" ".join(map(str, occs)))


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
	pattern_count = int(sys.stdin.readline().strip())
	patterns = sys.stdin.readline().strip().split()
	occs = find_occurrences(text, patterns)
	print(" ".join(map(str, occs)))


if __name__ == '__main__':
	# main()
	run_tests()
