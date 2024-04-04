from copy import deepcopy
from node import Node

class Problem:
    def __init__(self, initial_state, goal_state, transition_model, hospital_info):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.transition_model = transition_model
        self.hospital_info = hospital_info
        self.goal_hospital = ""

    def actions(self, state):
        neighbour_cities = list(self.transition_model[state]["connections"].keys())
        return neighbour_cities

    def result(self, state, action):
        return action

    def goal_test(self, state):
        city_hospitals = self.transition_model[state]["hospitals"]
        for hospital in city_hospitals:
            if (
                self.goal_state["type"] == self.hospital_info[hospital]["type"]
                and self.goal_state["department"]
                in self.hospital_info[hospital]["departments"]
            ):
                self.goal_hospital = hospital
                return True
        return False

    def step_cost(self, state, action):
        return self.transition_model[state]["connections"][action]

    def child_node(self, parent, action):
        state = self.result(parent.state, action)
        path_cost = parent.path_cost + self.step_cost(parent.state, action)
        return Node(state=state, parent=parent, action=action, path_cost=path_cost)
