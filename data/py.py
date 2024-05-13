import osmnx

graph = osmnx.graph_from_place("Algiers, Algeria", network_type="drive")
osmnx.io.save_graphml(graph, filepath="DriveGraph.graphml")
