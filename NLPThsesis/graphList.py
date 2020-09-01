
import rdflib
import myUtilities as mu


class graphList(object):
	"""docstring for graphList"""
	def __init__(self, numOfheaders = 6):
		self.gList = []
		for i in range(0,numOfheaders+1):
			self.gList.append(mu.load_obj_fast("headers0"+str(i)))
					