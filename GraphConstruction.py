import networkx as nx
import matplotlib.pyplot as plt

# Construct graph function
def construct_graph(preprocessed_text):
    # Split preprocessed text into words
    words = preprocessed_text.split()

    # Construct directed graph
    G = nx.DiGraph()

    # Add nodes to the graph for each unique word
    for word in set(words):
        G.add_node(word)

    # Add edges to the graph based on the sequential order of words in the text
    for i in range(len(words) - 1):
        source = words[i]
        target = words[i + 1]
        if not G.has_edge(source, target):
            G.add_edge(source, target, weight=1)
        else:
            G[source][target]['weight'] += 1

    return G


def visualize_graph(graph):
    # Draw the graph
    pos = nx.spring_layout(graph)  # Position nodes using the Fruchterman-Reingold force-directed algorithm
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray", linewidths=0.5, arrows=True)

    # Display the graph
    plt.title("Graph Visualization")
    plt.show()
