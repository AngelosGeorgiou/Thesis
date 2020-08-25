import ahocorasick as ac
import os
from  printModule import save_obj

globalPath = "/".join(os.path.realpath(__file__).split('/')[:-2])+'/'

A = ac.Automaton()

with open(globalPath + "res/headers00") as infile:
	for line in infile:
		for idx, key in enumerate(line.split()):
			A.add_word(key, (idx,key))

save_obj(A,"ahocorasickStruct")
# A.get('liver')
# haystack = line
# for end_index, (insert_order, original_value) in A.iter(haystack):
# 	start_index = end_index - len(original_value) + 1
# 	print((start_index, end_index, (insert_order, original_value)))
	# assert haystack[start_index:start_index + len(original_value)] == original_value