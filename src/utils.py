import json

def load_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def print_solution(solution_path, problem):
    if isinstance(solution_path, str): print(solution_path)
    else:
        for i, node in enumerate(solution_path):
            if i==0: continue
            if i == len(solution_path) - 1:
                print(node)
                print("=> " + problem.goal_hospital)
            else:
                print(node)