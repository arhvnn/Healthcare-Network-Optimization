from turtle import distance
from utils import load_data
from node import Node
import osmnx as ox
import os
import networkx as nx

script_dir = os.path.dirname(__file__)

data_file_path = os.path.join(script_dir, "..", "data", "Map.graphml")
graph = ox.load_graphml(filepath=data_file_path)

data_file_path = os.path.join(script_dir, "..", "data", "AlgiersHospitals.json")
algiers_hospitals = load_data(data_file_path)

data_file_path = os.path.join(script_dir, "..", "data", "MapNodes.json")
nodes = load_data(data_file_path)

data_file_path = os.path.join(script_dir, "..", "data", "MapEdges.json")
edges = load_data(data_file_path)
edges = {
    eval(key): value for key, value in edges.items()
}  # Turns keys from string into tuples


class problem:
    def __init__(
        self,
        initial_state,
        goal_state={"type": "public", "department": "General Surgery"},
        transition_model=nodes,
        costs=edges,
        hospital_info=algiers_hospitals,
    ):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.transition_model = transition_model
        self.hospital_info = hospital_info
        self.costs = costs
        self.goal_hospital = self.goal_hospital()

    def actions(self, state):
        neighbour_nodes = self.transition_model[str(state)]["neighbors"]
        return neighbour_nodes

    # FIXME: Remove this function

    def result(self, state, action):
        return action

    def goal_test(self, state):
        hospital = self.transition_model[str(state)]["hospital"]
        if hospital:
            if (
                self.goal_state["type"] == self.hospital_info[hospital]["type"]
                and self.goal_state["department"]
                in self.hospital_info[hospital]["departments"]
            ):
                return True
        return False

    def step_cost(self, state, action):
        return self.costs[(state, action)]["length"]

    def child_node(self, parent, action):
        """Derives a child node and updates its path cost"""
        state = self.result(parent.state, action)
        path_cost = parent.path_cost + self.step_cost(parent.state, action)
        return Node(state=state, parent=parent, action=action, path_cost=path_cost)

    def goal_hospital(self):
        """Returns the nearest hospital that satisfies the goal\'s requirments for the A* algorithm"""
        initial_x, initial_y = (
            self.transition_model[str(self.initial_state)]["x"],
            self.transition_model[str(self.initial_state)]["y"],
        )
        min_distance = float('inf')
        goal_hospital = None
        for hospital, info in self.hospital_info.items():
            if (
                self.goal_state["type"] == info["type"]
                and self.goal_state["department"] in info["departments"]
            ):
                distance = ox.distance.euclidean(
                    initial_y, initial_x, info["y"], info["x"]
                )
                if distance < min_distance:
                    min_distance = distance
                    goal_hospital_info = info
        return ox.distance.nearest_nodes(graph, goal_hospital_info['x'], goal_hospital_info['y'], return_dist=False)

    def heuristic(self, state):
        """Straight Line Distance heuristic"""
        goal_hospital = self.goal_hospital
        current_x, current_y = (
            self.transition_model[str(state)]["x"],
            self.transition_model[str(state)]["y"],
        )
        return ox.distance.euclidean(
            current_y,
            current_x,
            self.transition_model[str(goal_hospital)]["y"],
            self.transition_model[str(goal_hospital)]["x"],
        )
    
    def random_successor(self, state):
        """Returns a random successor of the given state"""
        import random
        return random.choice(self.actions(state))
