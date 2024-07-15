import heapq
import time
import tracemalloc

# Uniform Cost Search algorithm
class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        # Priority queue to store nodes to be explored, starting with the initial node and cost of 0
        frontier = []
        heapq.heappush(frontier, (0, start))

        # Frequency count of node visits
        visit_count = {start: 1}

        # Track the maximum size of the priority queue
        max_frontier_size = 0

        # Store the cost to reach each node
        cost_so_far = {start: 0}
        # Store the path taken to reach each node
        came_from = {start: None}

        # Store all visited nodes
        visited_order = []

        while frontier:
            # Track the maximum size of the priority queue
            max_frontier_size = max(max_frontier_size, len(frontier))

            # Pop the node with the lowest cost from the priority queue
            current_cost, current_node = heapq.heappop(frontier)
            # Record the current node as visited
            visited_order.append(current_node)

            # If the current node is the goal, reconstruct the path and return it
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                return visited_order, cost_so_far[goal], path[::-1], len(visited_order), max_frontier_size, visit_count

            # Explore neighbors of the current node
            for neighbor, cost in self.graph[current_node].items():
                # Calculate the new cost to reach the neighbor
                new_cost = current_cost + cost
                neighbor_cost = cost_so_far.get(neighbor, float('inf'))

                # If this path to the neighbor is cheaper, update cost and path
                if new_cost < neighbor_cost:
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(frontier, (new_cost, neighbor))
                    came_from[neighbor] = current_node
                    visit_count[neighbor] = visit_count.get(neighbor, 0) + 1

        # If the goal is not reachable, return the visited order, infinity as cost, and an empty path
        return visited_order, float('inf'), [], len(visited_order), max_frontier_size, visit_count

# Define a new graph with Metro Manila cities and connections
metro_manila_graph = {
    "Makati": {"Taguig": 5, "Pasay": 3, "Mandaluyong": 6},
    "Taguig": {"Makati": 5, "Pasig": 7},
    "Pasay": {"Makati": 3, "Paranaque": 4},
    "Mandaluyong": {"Makati": 6, "San Juan": 4, "Quezon City": 10},
    "Pasig": {"Taguig": 7, "Marikina": 5, "Quezon City": 8},
    "San Juan": {"Mandaluyong": 4, "Quezon City": 5},
    "Quezon City": {"Mandaluyong": 10, "San Juan": 5, "Pasig": 8, "Marikina": 7},
    "Marikina": {"Pasig": 5, "Quezon City": 7},
    "Paranaque": {"Pasay": 4}
}

# Create UniformCostSearch instance with the new graph
ucs = UniformCostSearch(metro_manila_graph)

# Function to get user input for start and end cities
def get_user_input():
    start_city = input("Enter the start city: ").strip()
    end_city = input("Enter the end city: ").strip()
    return start_city, end_city

# Example usage
def main():
    start_city, end_city = get_user_input()
    
    if start_city not in metro_manila_graph or end_city not in metro_manila_graph:
        print("Invalid city names. Please enter valid city names from the graph.")
        return
    
    # Measure time before executing the algorithm
    start_time = time.time()
    tracemalloc.start()  # Start memory tracking
    
    visited_order, total_cost, path, nodes_expanded, max_frontier_size, visit_count = ucs.search(start_city, end_city)
    
    # Measure time after executing the algorithm
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    path_str = " -> ".join(path)
    visited_str = " -> ".join(visited_order)
    
    result_text = (
        f"Final Path: {path_str}\n"
        f"Path Traversed: {visited_str}\n"
        f"Total Cost: {total_cost}\n"
        f"Time: {end_time - start_time:.4f} seconds\n"
        f"Nodes Expanded: {nodes_expanded}\n"
        f"Max Frontier Size: {max_frontier_size}\n"
        f"Memory Usage: Current={current / 1024:.2f}KB, Peak={peak / 1024:.2f}KB\n"
        f"Visit Count: {visit_count}"
    )
    
    print(result_text)

if __name__ == "__main__":
    main()
