from numpy import array
 
def beam_search(distances, beta):
    #initialising some record
    paths_so_far = [[list(), 0]]  
  
     
    #traverse through the neighbouring vertices row by row.
    for idx, tier in enumerate(distances):
        if idx > 0:
            print(f'Paths kept after tier {idx-1}:')
            print(*paths_so_far, sep='\n')
        paths_at_tier = list()
         
 
        for i in range(len(paths_so_far)):
            path, distance = paths_so_far[i]
             
            # Extending the paths
            for j in range(len(tier)):
                path_extended = [path + [j], distance + tier[j]]
                paths_at_tier.append(path_extended)
                 
        paths_ordered = sorted(paths_at_tier, key=lambda element: element[1])
         
        # The best paths are saved
        paths_so_far = paths_ordered[:beta]
        print(f'\nPaths reduced to after tier {idx}: ')
        print(*paths_ordered[beta:], sep='\n')
         
    return paths_so_far