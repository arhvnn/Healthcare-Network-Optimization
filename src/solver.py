from node import Node
from collections import deque
import heapq


class Solver:
    def __init__(self, problem):
        self.problem = problem

    def general_search(self, strategy="BFS"):
        initial_node = Node(state=self.problem.initial_state, path_cost=0)
        if self.problem.goal_test(initial_node.state):
            return self.solution(initial_node)

        if strategy == "BFS":
            frontier = deque([initial_node])  # Use a deque for BFS
        elif strategy == "A*":
            # Initialize the priority queue with the initial node and its cost
            frontier = []
            heapq.heappush(
                frontier,
                (
                    self.problem.heuristic(initial_node.state) + initial_node.path_cost,
                    initial_node,
                ),
            )
        else:
            frontier = [initial_node]  # Use a list for DFS

        explored = set()

        while frontier:
            if strategy == "BFS":
                node = frontier.popleft()  # FIFO for BFS
            elif strategy == "A*":
                _, node = heapq.heappop(frontier)  # Pop the node with the lowest cost
            else:
                node = frontier.pop()  # LIFO for DFS

            if node.state not in explored:
                explored.add(node.state)

                if self.problem.goal_test(node.state):
                    return self.solution(node)

                for action in self.problem.actions(node.state):
                    child = self.problem.child_node(node, action)
                    if (
                        child.state not in explored
                    ):  # and all(child != existing[1] for existing in frontier):
                        if strategy == "A*":
                            heapq.heappush(
                                frontier,
                                (
                                    child.path_cost
                                    + self.problem.heuristic(child.state),
                                    child,
                                ),
                            )
                        else:
                            frontier.append(child)

        return "GOAL IS UNREACHABLE!"

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

    def depth_first_search(self):
        initial_node = Node(state=self.problem.initial_state, path_cost=0)
        if self.problem.goal_test(initial_node.state):
            return self.solution(initial_node)

        frontier = [initial_node]
        explored = set()

        while frontier:
            node = frontier.pop()
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
