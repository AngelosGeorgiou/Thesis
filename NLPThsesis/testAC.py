import ahocorasick as ac
from  printModule import load_obj


A = load_obj('ahocorasickStruct')

A.get('liver')

# haystack = line
# for end_index, (insert_order, original_value) in A.iter(haystack):
# 	start_index = end_index - len(original_value) + 1
# 	print((start_index, end_index, (insert_order, original_value)))
	# assert haystack[start_index:start_index + len(original_value)] == original_value