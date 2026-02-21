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
# HOW IT WORKS: Uses a hash table to jump directly to a memory location.
    # WHEN TO USE: Frequency counting, memoization (DP), or mapping IDs to names.
    # COMPLEXITY: O(1) average for inserts and lookups.

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
# --- STACK (LIFO: Last-In, First-Out) ---
    # HOW IT WORKS: Like a stack of pancakes; you only interact with the top.
    # WHEN TO USE: Reversing data, matching parentheses, or DFS.
    # COMPLEXITY: O(1) for append/pop.

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
    # HOW IT WORKS: Uses a QUEUE to explore neighbors level-by-level.
    # WHEN TO USE: Finding the SHORTEST path in unweighted graphs/grids.
    # COMPLEXITY: O(V + E) where V is vertices and E is edges.

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
# HOW IT WORKS: Uses RECURSION (or a Stack) to go deep before wide.
    # WHEN TO USE: Checking connectivity, solving puzzles/mazes, or exhaustive search.
    # COMPLEXITY: O(V + E).

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
# HOW IT WORKS: Looks at the middle; if the target is smaller, 
    # discard the right half. If larger, discard the left half.
    # WHEN TO USE: Fast searching in sorted arrays or "Binary Search on Answer."
    # COMPLEXITY: O(log n).