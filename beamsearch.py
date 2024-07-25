class BeamSearch:
    def __init__(self, distances, beta):
        self.distances = distances
        self.beta = beta

    def search(self):
        paths_so_far = [[list(), 0]]
        max_frontier_size = 0
        all_paths = []
        visit_count = {}
        visited_order = []

        for idx, tier in enumerate(self.distances):
            if idx > 0:
                print(f'Paths kept after tier {idx-1}:')
                print(*paths_so_far, sep='\n')

            paths_at_tier = []

            for path, distance in paths_so_far:
                for j, cost in enumerate(tier):
                    path_extended = [path + [j], distance + cost]
                    paths_at_tier.append(path_extended)

            paths_ordered = sorted(paths_at_tier, key=lambda element: element[1])

            max_frontier_size = max(max_frontier_size, len(paths_ordered))
            all_paths.append(paths_ordered)
            
            paths_so_far = paths_ordered[:self.beta]
            visited_order.extend(paths_so_far)
            for path, _ in paths_so_far:
                for node in path:
                    visit_count[node] = visit_count.get(node, 0) + 1

            print(f'\nPaths reduced to after tier {idx}: ')
            print(*paths_ordered[self.beta:], sep='\n')

        final_path = paths_so_far[0][0]
        total_cost = paths_so_far[0][1]
        nodes_expanded = len(visited_order)

        return visited_order, total_cost, final_path, nodes_expanded, max_frontier_size, visit_count
