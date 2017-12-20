#!/usr/bin/env python

import random
import string

#DAG with no weights of the edges
#nodes of the graphs 26 

print("Graph with 20 nodes\n")
print("Nodes\n")
nodes=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(nodes)
print("\n")

print("Edges\n")
#edges between 20 of the nodes
edges=[]
for i in range(0,20):
	x=random.choice(string.ascii_uppercase)
	y=random.choice(string.ascii_uppercase)
	if(x!=y):
		edges.append((x,y))
print(edges)
print("\n")

#DAG with random weights associated with each edge of the graph 
#Weight associated with each graph is a value between 1 to 5 

edges_with_weight=[]
for i in range(0,20):
	x=random.choice(string.ascii_uppercase)
	y=random.choice(string.ascii_uppercase)
	if(x!=y):
		edges_with_weight.append((x,y,random.randint(1,5)))
print("Edges with weights\n")
print(edges_with_weight)
print("\n")

#Generating a graph with 100 nodes and corresponding edges with in it. 
#Nodes
print("Graph with 100 nodes\n")
print("Nodes\n")
Nodes=[]
for i in range(1,101):
	Nodes.append(str(i))
print(Nodes)
print("\n")

print("Edges\n")
#edges between 50 of the nodes 
Edges=[]
for i in range(0,50):
	a=str(random.randint(1,101))
	b=str(random.randint(1,101))
	if(a!=b):
		Edges.append((a,b))
print(Edges)
print("\n")

print("Edges with weight\n")
Edges_with_weight=[]
for i in range(0,50):
	u=str(random.randint(1,101))
	v=str(random.randint(1,101))
	if(u!=v):
		Edges_with_weight.append((u,v,random.randint(1,5)))
print(Edges_with_weight)
print("\n")






