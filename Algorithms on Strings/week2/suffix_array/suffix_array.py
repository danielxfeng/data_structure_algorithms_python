# python3
import os
import sys


def build_suffix_array(text):
	"""
	Build suffix array of the string text and
	return a list result of the same length as the text
	such that the value result[i] is the index (0-based)
	in text where the i-th lexicographically the smallest
	suffix of text starts.
	"""
	# print("text", text)
	suffixes = [None] * len(text)
	suffixes[0] = text
	for i in range(1, len(text)):
		suffixes[i] = text[i:]
	suffixes = [(t, i) for i, t in enumerate(suffixes)]
	suffixes.sort()
	result = [i[1] for i in suffixes]
	
	# print(result)
	return result


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		print(" ".join(map(str, build_suffix_array(text))))


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
	print(" ".join(map(str, build_suffix_array(text))))


if __name__ == '__main__':
	main()
	# run_tests()
