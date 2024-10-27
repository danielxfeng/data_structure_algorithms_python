# python3
import os
import sys


def PreprocessBWT(bwt):
	"""
	Preprocess the Burrows-Wheeler Transform bwt of some text
	and compute as a result:
		*   starts - for each character C in bwt, starts[C] is the first position
			of this character in the sorted array of
			all characters of the text.
		*   occ_count_before - for each character C in bwt and each position P in bwt,
			occ_count_before[C][P] is the number of occurrences of character C in bwt
			from position 0 to position P inclusive.
	"""
	
	# print("BWT", bwt)
	
	occ_count_before = {}
	first = "".join(sorted(bwt))
	# print("FST", first)
	starts = {}
	
	for i, t in enumerate(first):
		if t not in starts:
			starts[t] = i
	
	keys = starts.keys()
	
	for k in keys:
		c = 0
		lst = [0] * (len(bwt) + 1)
		for i, t in enumerate(bwt):
			if t == k:
				c += 1
			lst[i + 1] = c
		occ_count_before[k] = lst
	
	return starts, occ_count_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
	"""
	Compute the number of occurrences of string pattern in the text
	given only Burrows-Wheeler Transform bwt of the text and additional
	information we get from the preprocessing stage - starts and occ_counts_before.
	"""
	# print("Pattern", pattern, "BWT", bwt, "starts", starts, "occ_counts_before", occ_counts_before)
	top = 0
	bottom = len(bwt) - 1
	while top <= bottom:
		if pattern != "":
			symbol = pattern[-1]
			pattern = pattern[: -1]
			# print("ss", occ_counts_before[symbol][top])
			if symbol not in bwt[top: bottom + 1]:
				return 0
			top = starts[symbol] + occ_counts_before[symbol][top]
			bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] - 1
		else:
			# print("res", top, bottom - 1)
			return bottom - top + 1
	return 0


def run_tests():
	files = get_files()
	files.sort(key=lambda x: x[-1])
	for f in files:
		with open(f, 'r') as fs:
			text = fs.read().strip()
		data = text.split("\n")
		bwt = data[0]
		patterns = data[2].split()
		# Preprocess the BWT once to get starts and occ_count_before.
		# For each pattern, we will then use these precomputed values and
		# spend only O(|pattern|) to find all occurrences of the pattern
		# in the text instead of O(|pattern| + |text|).
		starts, occ_counts_before = PreprocessBWT(bwt)
		occurrence_counts = []
		for pattern in patterns:
			occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
		print(' '.join(map(str, occurrence_counts)))
		

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
	pattern_count = int(sys.stdin.readline().strip())
	patterns = sys.stdin.readline().strip().split()
	# Preprocess the BWT once to get starts and occ_count_before.
	# For each pattern, we will then use these precomputed values and
	# spend only O(|pattern|) to find all occurrences of the pattern
	# in the text instead of O(|pattern| + |text|).
	starts, occ_counts_before = PreprocessBWT(bwt)
	occurrence_counts = []
	for pattern in patterns:
		occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
	print(' '.join(map(str, occurrence_counts)))


if __name__ == '__main__':
	main()
	# run_tests()
