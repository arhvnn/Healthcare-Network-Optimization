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
                    self.problem.heuristic(initial_node) + initial_node.path_cost,
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

    def solution(self, node):
        path = []
        while node:
            path.insert(0, node)
            node = node.parent
        return path

    def hill_climbing_search(self, max_iterations=1000, step_size=0.1):
        # Initialize random starting point
        current_node = Node(state=self.problem.initial_state, path_cost=0)
        current_value = self.problem.heuristic(current_node.state)

        for _ in range(max_iterations):
            # Generate a new solution by adding a small random step
            new_state = self.problem.random_successor(current_node.state)
            new_node = Node(state=new_state, parent=current_node, path_cost=current_node.path_cost + 1)
            new_value = self.problem.heuristic(new_state)

            # If the new solution is better, move to it
            if new_value > current_value:
                current_node = new_node
                current_value = new_value

        return self.solution(current_node)