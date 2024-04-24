from node import Node
from collections import deque

class Solver:
    def __init__(self, problem):
        self.problem = problem

    def breadth_first_search(self):
        initial_node = Node(state=self.problem.initial_state, path_cost=0)
        if self.problem.goal_test(initial_node.state):
            return self.solution(initial_node)

        frontier = deque([initial_node])
        explored = set()

        while frontier:
            node = frontier.popleft()
            explored.add(node.state)

            for action in self.problem.actions(node.state):
                child = self.problem.child_node(node, action)
                if child.state not in explored and child not in frontier:
                    if self.problem.goal_test(child.state):
                        return self.solution(child)
                    frontier.append(child)

        return "GOAL IS UNREACHABLE!"

    def solution(self, node):
        path = []
        while node:
            path.insert(0, node)
            node = node.parent
        return path