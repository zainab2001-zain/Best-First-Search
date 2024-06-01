

from graphSearch import *
from build_world import *
from map_example import *


def main():

    method = 'Greedy'
    scene = input('Please choose one scene from 1~4:\n')
    graph = switch_map[scene]

    animation = True

    start, goal = (5, 47), (46, 3)
    ax, ann_iterate, ann_path = plot_init_map_noclick(graph, method, start, goal)
    flag, graph_result, update_ax = switch_search_method[method](graph, start, goal, ax, ann_iterate, animation)
    if flag == 'Successful':
        path, path_length = reconstruct_path(graph_result, start, goal)
        plot_search_result(path, path_length, update_ax, ann_path)


if __name__ == '__main__':
    main()
