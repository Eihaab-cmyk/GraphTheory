from GraphConstruction import construct_graph
from GraphConstruction import visualize_graph
from feature_extraction import frequent_subgraph_mining
from feature_extraction import extract_features
from knn_classification import knn_classify

# function to construct graph
def construct(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
      preprocessed_data = file.read()

   # Construct graph from preprocessed text data
    graph = construct_graph(preprocessed_data)

    return graph

# finance_train_graphs
finance_train_graph1 = construct("preprocessed_data/finance_train/preprocessed_finance_1_train_data.txt")
finance_train_graph2 = construct("preprocessed_data/finance_train/preprocessed_finance_2_train_data.txt")
finance_train_graph3 = construct("preprocessed_data/finance_train/preprocessed_finance_3_train_data.txt")
finance_train_graph4 = construct("preprocessed_data/finance_train/preprocessed_finance_4_train_data.txt")
finance_train_graph5 = construct("preprocessed_data/finance_train/preprocessed_finance_5_train_data.txt")
finance_train_graph6 = construct("preprocessed_data/finance_train/preprocessed_finance_6_train_data.txt")
finance_train_graph7 = construct("preprocessed_data/finance_train/preprocessed_finance_7_train_data.txt")
finance_train_graph8 = construct("preprocessed_data/finance_train/preprocessed_finance_8_train_data.txt")
finance_train_graph9 = construct("preprocessed_data/finance_train/preprocessed_finance_9_train_data.txt")
finance_train_graph10 = construct("preprocessed_data/finance_train/preprocessed_finance_10_train_data.txt")
finance_train_graph11 = construct("preprocessed_data/finance_train/preprocessed_finance_11_train_data.txt")
finance_train_graph12 = construct("preprocessed_data/finance_train/preprocessed_finance_12_train_data.txt")

#finance_test_graohs
finance_test_graph1 = construct("preprocessed_data/finance_test/preprocessed_finance_1_test_data.txt")
finance_test_graph2 = construct("preprocessed_data/finance_test/preprocessed_finance_2_test_data.txt")
finance_test_graph3 = construct("preprocessed_data/finance_test/preprocessed_finance_3_test_data.txt")

#lifestyle train graphs
lifestyle_train_graph1 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_1_train_data.txt")
lifestyle_train_graph2 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_2_train_data.txt")
lifestyle_train_graph3 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_3_train_data.txt")
lifestyle_train_graph4 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_4_train_data.txt")
lifestyle_train_graph5 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_5_train_data.txt")
lifestyle_train_graph6 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_6_train_data.txt")
lifestyle_train_graph7 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_7_train_data.txt")
lifestyle_train_graph8 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_8_train_data.txt")
lifestyle_train_graph9 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_9_train_data.txt")
lifestyle_train_graph10 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_10_train_data.txt")
lifestyle_train_graph11 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_11_train_data.txt")
lifestyle_train_graph12 = construct("preprocessed_data/lifestyle_train/preprocessed_Lifestyle_12_train_data.txt")

#lifestyle_test_graphs
lifestyle_test_graph1 = construct("preprocessed_data/lifestyle_test/preprocessed_Lifestyle_1_test_data.txt")
lifestyle_test_graph2 = construct("preprocessed_data/lifestyle_test/preprocessed_Lifestyle_2_test_data.txt")
lifestyle_test_graph3 = construct("preprocessed_data/lifestyle_test/preprocessed_Lifestyle_3_test_data.txt")

# Marketing train graphs
Marketing_train_graph1 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_1_train_data.txt")
Marketing_train_graph2 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_2_train_data.txt")
Marketing_train_graph3 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_3_train_data.txt")
Marketing_train_graph4 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_4_train_data.txt")
Marketing_train_graph5 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_5_train_data.txt")
Marketing_train_graph6 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_6_train_data.txt")
Marketing_train_graph7 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_7_train_data.txt")
Marketing_train_graph8 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_8_train_data.txt")
Marketing_train_graph9 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_9_train_data.txt")
Marketing_train_graph10 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_10_train_data.txt")
Marketing_train_graph11 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_11_train_data.txt")
Marketing_train_graph12 = construct("preprocessed_data/Marketing_train/preprocessed_Marketing_12_train_data.txt")

# Marketing test graphs
Marketing_test_graph1 = construct("preprocessed_data/Marketing_test/preprocessed_Marketing_1_test_data.txt")
Marketing_test_graph2 = construct("preprocessed_data/Marketing_test/preprocessed_Marketing_2_test_data.txt")
Marketing_test_graph3 = construct("preprocessed_data/Marketing_test/preprocessed_Marketing_3_test_data.txt")


#visualize the graph
#visualize_graph(graph1)

# frequent subgraph mining on training set graphs
training_graphs = [
   finance_train_graph1,
   finance_train_graph2,
   finance_train_graph3,
   finance_train_graph4,
   finance_train_graph5,
   finance_train_graph6,
   finance_train_graph7,
   finance_train_graph8,
   finance_train_graph9,
   finance_train_graph10,
   finance_train_graph11,
   finance_train_graph12,
   lifestyle_train_graph1,
   lifestyle_train_graph2,
   lifestyle_train_graph3,
   lifestyle_train_graph4,
   lifestyle_train_graph5,
   lifestyle_train_graph6,
   lifestyle_train_graph7,
   lifestyle_train_graph8,
   lifestyle_train_graph9,
   lifestyle_train_graph10,
   lifestyle_train_graph11,
   lifestyle_train_graph12,
   Marketing_train_graph1,
   Marketing_train_graph2,
   Marketing_train_graph3,
   Marketing_train_graph4,
   Marketing_train_graph5,
   Marketing_train_graph6,
   Marketing_train_graph7,
   Marketing_train_graph8,
   Marketing_train_graph9,
   Marketing_train_graph10,
   Marketing_train_graph11,
   Marketing_train_graph12,
     ]  # a list of training set graphs

testing_graphs = [
   finance_test_graph1,
   finance_test_graph2,
   finance_test_graph3,
   lifestyle_test_graph1,
   lifestyle_test_graph2,
   lifestyle_test_graph3,
   Marketing_test_graph1,
   Marketing_test_graph2,
   Marketing_test_graph3,
] # a list of testing set graphs

labels = ["Finance"] * 12 + ["Lifestyle"] * 12 + ["Marketing"] * 12
k=3

#frequent_subgraphs = frequent_subgraph_mining(training_graphs)

# Extract features from training set graphs
#feature_matrix = extract_features(training_graphs, frequent_subgraphs)

predicted_class = knn_classify(Marketing_test_graph1, training_graphs, labels, k)
print(predicted_class)