from problem import Problem
from solver import Solver
from utils import load_data, print_solution
import os


def main():
    script_dir = os.path.dirname(__file__)

    data_file_path = os.path.join(script_dir, "..", "data", "AlgiersCities.json")
    algiers_cities = load_data(data_file_path)

    data_file_path = os.path.join(script_dir, "..", "data", "AlgiersHospitals.json")
    algiers_hospitals = load_data(data_file_path)

    initial_state = "Baraki"
    goal_state = {"type": "public", "department": "Physiology"}

    problem = Problem(initial_state, goal_state, algiers_cities, algiers_hospitals)
    solver = Solver(problem)

    solution_path = solver.breadth_first_search()
    if solution_path == "FAILURE!":
        print("Goal not reachable!")
    else:
        print_solution(solution_path, problem)


if __name__ == "__main__":
    main()
