import osmnx as ox
from utils import get_current_location_coordinates
from problem import problem
from solver import Solver

graph = ox.load_graphml(filepath="data/Map.graphml")

Y, X = get_current_location_coordinates()
initial_state=ox.distance.nearest_nodes(graph, X, Y, return_dist=False)
problem=problem(initial_state)
solver = Solver(problem)
solution_path = solver.breadth_first_search()

states=[]
for i in solution_path:
    states.append(i.state)
states

ox.plot.plot_graph_route(graph, states)