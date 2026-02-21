#>------------///DICTIONARIES
# Problem: Count the frequency of each number in a list
data = [1, 2, 2, 3, 1, 4, 2]
counts = {}

for num in data:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Output: {1: 2, 2: 3, 3: 1, 4: 1}
print(counts)

#>------------/// STACK
# Stack (using a simple list)
stack = []
stack.append("A")  # Push
stack.append("B")
item = stack.pop() # Removes "B" (the last one in)

# Queue (using collections.deque for efficiency)
from collections import deque
queue = deque(["A", "B"])
queue.append("C")      # Enqueue
first = queue.popleft() # Removes "A" (the first one in)

#>------------///BREADTH FIRST SEARCH
from collections import deque

def bfs(graph, start_node):
    visited = {start_node}
    queue = deque([start_node])
    
    while queue:
        current = queue.popleft()
        print(f"Visiting {current}")
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an Adjacency List
graph = { 'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': [] }
bfs(graph, 'A')

#>------------///
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(node)
    print(f"Visiting {node}")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Using the same graph as above
dfs(graph, 'A')

#>------------///
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found it!
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 # Not found

sorted_list = [10, 20, 30, 40, 50]
print(binary_search(sorted_list, 40)) # Output: 3