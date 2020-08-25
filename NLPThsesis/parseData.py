from rdflib import Graph
import myUtilities as mu
import sys
sys.path.insert(1,"/home/angelos/Desktop/meshHeadings")

for i in range(0,10):
	g = Graph()
	g = g.parse("/home/angelos/Desktop/meshHeadings/headers0"+str(i),format='nt')
	print("Parsed",i)
	mu.save_obj_fast(g,"headers0"+str(i))
	print("Saved",i)