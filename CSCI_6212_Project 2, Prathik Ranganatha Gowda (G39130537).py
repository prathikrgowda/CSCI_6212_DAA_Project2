import random  #to import random module to generate random weights for the edges
import time #to import time module to calculate the time taken by the algortithm

class DisjointSet: #creates a class called disjoint set
    def __init__(self, nodes): #In which the constructor takes the number of nodes as the input
        self.n = nodes #the number of nodes in the graph
        self.edges = [] #list to store all the edges of the graph

    def addEdge(self, source, destination, weight): #this method adds an edge to the graph
        self.edges.append([source, destination, weight]) #adds the edge to the graph

    def find(self, parent, i): #this method finds the root of the tree containing the given code
        if parent[i] == i: #to check if the parent of the given node is itself
            return i # If it is, then the given node is the root of its own tree and it returns it
        else:
            return self.find(parent, parent[i]) #else we recursively call the find() method on the parent of the given node. This process continues until we find a node whose parent is itself. That node is the root of the tree containing the given node, and we return it.

    def union(self, parent, rank, x, y): #this method merges two trees together containing nodes x and nodes y together.
        #It is done by setting the parent of the node with the lower rank to be the node with the higher rank.
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x
        #If the two nodes have the same rank, then we set the parent of the second node to be the first node and increase the rank of the first node by 1.
        else:
            parent[y] = x
            rank[x] += 1

    def MinimumSpanningTree(self): #this methos finds the minimum spanning tree for the graph
        start_time = time.time_ns() #starts the timer
        result = [] #to store the edges of the minimum spanning tree
        parent = [] #empty list to store the parent of each node in the graph
        rank = [] #empty list to store the rank of each node in the graph
        i, e = 0, 0 #i variable is used to iterate over the edges of the graph, e variable used to keep track of number of edges in the minimum spanning tree
        self.edges = sorted(self.edges, key=lambda item: item[2])  #sorts the edges in ascending order of their weights
        for node in range(self.n):
            parent.append(node) #initialize the parent array
            rank.append(0) #initialize the rank array
        while e < self.n - 1: #iterates over the edges in sorted order until the edges in the minimum spanning tree is one less than the number of nodes given as input
            source, destination, weight = self.edges[i]
            i += 1
            x = self.find(parent, source) #finds the root of the tree containing the source node
            y = self.find(parent, destination) #finds the root of the tree containing the destination node
            # checks if the source and destination are in the same tree, if they are not then merges the trees together and adds the edge to the minimum spanning tree
            if x != y:
                e = e + 1
                result.append([source, destination, weight]) #adding the edge to the minimum spanning tree
                self.union(parent, rank, x, y) #merges the trees together
        stop_time = time.time_ns() #stops the timer

        minimum_cost = 0 #variable to store the total weight of the minimum spanning tree
        print("the edges constituting the edges of the minimum spanning tree:\n")
        for source, destination, weight in result: #iterating through each edge in the minimum spanning tree to print them
            minimum_cost = minimum_cost + weight
            print("%d -- %d = %d" % (source, destination, weight)) #prints the edges of the minimum spanning tree
        print("minimum spanning tree weight: ", minimum_cost) #prints the total weight of the minimum spanning tree
        print("The time taken by the Kruskal's algorithm to find the minimum spanning tree:", stop_time - start_time) #prints the total time taken by the Kruskal's algorithm for finding the minimum spanning tree


#to generate a random graph of n nodes and m edges
nodes = 1000 #number of nodes(n)
edges = (nodes*(nodes-1))/2 #number of edges by the formula (n*(n-1))/2
print(edges)
count = 0 #to count the number of edges created
g = DisjointSet(nodes) #to create a disjoint object for the graph
for i in range(0, nodes):
    if (count == edges): #to create (n*(n-1))/2 edges in the graph
        break
    #to create random edges with random weights for the graph
    if i > 1:
        start = random.randint(0, i - 1)
    else:
        start = random.randint(i + 1, i + 5)
    stop = random.randint(i + 1, nodes)
    for j in range(start, stop):
        g.addEdge(i, j, random.randint(1, 50))
        count += 1

g.MinimumSpanningTree() #function call to find the minimum spanning tree using Kruskal's algorithm

