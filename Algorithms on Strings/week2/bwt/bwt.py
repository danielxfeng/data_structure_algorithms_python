# python3
import os
import sys


def BWT(text):
	# print(text)
	length = len(text)
	results = [[] for _ in range(length)]
	for i in range(length):
		text = text[-1] + text[:-1]
		results[i] = text
	
	results.sort()
	# print(results)
	result = [i[-1] for i in results]

	return "".join(result)


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		print(BWT(text))


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
	print(BWT(text))


if __name__ == '__main__':
	main()
	# run_tests()
