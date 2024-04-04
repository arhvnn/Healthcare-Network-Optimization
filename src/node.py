class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  
        self.parent = parent  
        self.action = action  
        self.path_cost = path_cost  

    def __str__(self):
        return f"# City: {self.state}, Distance crossed: {round(self.path_cost, 2)}KM"
