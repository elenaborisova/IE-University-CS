class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def __repr__(self):
        result = ''

        for source_val, source in self.graph_dict.items():
            if source.get_edges():
                result += f'Comedian {source_val} influences => {source.get_edges()}\n\n'

        return result

