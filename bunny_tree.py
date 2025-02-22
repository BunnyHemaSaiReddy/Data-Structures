import networkx as nx
import  matplotlib.pyplot as plt
#import networkx.drawing.nx_agraph as nx_graph

def di_draw_tree(relations):
    g=nx.DiGraph()
    g.add_edges_from(relations)
    pos=nx.spring_layout(g)
    #pos=nx_graph.graphviz_layout(g,prog='dot')
    nx.draw(g,pos,with_labels=True)
    plt.show()
    return 'done'
def draw_tree(relations,k=None):
    g=nx.Graph()
    g.add_edges_from(relations)
    pos=nx.spring_layout(g,k=None)
    #pos=nx_graph.graphviz_layout(g,prog='dot')
    nx.draw(g,pos,with_labels=True)
    plt.show()
    return 'done'
def draw_tree_weighted(relations,k=None):
    G=nx.Graph()
    G.add_weighted_edges_from(relations)
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif") 
    plt.show()
    return 'done'
#print(draw_tree([('d', 'c'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'a'), ('e', 'b')]))