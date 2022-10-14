from networkx import draw, DiGraph, spring_layout
import matplotlib.pyplot as plt

g = DiGraph()
# out = [[('A', 'C')], [('B', 'C')], [('C', 'D')], [('C', 'E')], [('D', 'E')]]
# out = [[("socks", "shoes")],
#        [("shirt", "belt")],
#        [("shirt", "tie")],
#        [("tie", "jacket")],
#        [("belt", "jacket")],
#        [("pants", "shoes")],
#        [("underpants", "pants")],
#        [("pants", "belt")]]
# out = [[('1','2')],[('1','4')],[('2','3')],[('4','2')],[('4','6')],[('4','5')],[('5','6')]]
out = [[('a', 'c')], [('a', 'b')], [('b', 'd')], [('c', 'd')], [('c', 'f')], [('b', 'e')], [('e', 'f')]]


# g.add_edges_from([('A', 'C'), ('B', 'C')])
def anime(graph, connections):
    fig = plt.figure(figsize=(10, 6))
    plt.title("directed acyclic graph")
    ind = (len(connections) - 1)
    for i in range(ind):
        graph.add_edges_from(connections[i])
        pos = spring_layout(graph)
        # draw(g, with_labels=1)
        draw(
            graph, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='pink', alpha=0.9,
            labels={node: node for node in graph.nodes()}
        )
        plt.title("Directed Acyclic Graph")
        plt.show(block=False)
        plt.pause(2)
        plt.clf()
    graph.add_edges_from(connections[ind])
    pos = spring_layout(graph)
    draw(
        graph, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', alpha=0.9,
        labels={node: node for node in graph.nodes()}
    )
    plt.show(block=False)
    plt.pause(60)
    plt.clf()
    plt.close()


anime(g, out)
# next_out = ["underpants", "pants", "shirt", "tie", "belt", "jacket", "socks", "shoes"]
# next_out = ['B', 'A', 'C', 'D', 'E']
# next_out = ['1', '4', '5', '6', '2', '3']
next_out = ['a', 'b', 'e', 'c', 'f', 'd']
visited = []
redundanti = []
redundantj = []
for i in range(len(next_out)):
    for j in range(i, len(next_out)):
        if [(next_out[i], next_out[j])] in out and [(next_out[i], next_out[j])] not in visited and (
                next_out[i] not in redundanti or next_out[j] not in redundantj):
            visited.append([(next_out[i], next_out[j])])
            redundanti.append(next_out[i])
            redundantj.append(next_out[j])
            i = j
print(visited)
x = DiGraph()
anime(x, visited)
