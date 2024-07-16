import time
import tracemalloc
from UCS import UniformCostSearch
from AStar import AStarSearch

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

# Define heuristic values for each city
heuristic_values = {
    "Makati": 10, "Taguig": 8, "Pasay": 6, "Mandaluyong": 7, "Pasig": 3,
    "San Juan": 4, "Quezon City": 2, "Marikina": 1, "Paranaque": 9
}

# Function to display the cities and their heuristic values
def display_cities_and_heuristics():
    print("Cities and their heuristic values:")
    for city, heuristic in heuristic_values.items():
        print(f"{city}: {heuristic}")

# Function to display the graph in a simple format
def display_graph(graph):
    print("\nGraph connections:")
    for city, connections in graph.items():
        connections_str = ", ".join(f"{neighbor}({cost})" for neighbor, cost in connections.items())
        print(f"{city} -> {connections_str}")

# Function to get user input for start and end cities
def get_user_input():
    start_city = input("\n\nEnter the start city: ").strip()
    end_city = input("Enter the end city: ").strip()
    return start_city, end_city

# Function to run the search and display results
def run_search(search_algorithm, start_city, end_city):
    start_time = time.time()
    tracemalloc.start()
    
    visited_order, total_cost, path, nodes_expanded, max_frontier_size, visit_count = search_algorithm.search(start_city, end_city)
    
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

def main():
    display_cities_and_heuristics()
    display_graph(metro_manila_graph)
    
    start_city, end_city = get_user_input()
    
    if start_city not in metro_manila_graph or end_city not in metro_manila_graph:
        print("Invalid city names. Please enter valid city names from the graph.")
        return
    
    print("\nUniform Cost Search:")
    ucs = UniformCostSearch(metro_manila_graph)
    run_search(ucs, start_city, end_city)
    
    print("\nA* Search:")
    a_star = AStarSearch(metro_manila_graph, heuristic_values)
    run_search(a_star, start_city, end_city)

if __name__ == "__main__":
    main()
