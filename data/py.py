import osmnx

graph = osmnx.graph_from_place('Algiers, Algeria')
osmnx.plot.graph(graph)