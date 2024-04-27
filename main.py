from GraphConstruction import construct_graph
from feature_extraction import frequent_subgraph_mining
from feature_extraction import extract_features

# Load preprocessed text data from file
file_path = "preprcessed_data/preprocessed_finance_train_data.txt"
with open(file_path, "r", encoding="utf-8") as file:
    preprocessed_data = file.read()

# Construct graph from preprocessed text data
graph1 = construct_graph(preprocessed_data)

file_path2 = "preprcessed_data/preprocessed_lifestyle_train_data.txt"
with open(file_path2, "r", encoding="utf-8") as file:
    preprocessed_data2 = file.read()

graph2 = construct_graph(preprocessed_data2)

file_path3 = "preprcessed_data/preprocessed_marketing_train_data.txt"
with open(file_path3, "r", encoding="utf-8") as file:
    preprocessed_data3 = file.read()

graph3 = construct_graph(preprocessed_data3)

# frequent subgraph mining on training set graphs
training_graphs = [graph1,graph2,graph3]  # a list of training set graphs
frequent_subgraphs = frequent_subgraph_mining(training_graphs)

# Extract features from training set graphs
feature_matrix = extract_features(training_graphs, frequent_subgraphs)