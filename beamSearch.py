class BeamSearch:
    def __init__(self, graph, heuristic_values, beam_width):
        self.graph = graph
        self.heuristic_values = heuristic_values
        self.beam_width = beam_width

    def search(self, start_city, end_city):
        # Initialize the frontier with the start city
        frontier = [(start_city, 0)]
        visited_order = []
        nodes_expanded = 0
        max_frontier_size = 1
        visit_count = {city: 0 for city in self.graph}

        while frontier:
            # Sort the frontier based on the heuristic values and limit its size to the beam width
            frontier.sort(key=lambda x: self.heuristic_values[x[0]], reverse=True)
            frontier = frontier[:self.beam_width]

            # Pop the city with the highest heuristic value from the frontier
            current_city, current_cost = frontier.pop(0)
            visited_order.append(current_city)
            visit_count[current_city] += 1

            # If the current city is the end city, return the results
            if current_city == end_city:
                return visited_order, current_cost, visited_order, nodes_expanded, max_frontier_size, visit_count

            # Expand the current city
            nodes_expanded += 1
            for neighbor, cost in self.graph[current_city].items():
                if neighbor not in visited_order:
                    frontier.append((neighbor, current_cost + cost))

            # Update the maximum frontier size
            max_frontier_size = max(max_frontier_size, len(frontier))

        # If no path is found, return None
        return None
