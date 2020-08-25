import gzip, pickle, pickletools
import os

global globalPath
globalPath = "/".join(os.path.realpath(__file__).split('/')[:-2])+'/'


def save_obj_fast(obj, name, path = globalPath+'res/'):
	"""
		save_obj_fast(obj, name, path = globalPath+'res/')
	"""

	with gzip.open(path + name + '.pkl', 'wb') as f:
		pickled = pickle.dumps(obj)
		optimized_pickle = pickletools.optimize(pickled)
		f.write(optimized_pickle)

def load_obj_fast(name, path = globalPath+'res/'):
	"""
		load_obj_fast(name, path = globalPath+'res/')	
	"""

	with gzip.open(path + name + '.pkl', 'rb') as f:
		p = pickle.Unpickler(f)
		return p.load()


def save_obj(obj, name, path = globalPath+'res/'):
	"""
		save_obj(obj, name, path = globalPath+'res/')

	"""
	with open( path + name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name, path = globalPath+'res/' ):
	"""
		load_obj(name, path = globalPath+'res/' )
	"""

	with open( path + name + '.pkl', 'rb') as f:
		return pickle.load(f)

def printVars(thing):
	print(thing)
	for el in vars(thing):
		print('\t',el)

def printList(lst):
	if not lst:
		return
	if not isinstance(lst,list):
		lst = list(lst)
	for el in lst:
		print('\t',el)

def printToFile(obj, name):
	f = open(globalPath + "output/" + name +" .txt","w+")
	if isinstance(obj,dict):
		for key, value in obj.items():
			f.write(str(key)+'\n')
			if isinstance(value,list):
				for elem in value:
					f.write('\t'+str(elem)+'\n')
			else:
				f.write('\t'+str(value)+'\n')
		return
	for i in obj:
		if isinstance(i,list):
			f.write(str(i[0])+'\n')
			for el in i[1:]:
				f.write('\t'+str(el)+'\n')
			f.write('\n')
		else:
			f.write(str(i)+'\n')
	f.close