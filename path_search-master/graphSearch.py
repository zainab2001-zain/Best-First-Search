

from pathsearch_class import *
from build_world import plot_visited_point
import math

#SHORTEST DISTANCE BETWEEN 2 POINTS
def euclidean_distance(current,goal):
    return math.sqrt(math.pow(current[0]-goal[0],2)+math.pow(current[1]-goal[1],2))

def greedy_search(graph, start, goal, ax, ann_iterate, animation):
    search_iterate = True #give boolean value
    num_iterate = 0 #initialize it zero
    graph.Nodes[start[0]][start[1]].distance = 0
    visited_queue = PriorityQueue()
    visited_queue.put(start, 0)

    while not visited_queue.empty():
        num_iterate = num_iterate+1
        current = visited_queue.get()
        graph.Nodes[current[0]][current[1]].visited = True
        graph.Nodes[current[0]][current[1]].queued = False
        if current == goal:
            search_iterate = False
            break
        for nb in graph.neighbors(current):
            if not graph.Nodes[nb[0]][nb[1]].visited:
                if not graph.Nodes[nb[0]][nb[1]].queued:
                    graph.Nodes[nb[0]][nb[1]].queued = True
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].priority = euclidean_distance(nb,goal)
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].priority)
                elif graph.Nodes[nb[0]][nb[1]].distance > graph.Nodes[current[0]][current[1]].distance + 1:
                    graph.Nodes[nb[0]][nb[1]].distance = graph.Nodes[current[0]][current[1]].distance + 1
                    graph.Nodes[nb[0]][nb[1]].priority = euclidean_distance(nb,goal)
                    graph.Nodes[nb[0]][nb[1]].parent = graph.Nodes[current[0]][current[1]]
                    visited_queue.put(nb,graph.Nodes[nb[0]][nb[1]].priority)
        if animation:
            plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    if not search_iterate:
        flag = 'Successful'
        ax = plot_visited_point(graph, num_iterate, visited_queue.len(), ax, ann_iterate)
    else:
        flag = 'Failed'
    return flag, graph, ax

switch_search_method = {
    'Greedy': greedy_search
}
