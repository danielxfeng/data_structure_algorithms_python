# python3
import os
import sys


def InverseBWT(bwt):
	last = [(v, i) for (i, v) in enumerate(bwt)]
	first = sorted(last)
	first_to_last = {f: l for f, l in zip(first, last)}
	# print(first_to_last)
	
	next = first[0]
	result = ''
	for i in range(len(bwt)):
		result += next[0]
		next = first_to_last[next]
		# print(next)
	
	return result[::-1]
	
	
def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		print(InverseBWT(text))


def get_files():
	files = []
	path = os.path.join(os.getcwd(), "sample_tests")
	for file in os.listdir(path):
		if file.split(".")[-1] == "a":
			continue
		files.append(os.path.join(path, file))
	return files


def main():
	bwt = sys.stdin.readline().strip()
	print(InverseBWT(bwt))


if __name__ == '__main__':
	main()
	# run_tests()
