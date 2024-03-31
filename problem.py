from collections import deque
import heapq
from copy import deepcopy
import json

algiers_cities = {}
with open('data/AlgiersCities.json', 'r') as f:
    algiers_cities=json.read() 

class TravelPlanningProblemV2:
    def __init__(
        self,
        initial_state,
        goal_state,
        transition_model=algiers_cities,
    ):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.transition_model = transition_model

    def actions(self, state):
        neighbour_cities = self.transition_model[state]
        if neighbour_cities:
            neighbour_cities_numbers = list(
                self.transition_model[state]["connections"].keys()
            )
            return neighbour_cities_numbers
        else:
            return []

    def result(self, state, action):
        new_state = deepcopy(state)
        if action in self.transition_model[state]:
            new_state = action
        else:
            new_state = self.transition_model[state]["Neighbors"][action]
        return new_state

    def goal_test(self, state):
        return state == self.goal_state

    def step_cost(self, state, action):
        return self.transition_model[state]["connections"][action]
