from collections import deque
import heapq
from copy import deepcopy
from tabulate import tabulate


class EightPuzzleProblem:
    def __init__(self, initial_state, goal_state=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        # Appends possible actions to a list then returns it
        actions = []
        empty_tile_row, empty_tile_col = self.find_empty_tile(state)

        if empty_tile_row > 0:
            actions.append("UP")
        if empty_tile_row < 2:
            actions.append("DOWN")
        if empty_tile_col > 0:
            actions.append("LEFT")
        if empty_tile_col < 2:
            actions.append("RIGHT")

        return actions

    def result(self, state, action):
        # Applies an action to a state, then returns the new state
        new_state = deepcopy(state)
        empty_tile_row, empty_tile_col = self.find_empty_tile(new_state)
        # Swaps the empty tile with the tile of the corresponding direction
        if action == "UP":
            (
                new_state[empty_tile_row][empty_tile_col],
                new_state[empty_tile_row - 1][empty_tile_col],
            ) = (new_state[empty_tile_row - 1][empty_tile_col], 0)
        elif action == "DOWN":
            (
                new_state[empty_tile_row][empty_tile_col],
                new_state[empty_tile_row + 1][empty_tile_col],
            ) = (new_state[empty_tile_row + 1][empty_tile_col], 0)
        elif action == "LEFT":
            (
                new_state[empty_tile_row][empty_tile_col],
                new_state[empty_tile_row][empty_tile_col - 1],
            ) = (new_state[empty_tile_row][empty_tile_col - 1], 0)
        elif action == "RIGHT":
            (
                new_state[empty_tile_row][empty_tile_col],
                new_state[empty_tile_row][empty_tile_col + 1],
            ) = (new_state[empty_tile_row][empty_tile_col + 1], 0)

        return new_state

    def goal_test(self, state):
        return state == self.goal_state

    def step_cost(self, state, action):
        # Define the step cost function to compute the cost of taking an action in a given state
        return 1

    def find_empty_tile(self, state):
        # Traverses the state matrix and returns the empty tile as a tuple
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j


################################################################
cities_connections = {
    "Algiers": ["Oran", "Constantine", "Tizi Ouzou", "Bechar", "Setif"],
    "Oran": ["Algiers", "Tlemcen", "Mascara", "Skikda", "Bejaia"],
    "Constantine": ["Algiers", "Annaba", "Setif", "Ghardaia"],
    "Tizi Ouzou": ["Algiers", "Bejaia", "Bouira", "Adrar"],
    "Tlemcen": ["Oran", "Sidi Bel Abbes", "Mascara", "Guelma"],
    "Annaba": ["Constantine", "Guelma", "Skikda", "El Oued"],
    "Bechar": ["Algiers", "Adrar", "Tindouf"],
    "Setif": ["Algiers", "Constantine", "Ghardaia", "El Oued"],
    "Bejaia": ["Oran", "Tizi Ouzou", "Bouira", "Tindouf"],
    "Mascara": ["Oran", "Tlemcen", "Guelma", "El Oued"],
    "Guelma": ["Tlemcen", "Annaba", "Mascara", "Tindouf"],
    "Skikda": ["Oran", "Annaba", "El Oued", "Tindouf"],
    "Ghardaia": ["Constantine", "Setif", "Adrar"],
    "Bouira": ["Tizi Ouzou", "Bejaia", "Tindouf"],
    "Adrar": ["Bechar", "Tizi Ouzou", "Ghardaia"],
    "Tindouf": ["Bechar", "Bejaia", "Guelma", "Skikda", "Bouira"],
}


class TravelPlanningProblem:
    def __init__(
        self,
        initial_state="Algiers",
        goal_state="Skikda",
        transition_model=cities_connections,
    ):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.transition_model = transition_model

    def actions(self, state):
        neighbour_cities = self.transition_model[state]
        if neighbour_cities:
            neighbour_cities_numbers = list(range(1, len(neighbour_cities) + 1))
            return neighbour_cities_numbers
        else:
            return []

    def result(self, state, action):
        new_state = deepcopy(state)
        if action in self.transition_model[state]:
            new_state = action
        else:
            new_state = self.transition_model[state][
                action - 1
            ]  # Subtract 1 since actions start from 1
        return new_state

    def goal_test(self, state):
        return state == self.goal_state

    def step_cost(self, state, action):
        return 1


################################################################
cities_connections_v2 = {
    "Algiers": {
        "Coordinates": (36.7528, 3.0420),
        "Neighbors": {
            "Oran": 450,
            "Constantine": 320,
            "Tizi Ouzou": 80,
            "Bechar": 700,
            "Setif": 200,
        },
    },
    "Oran": {
        "Coordinates": (35.6969, -0.6331),
        "Neighbors": {
            "Algiers": 450,
            "Tlemcen": 200,
            "Mascara": 150,
            "Skikda": 550,
            "Bejaia": 400,
        },
    },
    "Constantine": {
        "Coordinates": (36.3650, 6.6147),
        "Neighbors": {"Algiers": 320, "Annaba": 210, "Setif": 120, "Ghardaia": 600},
    },
    "Tizi Ouzou": {
        "Coordinates": (36.7117, 4.0456),
        "Neighbors": {"Algiers": 80, "Bejaia": 150, "Bouira": 100, "Adrar": 800},
    },
    "Tlemcen": {
        "Coordinates": (34.8888, -1.3153),
        "Neighbors": {
            "Oran": 200,
            "Sidi Bel Abbes": 120,
            "Mascara": 180,
            "Guelma": 350,
        },
    },
    "Annaba": {
        "Coordinates": (36.9060, 7.7465),
        "Neighbors": {"Constantine": 210, "Guelma": 100, "Skikda": 90, "El Oued": 450},
    },
    "Bechar": {
        "Coordinates": (31.6304, -2.2687),
        "Neighbors": {"Algiers": 700, "Adrar": 100, "Tindouf": 300},
    },
    "Setif": {
        "Coordinates": (36.1869, 5.4175),
        "Neighbors": {
            "Algiers": 200,
            "Constantine": 120,
            "Ghardaia": 300,
            "El Oued": 500,
        },
    },
    "Bejaia": {
        "Coordinates": (36.7508, 5.0564),
        "Neighbors": {"Oran": 400, "Tizi Ouzou": 150, "Bouira": 250, "Tindouf": 600},
    },
    "Mascara": {
        "Coordinates": (35.3984, 0.1401),
        "Neighbors": {"Oran": 150, "Tlemcen": 180, "Guelma": 400, "El Oued": 550},
    },
    "Guelma": {
        "Coordinates": (36.4629, 7.4267),
        "Neighbors": {"Tlemcen": 350, "Annaba": 100, "Mascara": 400, "Tindouf": 700},
    },
    "Skikda": {
        "Coordinates": (36.8796, 6.9036),
        "Neighbors": {"Oran": 550, "Annaba": 90, "El Oued": 350, "Tindouf": 800},
    },
    "Ghardaia": {
        "Coordinates": (32.4882, 3.6733),
        "Neighbors": {"Constantine": 600, "Setif": 300, "Adrar": 400},
    },
    "Bouira": {
        "Coordinates": (36.3724, 3.9007),
        "Neighbors": {"Tizi Ouzou": 100, "Bejaia": 250, "Tindouf": 650},
    },
    "Adrar": {
        "Coordinates": (27.8617, -0.2917),
        "Neighbors": {"Bechar": 100, "Tizi Ouzou": 800, "Ghardaia": 400},
    },
    "El Oued": {
        "Coordinates": (33.3564, 6.8631),
        "Neighbors": {"Annaba": 450, "Mascara": 550, "Skikda": 350},
    },
    "Tindouf": {
        "Coordinates": (27.6706, -8.1476),
        "Neighbors": {
            "Bechar": 300,
            "Bejaia": 600,
            "Guelma": 700,
            "Skikda": 800,
            "Bouira": 650,
        },
    },
}


class TravelPlanningProblemV2:
    def __init__(
        self,
        initial_state="Algiers",
        goal_state="Skikda",
        transition_model=cities_connections_v2,
    ):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.transition_model = transition_model

    def actions(self, state):
        neighbour_cities = self.transition_model[state]
        if neighbour_cities:
            neighbour_cities_numbers = list(
                self.transition_model[state]["Neighbors"].keys()
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
        return self.transition_model[state]["Neighbors"][action]


################################################################
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # Represents the state in the state space
        self.parent = parent  # Represents the parent node in the search tree
        self.action = action  # Represents the action taken to reach this state
        self.path_cost = (
            path_cost  # Represents the cost of the path from the initial state
        )

    def __str__(self):
        return f"# State: {self.state}, Action: {self.action}, Path Cost: {self.path_cost}\n"


################################################################
# class Problem:
#     def __init__(self, initial_state, goal_state):
#         self.initial_state = initial_state
#         self.goal_state = goal_state

#     def actions(self, state):
#         return []

#     def result(self, state, action):
#         return state

#     def goal_test(self, state):
#         return state == self.goal_state

#     def step_cost(self, state, action):
#         return 1


################################################################
def child_node(problem, parent, action):
    state = problem.result(parent.state, action)
    path_cost = parent.path_cost + problem.step_cost(parent.state, action)
    return Node(state=state, parent=parent, action=action, path_cost=path_cost)


################################################################
def solution(node):
    path = []
    while node:
        path.insert(0, node)
        node = node.parent
    return path


################################################################
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

    return "failure"

################################################################
def depth_first_search(problem):
    node = Node(state=problem.initial_state, path_cost=0)
    if problem.goal_test(node.state):
        return solution(node)

    frontier = [(node.path_cost, node)]  # Priority queue ordered by path cost
    explored = set()
    solutions=[]

    while frontier:
        if not frontier:  # If frontier is empty
            return "failure"

        _, node = frontier.pop()  # Choose the node with lowest path cost from frontier
        explored.add(tuple(map(tuple, node.state)))

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if tuple(map(tuple, child.state)) not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    solutions.append(solution(child))
                frontier.append((child.path_cost, child))
    optimised_solution=min(solutions, key=len)
    if optimised_solution: return optimised_solution
    else: return "failure"


################################################################
def uniform_cost_search(problem):
    node = Node(state=problem.initial_state, path_cost=0)
    frontier = [(node.path_cost, node)]  # Priority queue ordered by path cost
    explored = set()

    while frontier:
        if not frontier:  # If frontier is empty
            return "failure"

        _, node = heapq.heappop(frontier)  # Choose the lowest-cost node in frontier
        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node.state)

        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if child.state not in explored and not any(
                child.state == n[1].state for n in frontier
            ):
                heapq.heappush(frontier, (child.path_cost, child))
            elif any(
                child.state == n[1].state and child.path_cost < n[1].path_cost
                for n in frontier
            ):
                frontier = [
                    (cost, nd) if nd.state != child.state else (child.path_cost, child)
                    for cost, nd in frontier
                ]

    return "failure"


################################################################
def GeneralSolver(problem, algorithm):
    if algorithm == "BFS":
        solution_path = breadth_first_search(problem)
        for node in solution_path:
            print(node)
    elif algorithm == "DFS":
        solution_path = depth_first_search(problem)
        for node in solution_path:
            print(node)
    elif algorithm == "UCS":
        solution_path = uniform_cost_search(problem)
        for node in solution_path:
            print(node)
    return solution_path


################################################################
problem = EightPuzzleProblem([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
GeneralSolver(problem, "DFS")
# print(problem.step_cost("Algiers", "Setif"))