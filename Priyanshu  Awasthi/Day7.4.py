
def Sort_Tuple(tup):

	tup.sort(key = lambda x: x[-1])
	return tup

tup = [(1, 3), (3, 2), (2, 1)]
print(Sort_Tuple(tup))
