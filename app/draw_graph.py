from turtle import color
from PIL import Image

import io
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(leave_nodes, arrive_nodes, nodes_weight, nodes_number, visitable_showplaces):

    G=nx.DiGraph()

    trace = [(visitable_showplaces[i-1], visitable_showplaces[i]) for i in range(1, len(visitable_showplaces))]

    for node in range(1, nodes_number+1):
        print(node)
        G.add_node(node)

    edge_labels = dict()

    for k in range(len(leave_nodes)):
        i = leave_nodes[k]
        j = arrive_nodes[k]
        w = nodes_weight[k]

        edge_labels[(i, j)] = w


        if (i, j) not in trace:
            G.add_edge(i, j, color='r', weight=w, arrowstyle='->', arrowsize=10)
        else:
            G.add_edge(i, j, color='g', weight=w, arrowstyle='->', arrowsize=10)


    colors = nx.get_edge_attributes(G,'color').values()

    pos = nx.planar_layout(G)
    nx.draw(G, pos, edge_color=colors, width=2, with_labels=True, arrowstyle="->", arrowsize=10, edge_cmap=plt.cm.Reds)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

    buf = io.BytesIO()
    buf_test = open("test.png", "wb")
    plt.savefig(buf, format='png')
    plt.savefig(buf_test, format='png')
    buf.seek(0)
    plt.close()

    return buf


if __name__ == "__main__":

    from_place = [1, 2, 2]
    to_place = [2, 3, 4]
    width = [5, 7, 8]
    visitable_showplaces = [1, 2, 4]

    max_time = 13
    nodes_number = 4

    # from_place = [1, 1, 3, 2, 4, 6]
    # to_place = [2, 3, 6, 4, 6, 5]
    # width = [2, 3, 3, 2, 2, 1]

    # max_time = 7
    # nodes_number = 6

    # from_place = [1, 3, 1, 2, 4]
    # to_place = [3, 5, 2, 4, 5]
    # width = [3, 3, 2, 3, 2]

    # max_time = 6
    # nodes_number = 5

    print(draw_graph(from_place, to_place, width, nodes_number, visitable_showplaces))