from utils import load_data
from node import Node

data_file_path = "data/AlgiersHospitals.json"
algiers_hospitals = load_data(data_file_path)

data_file_path = "data/MapNodes.json"
nodes = load_data(data_file_path)

data_file_path = "data/MapEdges.json"
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

    def actions(self, state):
        neighbour_nodes = self.transition_model[str(state)]["neighbors"]
        return neighbour_nodes

    # FIXME: Remove this function

    def result(self, state, action):
        return action

    def goal_test(self, state):
        hospital = nodes[str(state)]["hospital"]
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
        state = self.result(parent.state, action)
        path_cost = parent.path_cost + self.step_cost(parent.state, action)
        return Node(state=state, parent=parent, action=action, path_cost=path_cost)
