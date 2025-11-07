# & "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx
# Initialize an empty dictionary to store the graph
graph = {}

n = int(input("Enter number of nodes: "))

# Loop to take input for each node and its neighbours
for _ in range(n):
    k = input("Node: ")  # Node name
    v = input("Neighbours (comma separated): ").split(',')  # Neighbours separated by commas
    graph[k] = [x for x in v if x]  # Store node and its neighbours in the graph dictionary

# Take the starting node for BFS traversal
start = input("Start node: ")

# Initialize an empty list to keep track of visited nodes
visited = []

# Initialize a queue with the start node (BFS uses a queue)
queue = [start]

# BFS traversal begins
while queue:
    node = queue.pop(0)  # Remove the first element from the queue (FIFO)
    
    if node not in visited:  # Process only if the node has not been visited yet
        print(node, end=" ")  # Print the current node
        visited.append(node)  # Mark it as visited
        
        # Add all unvisited neighbours to the queue
        for neigh in graph.get(node, []):
            if neigh not in visited:
                queue.append(neigh)


'''
OUTPUT
Enter number of nodes: 4
Node: a
Neighbours (comma separated): b,c
Node: b
Neighbours (comma separated): d
Node: c
Neighbours (comma separated): d
Node: d
Neighbours (comma separated): 
Start node: a
a b c d 
It takes the graph input from the user, then prints the order in which nodes are visited starting from a given node.
AI,GAME DEVELOPMENT,ROBOTICS,EDUCATION
'''