# python3
import os
import sys


def find_pattern(pattern, text):
	"""
	Find all the occurrences of the pattern in the text
	and return a list of all positions in the text
	where the pattern starts in the text.
	"""
	large_s = pattern + "$" + text
	s = compute_prefix(large_s)
	# print("s", s)
	result = []
	len_p = len(pattern)
	for i in range(len_p + 1, len(s)):
		if s[i] == len_p:
			# print(s[i], len_p)
			result.append(i - (2 * len_p))
		
	# print(pattern, text)
	# print("res", result)
	return result


def compute_prefix(p):
	len_p = len(p)
	s = [None] * len_p
	s[0], border = 0, 0
	for i in range(1, len_p):
		while border > 0 and p[i] != p[border]:
			border = s[border - 1]
		if p[i] == p[border]:
			border += 1
		else:
			border = 0
		# print("border", i, border)
		
		s[i] = border
		
	return s


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		text = text.split("\n")
		pattern = text[0]
		text = text[1]
		result = find_pattern(pattern, text)
		print(" ".join(map(str, result)))


def get_files():
	files = []
	path = os.path.join(os.getcwd(), "sample_tests")
	for file in os.listdir(path):
		if file.split(".")[-1] == "a":
			continue
		files.append(os.path.join(path, file))
	return files


def main():
	pattern = sys.stdin.readline().strip()
	text = sys.stdin.readline().strip()
	result = find_pattern(pattern, text)
	print(" ".join(map(str, result)))


if __name__ == '__main__':
	main()
	# run_tests()
