#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx

import heapq   # Import heapq for using a priority queue (min-heap)

# Create the graph with nodes and edge costs
graph = {
    'A': [('B', 1), ('C', 4)],   # A connects to B (1) and C (4)
    'B': [('D', 6)],             # B connects to D (6)
    'C': [('D', 1)],             # C connects to D (1)
    'D': []                      # D has no outgoing edges
}

# Heuristic (estimated cost to reach goal 'D')
h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

# Function to perform A* search
def a_star(start, goal):
    pq = [(h[start], 0, [start])]   # Priority queue → (f, g, path)

    while pq:                       # Run until queue is empty
        f, g, path = heapq.heappop(pq)  # Remove node with smallest f value
        node = path[-1]                 # Current node is last in path

        if node == goal:               # If goal reached
            return path, g             # Return path and cost

        # Check all neighbors of current node
        for neighbor, cost in graph[node]:
            g_new = g + cost           # Update actual cost
            f_new = g_new + h[neighbor]# Calculate total estimated cost
            heapq.heappush(pq, (f_new, g_new, path + [neighbor])) # Add neighbor to queue

    return [], float('inf')            # If goal not found, return empty path

# Take user inputs and convert to uppercase
s = input("Start node: ").upper()
g = input("Goal node: ").upper()

# Run the A* algorithm
path, cost = a_star(s, g)

# Display final shortest path and cost
print("Shortest Path:", ' → '.join(path))
print("Total Cost:", cost)

'''
Actual cost (g) → the distance traveled so far
Heuristic (h) → estimated cost to reach the goal
f = g + h → total estimated cost

'''



'''PS C:\Users\LENOVO\OneDrive\Desktop\SEM7\AINLP\AI> & C:/Users/LENOVO/AppData/Local/Programs/Python/Python313/python.exe c:/Users/LENOVO/OneDrive/Desktop/SEM7/AINLP/AI/A2Astar.py
>>
Start node: A
Goal node: D
Shortest Path: A → C → D
Total Cost: 5'''