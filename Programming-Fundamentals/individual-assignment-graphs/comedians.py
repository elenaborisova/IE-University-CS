# %%
import csv
from graph import Graph
from vertex import Vertex
from collections import deque
from pyvis.network import Network


def parse_csv_to_graph(path):
    influences_graph = Graph(directed=True)

    try:
        with open(path) as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                source, target = row

                if not source:
                    continue
                elif source not in influences_graph.graph_dict:
                    source_vertex = Vertex(source)
                    influences_graph.add_vertex(source_vertex)
                else:
                    source_vertex = influences_graph.graph_dict[source]

                if not target:
                    continue
                elif target not in influences_graph.graph_dict:
                    target_vertex = Vertex(target)
                    influences_graph.add_vertex(target_vertex)
                else:
                    target_vertex = influences_graph.graph_dict[target]

                influences_graph.add_edge(source_vertex, target_vertex)

        return influences_graph

    except:
        return None


# %%
def is_input_valid(diagram, start, end):
    return start in diagram.graph_dict and end in diagram.graph_dict


def influence_chains(diagram, start, end=None):
    if end is not None and not is_input_valid(diagram, start, end):
        return f'The comedian(s) does not exist in the network!'

    queue = deque([start])
    paths = {start: [start]}

    while queue:
        source = queue.popleft()
        source_vertex = diagram.graph_dict[source]
        targets = source_vertex.get_edges()

        for target in targets:
            if target not in paths:
                if target == end:
                    return {start: paths[source][1:] + [target]}
                paths[target] = paths[source] + [target]
            queue.append(target)

    result = {start: list(paths)[1:]}
    if end is not None and end not in paths:
        return f'There is no path between {start} and {end}!'
    return result


# %%
def top_10_influencers(diagram):
    influencers_scores = {}

    for influencer_name, influencer_vertex in diagram.graph_dict.items():
        influencers_scores[influencer_name] = len(influencer_vertex.get_edges())

    influencers_scores_sorted = [k for k, v in sorted(influencers_scores.items(),
                                                      key=lambda x: x[1],
                                                      reverse=True)]

    return influencers_scores_sorted[:10]


# %%
def draw_graph(diagram):
    net = Network(directed=True)

    nodes = list(diagram.graph_dict.keys())
    net.add_nodes(nodes, label=nodes)

    for node in diagram.graph_dict:
        for neighbor in diagram.graph_dict[node].get_edges():
            net.add_edge(node, neighbor)

    net.repulsion(
        node_distance=500,
        central_gravity=0.2,
        spring_length=200,
        spring_strength=0.05,
        damping=0.09,
    )

    net.show('graph-visualization.html')
    
    
graph = parse_csv_to_graph('comedians.csv')
