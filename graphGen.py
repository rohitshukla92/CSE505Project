#!/usr/bin/env python

import random
import string

#DAG with no weights of the edges
#nodes of the graphs 26 
nodes=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#edges between 20 of the nodes
edges=[]
for i in range(0,20):
	x=random.choice(string.ascii_uppercase)
	y=random.choice(string.ascii_uppercase)
	if(x!=y):
		edges.append((x,y))

print(edges)

#DAG with random weights associated with each edge of the graph 

edges_with_weight=[]
for i in range(0,20):
	x=random.choice(string.ascii_uppercase)
	y=random.choice(string.ascii_uppercase)
	if(x!=y):
		edges_with_weight.append((x,y,random.randint(1,5)))

print("Edges with weights\n")
print(edges_with_weight)



