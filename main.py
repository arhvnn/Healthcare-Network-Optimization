from collections import deque
import heapq
from copy import deepcopy
import json

algiers_cities = {}
with open("data/AlgiersCities.json", "r") as f:
    algiers_cities = json.load(f)

algiers_hospitals = {}
with open("data/AlgiersHospitals.json", "r") as f:
    algiers_hospitals = json.load(f)


class TransportProblem:
    def __init__(
        self,
        initial_state,
        goal_state={"type": "public", "department": "Gynecology-Obstetrics"},
        transition_model=algiers_cities,
        hospital_info=algiers_hospitals,
    ):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.transition_model = transition_model
        self.hospital_info = hospital_info

    def actions(self, state):
        neighbour_cities = list(self.transition_model[state]["connections"].keys())
        return neighbour_cities

    def result(self, state, action):
        new_state = deepcopy(state)
        new_state = action
        return new_state

    def goal_test(self, state):
        city_hospitals = algiers_cities[state]["hospitals"]
        for hospital in city_hospitals:
            if (
                self.goal_state["type"] == self.hospital_info[hospital]["type"]
                and self.goal_state["department"]
                in self.hospital_info[hospital]["departments"]
            ):
                return True
        return False

    def step_cost(self, state, action):
        return self.transition_model[state]["connections"][action]


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # Represents the state in the state space
        self.parent = parent  # Represents the parent node in the search tree
        self.action = action  # Represents the action taken to reach this state
        self.path_cost = path_cost  # Represents the cost of the path from the initial state


    def __str__(self):
        return f"# State: {self.state}, Distance crossed: {round(self.path_cost, 2)}KM"


def child_node(problem, parent, action):
    state = problem.result(parent.state, action)
    path_cost = parent.path_cost + problem.step_cost(parent.state, action)
    return Node(state=state, parent=parent, action=action, path_cost=path_cost)


def solution(node):
    path = []
    while node:
        path.insert(0, node)
        node = node.parent
    return path


def breadth_first_search(problem):
    node = Node(state=problem.initial_state, path_cost=0)
    if problem.goal_test(node.state):
        return solution(node)

    frontier = deque([node])  # FIFO queue with node as the only element
    explored = set()

    while frontier:
        if not frontier:  # If frontier is empty
            return "failure"

        node = frontier.popleft()  # Choose the shallowest node in frontier
        explored.add(tuple(map(tuple, node.state)))

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if (
                tuple(map(tuple, child.state)) not in explored and child not in frontier
            ):  # To avoid redundant paths and loops
                if problem.goal_test(child.state):
                    return solution(child)
                frontier.append(child)

    return "FAILURE!"


def GeneralSolver(problem, algorithm):
    if algorithm == "BFS":
        solution_path = breadth_first_search(problem)
        cost = 0
        for i, node in enumerate(solution_path):
            if i ==len(solution_path)-1: 
                print(node)
                for hospital in algiers_cities[node.state]["hospitals"]:
                    if goal["department"] in algiers_hospitals[hospital]["departments"]:
                        print("=> "+hospital)
            else: print(node)
    return solution_path

goal={"type": "public", "department":"Physiology"}
problem = TransportProblem(initial_state="Mahelma", goal_state=goal)
GeneralSolver(problem, "BFS")
