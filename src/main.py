import osmnx as ox
from node import Node
from problem import Problem
from solver import Solver
from utils import load_data, get_current_location_coordinates

graph = ox.load_graphml(filepath="data/Map.graphml")

# Get current location coordinates
Y, X = get_current_location_coordinates()
initial_state = ox.distance.nearest_nodes(graph, X, Y, return_dist=False)

# Define the problem
problem = Problem(initial_state)

# Solve the problem
solver = Solver(problem)
solution_path = solver.breadth_first_search()

# Extract states from solution path
states = [i.state for i in solution_path]

# Plot the solution
ox.plot.plot_graph_route(graph, states)
