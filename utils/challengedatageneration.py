# Author: Benjamin Maudet

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import json

from tqdm import tqdm

from graphgen import GraphGenerator
from datagen import DataGenerator


if __name__ == "__main__":
    # These values are arbitrary
    N_GRAPHS = 10
    MIN_SAMPLES = 10000
    MAX_SAMPLES = 15000
    SAMPLING_BIAS_QUANTILE_RANGE = (0.92, 0.97)
    BIASTYPES = ['hiddenconfounder', 'sampling']


    graph_generator = GraphGenerator()
    # tqdm progress bar to generate graphs
    for i in tqdm(range(N_GRAPHS)):
        graph = graph_generator.generate()
        original_graph = graph.copy()
        # print(len(original_graph.nodes))
        chosen_bias = random.choice(BIASTYPES)

        metadata = {
            "num_nodes": len(graph.nodes),
            "chosen_bias": chosen_bias
        }

        if chosen_bias == 'hiddenconfounder':
            # add a hidden confounder
            confounder = graph_generator.num_nodes
            graph.add_node(confounder)
            # chose a random edge
            edge = random.choice(list(graph.edges))
            graph.add_edge(confounder, edge[0])
            graph.add_edge(confounder, edge[1])
            metadata["confounder"] = int(confounder)
            metadata["between_nodes"] = edge
            # print("hidden confounder")

        graph_generator.genweight(graph)

        data_generator = DataGenerator(graph, len(graph.nodes))
        data = data_generator.generate(np.random.randint(MIN_SAMPLES, MAX_SAMPLES))
        df = pd.DataFrame(data, columns=list(graph.nodes))

        if chosen_bias == 'hiddenconfounder':
            df = df.drop(columns=[confounder])

        if chosen_bias == 'sampling':
            # chose a random node to bias
            biased_node = np.random.randint(0, len(graph.nodes))
            # get the 95% quantile of the node
            quantile = random.uniform(*SAMPLING_BIAS_QUANTILE_RANGE)
            threshold = df[biased_node].quantile(quantile)
            # remove all rows where the node is above the quantile
            df = df[df[biased_node] < threshold]
            metadata["biased_node"] = biased_node
            metadata["quantile"] = quantile
            metadata["threshold"] = threshold

        # save the graph and the data
        with open(f"generated_data/ground_truths/metadata_{i}.json", "w") as f:
            json.dump(metadata, f)
        truth = nx.to_numpy_matrix(original_graph, nodelist=sorted(original_graph.nodes), dtype=np.uint8, weight=None)
        np.save(f"generated_data/ground_truths/{i}.npy", truth)
        df.to_csv(f"generated_data/datasets/{i}.csv", index=False)
    
