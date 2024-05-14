import osmnx as ox
from utils import get_current_location_coordinates
from problem import problem
from solver import Solver
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(__file__)

data_file_path = os.path.join(script_dir, "..", "data", "Map.graphml")
graph = ox.load_graphml(filepath=data_file_path)


Y, X = ox.geocoder.geocode("Sidi Abdellah")

initial_state = ox.distance.nearest_nodes(graph, X, Y, return_dist=False)
problem = problem(initial_state, goal_state={"type": "public", "department": "Anatomical Pathology"})
solver = Solver(problem)
# solution_path = solver.general_search(strategy="BFS")
solution_path = solver.hill_climbing_search()

states = []
for node in solution_path:
    states.append(node.state)

fig, ax = ox.plot.plot_graph_route(graph, states, route_color="b")
fig.savefig("solution.jpg")
