# Problem 1: Get Flight Cost

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we find the minimum cost path or just any valid path?
   Q2: How should we handle cycles in the flight network?

2. Write out in plain English what you want to do: 

   I want to find the cost of any path from start to destination using BFS.
   I'll use a queue to explore flights level by level, tracking the cumulative cost.
   I'll maintain a visited set to avoid revisiting locations and return the first
   valid path cost I find, or -1 if no path exists.

3. Translate each sub-problem into pseudocode:

   Use BFS with queue storing (location, cumulative_cost)
   Track visited locations to avoid cycles
   Return cost when destination is reached

   queue <- deque with (start, 0)
   visited <- empty set
   while queue is not empty do
       curr_location, curr_cost <- queue.popleft()
       add curr_location to visited
       if curr_location == dest then
           return curr_cost
       for neighbor_location, neighbor_cost in flights.get(curr_location, []) do
           if neighbor_location not in visited then
               queue.append((neighbor_location, curr_cost + neighbor_cost))
   return -1

4. Translate the pseudocode into Python and share your final answer:

   def calculate_cost(flights, start, dest):
       from collections import deque
       visited = set()
       queue = deque([(start, 0)])

       while queue:
           curr_location, curr_cost = queue.popleft()
           if curr_location in visited:  # Fixed: check visited before processing
               continue
           visited.add(curr_location)
           if curr_location == dest:
               return curr_cost
           
           for neighbor_location, neighbor_cost in flights.get(curr_location, []):
               if neighbor_location not in visited:
                   queue.append((neighbor_location, curr_cost + neighbor_cost))
       return -1
"""

# Problem 2: Expanding Flight Offerings

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we count components by treating the graph as undirected?
   Q2: How do we efficiently count connected components without modifying the input?

2. Write out in plain English what you want to do: 

   I want to count the number of connected components in the flight network.
   The minimum flights needed equals (number of components - 1) since we need
   one edge to connect each pair of components. I'll use DFS to explore each
   component and count how many separate groups exist.

3. Translate each sub-problem into pseudocode:

   Count connected components using DFS
   Return (components - 1) as minimum edges needed

   num_components <- 0
   visited <- empty set
   function dfs(curr):
       add curr to visited
       for neighbor in flights.get(curr, []) do
           if neighbor not in visited then
               dfs(neighbor)
   
   for each location in flights do
       if location not in visited then
           dfs(location)
           increment num_components
   return num_components - 1

4. Translate the pseudocode into Python and share your final answer:

   def min_flights_to_expand(flights):
       num_components = 0
       visited = set()

       def dfs(curr):
           visited.add(curr)
           for neighbor in flights.get(curr, []):
               if neighbor not in visited:
                   dfs(neighbor)

       for location in flights:
           if location not in visited:
               dfs(location)
               num_components += 1
       
       return num_components - 1
"""

# Problem 3: Get Flight Itinerary

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we return the shortest path or any valid path?
   Q2: How do we reconstruct the path during our search?

2. Write out in plain English what you want to do: 

   I want to find any path from source to destination using DFS with backtracking.
   I'll maintain a current path and visited set, exploring each neighbor recursively.
   When I reach the destination, I'll return the current path. If a path doesn't work,
   I'll backtrack by removing the node from both the path and visited set.

3. Translate each sub-problem into pseudocode:

   Use DFS with path reconstruction and backtracking
   Track current path and visited nodes
   Backtrack when dead ends are reached

   function dfs_helper(curr, visited, path):
       if curr == dest then
           return copy of path
       for neighbor in flights.get(curr, []) do
           if neighbor not in visited then
               add neighbor to path and visited
               result <- dfs_helper(neighbor, visited, path)
               if result then return result
               remove neighbor from visited and path
       return None

4. Translate the pseudocode into Python and share your final answer:

   def get_itinerary(flights, source, dest):
       def dfs_helper(curr, visited, path):
           if curr == dest:
               return path.copy()
           
           for neighbor in flights.get(curr, []):
               if neighbor not in visited:
                   path.append(neighbor)
                   visited.add(neighbor)
                   res = dfs_helper(neighbor, visited, path)
                   if res:
                       return res
                   visited.remove(neighbor)
                   path.pop()
           return None
       
       return dfs_helper(source, {source}, [source])
"""

# Problem 4: Pilot Training

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: How do we detect cycles in the prerequisite dependencies?
   Q2: Should we check all courses or only those with prerequisites?

2. Write out in plain English what you want to do: 

   I want to detect if there are any cycles in the course prerequisite graph.
   If there's a cycle, it's impossible to complete all courses. I'll use DFS with
   three states: unvisited, currently visiting (in recursion stack), and completely visited.
   If I encounter a node that's currently being visited, there's a cycle.

3. Translate each sub-problem into pseudocode:

   Build adjacency list from prerequisites
   Use DFS with cycle detection using three states
   Return False if any cycle is found

   adj_list <- build from flight_prerequisites
   visited <- empty set
   visiting <- empty set (recursion stack)
   
   function dfs(curr):
       if curr in visiting then return False (cycle detected)
       if curr in visited then return True
       add curr to visiting
       for prereq in adj_list.get(curr, []) do
           if not dfs(prereq) then return False
       remove curr from visiting
       add curr to visited
       return True

4. Translate the pseudocode into Python and share your final answer:

   def can_complete_flight_training(num_courses, flight_prerequisites):
       from collections import defaultdict
       adj_list = defaultdict(list)

       for course, prereq in flight_prerequisites:
           adj_list[course].append(prereq)
       
       visited = set()
       visiting = set()

       def dfs(curr):
           if curr in visiting:
               return False
           if curr in visited:
               return True
           
           visiting.add(curr)
           for prereq in adj_list.get(curr, []):
               if not dfs(prereq):
                   return False
           visiting.remove(curr)
           visited.add(curr)
           return True
       
       for course in adj_list.keys():
           if not dfs(course):
               return False
       
       return True
"""

# Problem 5: Reorient Flight Routes

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: How do we determine which edges need to be reoriented during traversal?
   Q2: Should we traverse from airport 0 to count misdirected edges?

2. Write out in plain English what you want to do: 

   I want to count how many edges need to be reoriented so all airports can reach airport 0.
   I'll create both directed and undirected representations of the graph. Using DFS from airport 0,
   I'll traverse the undirected graph and count edges that go away from airport 0 (need reorienting).
   An edge needs reorienting if (neighbor, current) is not in the original directed edges.

3. Translate each sub-problem into pseudocode:

   Create directed edge set and undirected adjacency list
   Use DFS from airport 0 to traverse tree
   Count edges that point away from airport 0

   directed_edges <- set of original connections
   undirected_adj_list <- build bidirectional adjacency list
   num_misdirections <- 0
   
   function dfs(curr):
       mark curr as visited
       for neighbor in undirected_adj_list.get(curr, []) do
           if neighbor not in visited then
               if (neighbor, curr) not in directed_edges then
                   increment num_misdirections
               dfs(neighbor)

4. Translate the pseudocode into Python and share your final answer:

   def min_reorient_flight_routes(n, connections):
       num_misdirections = 0
       directed_edges = set([(edge[0], edge[1]) for edge in connections])
       undirected_adj_list = {num: [] for num in range(n)}

       for edge in connections:
           u, v = edge
           undirected_adj_list[u].append(v)
           undirected_adj_list[v].append(u)

       visited = set()
       def dfs(curr):
           nonlocal num_misdirections
           visited.add(curr)
           for neighbor in undirected_adj_list.get(curr, []):
               if neighbor not in visited:
                   if (neighbor, curr) not in directed_edges:
                       num_misdirections += 1
                   dfs(neighbor)
       
       dfs(0)
       return num_misdirections
"""