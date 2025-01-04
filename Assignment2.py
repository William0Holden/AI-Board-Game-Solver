# William Holden
from search import *

def main():
    initial_state = (0, 0)
    problem = WaterAndJugsProblem(initial_state)
    solution = breadth_first_tree_search(problem)
    
    # Check if a solution was found
    if solution:
        file_path = os.path.join(os.getcwd(), "water_jugs_solution.txt") #
        print("Solution Path:")
        with open(file_path, "w") as file:
            file.write("Water Jugs Solution: \n")
            for step in solution.path():
                state_str = str(step.state)
                print(state_str)
                file.write(state_str + "\n")
        print("Solution path has been saved to " + file_path + ".")
    else:
        print("No solution found.")

    initial_grid = (3, 5, 1, 8, 2, 6, 0, 7, 4) # initial state for all eight puzzles as outlined in 1.2
    goal = (1, 2, 3, 8, 0, 4, 7, 6, 5) # goal for all eight puzzles as outlined in 1.2

    problem = EightPuzzleManhattanDistance(initial_grid, goal) # initializing problem
    solution = astar_search(problem) # solving problem
    if solution: # printing solution to .txt file
        file_path = os.path.join(os.getcwd(), "eight_puzzle_solution_manhattan_distance.txt") 
        print("Solution Path:")
        with open(file_path, "w") as file:
            file.write("Eight Puzzle with Manhattan distance heuristic: \n")
            for step in solution.path():
                state_str = str(step.state)
                print(state_str)
                file.write(state_str + "\n")
        print("Solution path has been saved to " + file_path + ".")
    else:
        print("No solution found.")

    problem = EightPuzzleMisplacedTiles(initial_grid, goal)
    solution = astar_search(problem)
    if solution:  
        file_path = os.path.join(os.getcwd(), "eight_puzzle_solution_misplaced_tiles.txt") 
        print("Solution Path:")
        with open(file_path, "w") as file:
            file.write("Eight Puzzle with misplaced tiles heurisitc: \n")
            for step in solution.path():
                state_str = str(step.state)
                print(state_str)
                file.write(state_str + "\n")
        print("Solution path has been saved to " + file_path + ".")
    else:
        print("No solution found.")

    problem = EightPuzzleNMaxSwap(initial_grid, goal)
    solution = astar_search(problem)
    if solution:
        file_path = os.path.join(os.getcwd(), "eight_puzzle_solution_n_max_swap.txt")
        print("Solution Path:")
        with open(file_path, "w") as file:
            file.write("Eight Puzzle with n Max Swaps heurisitc: \n")
            for step in solution.path():
                state_str = str(step.state)
                print(state_str)
                file.write(state_str + "\n")
        print("Solution path has been saved to " + file_path + ".")
    else:
        print("No solution found.")

    problem = EightPuzzleNilssonsDistance(initial_grid, goal)
    solution = astar_search(problem)
    if solution:
        file_path = os.path.join(os.getcwd(), "eight_puzzle_solution_nilssons_distance.txt")
        print("Solution Path:")
        with open(file_path, "w") as file:
            file.write("Eight Puzzle with Nilsson's distance heurisitc: \n")
            for step in solution.path():
                state_str = str(step.state)
                print(state_str)
                file.write(state_str + "\n")
        print("Solution path has been saved to " + file_path + ".")
    else:
        print("No solution found.")

    initial_state = ('M', 'M', 'M', ' ', 'F', 'F', 'F')
    problem = TheDatingGame(initial_state)
    solution = astar_search(problem)
    if solution:
        file_path = os.path.join(os.getcwd(), "dating_game_solution_astar.txt")
        print("Solution Path:")
        with open(file_path, "w") as file:
            file.write("Dating Game Solutuion with AStar search: \n")
            for step in solution.path():
                state_str = str(step.state)
                print(state_str)
                file.write(state_str + "\n")
        print("Solution path has been saved to " + file_path + ".")
    else:
        print("No solution found.")

    solution = depth_limited_search(problem)
    if solution:
        file_path = os.path.join(os.getcwd(), "dating_game_solution_depth_limited.txt")
        print("Solution Path:")
        with open(file_path, "w") as file:
            file.write("Dating Game Solutuion with depth limited search: \n")
            for step in solution.path():
                state_str = str(step.state)
                print(state_str)
                file.write(state_str + "\n")
        print("Solution path has been saved to " + file_path + ".")

    initial_state = (1, 1)
    goal = (3, 2)
    grid_problem = GridWorldProblem(initial_state, goal)
    grid_agent = GridAgent()
    grid_agent.search(grid_problem)
    grid_agent.print_solution()


# Problem 1: Water and Jug Problem PUT MORE COMMENTS IN HERE
class WaterAndJugsProblem(Problem):
    def __init__(self, initial, goal=(2, 0)):
        super().__init__(initial, goal)

    def actions(self, state): # defining actions
        actions = []
        if state[0] < 4:
            actions.append("Fill 4-gallon jug")
        if state[1] < 3:
            actions.append("Fill 3-gallon jug")
        if state[0] > 0:
            actions.append("Empty 4-gallon jug")
        if state[1] > 0:
            actions.append("Empty 3-gallon jug")
        if state[0] > 0 and state[1] < 3:
            actions.append("Pour water from 4-gallon jug into 3-gallon jug")
        if state[0] < 4 and state[1] > 0:
            actions.append("Pour water from 3-gallon jug into 4-gallon jug")
        return actions

    def result(self, state, action): # defining results (what will happen when an action is taken)
        if action == "Fill 4-gallon jug": 
            return (4, state[1])
        elif action == "Fill 3-gallon jug": 
            return (state[0], 3)
        elif action == "Empty 4-gallon jug":
            return (0, state[1])
        elif action == "Empty 3-gallon jug":
            return (state[0], 0)
        elif action == "Pour water from 4-gallon jug into 3-gallon jug":
            if state[0] + state[1] <= 3:
                return (0, state[0] + state[1])
            else:
                return (state[0] + state[1] - 3, 3)
        elif action == "Pour water from 3-gallon jug into 4-gallon jug":
            if state[0] + state[1] <= 4:
                return (state[0] + state[1], 0)
            else:
                return (4, state[0] + state[1] - 4)

    def goal_test(self, state):
        return state == self.goal
    
class EightPuzzleNMaxSwap(EightPuzzle): # defining the n max swap heuristic
    def h(self, node):
        nMaxSwaps = 0

        
        tempState = []
        for i in range(len(node.state)):
            tempState.append(node.state[i])

        isSameFlag = False
        while not isSameFlag:
            for i in range(len(tempState)):
                if tempState[i] == 0 and self.goal[i] != 0 and tempState[i] != self.goal[i]: # looking to see if 0 is in the incorrect position
                    tempState[tempState.index(self.goal[i])] = 0 #swapping 0 with the number that should be in its position
                    tempState[i] = self.goal[i]
                    nMaxSwaps += 1
                if self.goal[tempState.index(0)] == 0 and tempState[i] != 0 and tempState[i] != self.goal[i]: # looking for a number in the incorrect position while 0 is in the goal position
                    tempState[tempState.index(0)] = tempState[i] #swapping the number in the incorrect position with 0
                    tempState[i] = 0
                    nMaxSwaps += 1
            for i in range(len(tempState)): #checking to see if in goal position after each loop through the list
                if tempState[i] == self.goal[i]:
                    isSameFlag = True
                else:
                    isSameFlag = False
                    break
        return nMaxSwaps
    
class EightPuzzleManhattanDistance(EightPuzzle): # defining the manhattan distance heuristic
    def h(self, node):
        #coverting to a 3x3 grid for easier calculations

        goal_grid = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                goal_grid[i][j] = self.goal[i*3 + j]

        #coverting the current state to a 3x3 grid

        curr_grid = [[node.state[0],node.state[1],node.state[2]],[node.state[3],node.state[4],node.state[5]],[node.state[6],node.state[7],node.state[8]]] # i know this is lazy but it works

        #calculating the manhattan distance
        manhatDis = 0
        for i in range(3):
            for j in range(3):
                if curr_grid[i][j] != goal_grid[i][j]:
                    for k in range(3):
                        for l in range(3):
                            if curr_grid[i][j] == goal_grid[k][l]:
                                manhatDis += abs(i-k) + abs(j-l) #returning the manhattan distance
        return manhatDis
    
class EightPuzzleNilssonsDistance(EightPuzzle):
    def h(self, node):
        goal_grid = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                goal_grid[i][j] = self.goal[i*3 + j]

        #coverting the current state to a 3x3 grid

        curr_grid = [[node.state[0],node.state[1],node.state[2]],[node.state[3],node.state[4],node.state[5]],[node.state[6],node.state[7],node.state[8]]]

        #calculating the manhattan distance (same as above)
        manhatDis = 0
        for i in range(3):
            for j in range(3):
                if curr_grid[i][j] != goal_grid[i][j]:
                    for k in range(3):
                        for l in range(3):
                            if curr_grid[i][j] == goal_grid[k][l]:
                                manhatDis += abs(i-k) + abs(j-l) #returning the manhattan distance
        
        #calculating sequence score: for each noncentral square, add 2 if it is not followed by its proper successor, and 0 otherwise

        seqScore = 0
        for i in range(3):
            for j in range(3): 
                if i != 1 and j != 1: # if not the central square
                    if j < 2:
                        if curr_grid[i][j + 1] != goal_grid[i][j+1]: # if not followed by proper successor
                            seqScore += 2
                    elif j == 2 and i < 2:
                        if curr_grid[i+1][0] != goal_grid[i+1][0]: # if not followed by proper successor
                            seqScore += 2
                    elif j == 2 and i == 2: # if last square loop back to first square
                        if curr_grid[0][0] != goal_grid[0][0]:
                            seqScore += 2
    
        return manhatDis + seqScore
    
class EightPuzzleMisplacedTiles(EightPuzzle): # defining the misplaced tiles heuristic (original heuristic)
    def h(self, node):
        return sum(s != g for (s, g) in zip(node.state, self.goal))

class TheDatingGame(Problem): 
    def __init__(self, initial, goal=('M','F','M','F','M','F',' ')):
        super().__init__(initial, goal)

    def find_empty_chair(self, state):
        return state.index(' ')

    def actions(self, state): # defining actions
        possible_actions = ["LEFT 1", "LEFT 2", "LEFT 3", "RIGHT 1", "RIGHT 2", "RIGHT 3"]

        empty_chair = self.find_empty_chair(state)

        if empty_chair < 3: 
            possible_actions.remove("LEFT 3")
        if empty_chair < 2: # if the empty chair is in the first two positions, you can't move left two
            possible_actions.remove("LEFT 2")
        if empty_chair < 1: # if the empty chair is in the first position, you can't move left
            possible_actions.remove("LEFT 1")
        if empty_chair > 3:
            possible_actions.remove("RIGHT 3")
        if empty_chair > 4: # if the empty chair is in the last two positions, you can't move right two
            possible_actions.remove("RIGHT 2")
        if empty_chair > 5: # if the empty chair is in the last position, you can't move right
            possible_actions.remove("RIGHT 1")
    
        return possible_actions
    
    def result(self, state, action):
        empty_chair = self.find_empty_chair(state)
        new_state = list(state)

        delta = {"LEFT 1": -1, "LEFT 2": -2,"LEFT 3": -3 , "RIGHT 1": 1, "RIGHT 2": 2, "RIGHT 3": 3} # copied from EightPuzzle class and changed to fit this problem
        neighbor = empty_chair + delta[action]
        new_state[empty_chair], new_state[neighbor] = new_state[neighbor], new_state[empty_chair]

        return tuple(new_state)
    
    def path_cost(self, c, state1, action, state2): # path cost is equal to number of seats moved
        if action == "LEFT 1" or action == "RIGHT 1":
            return c + 1
        elif action == "LEFT 2" or action == "RIGHT 2":
            return c + 2
        elif action == "LEFT 3" or action == "RIGHT 3":
            return c + 3

    def goal_test(self, state):
        return state == self.goal
    
    def h(self, node): # heuristic is number of misplace seats. This heuristic is admissible because it never overestimates the cost to reach the goal
        misplacedSeats = 0
        for i in range(len(node.state)):
            if node.state[i] != self.goal[i]:
                misplacedSeats += 1
        return misplacedSeats 
    
class GridWorldProblem(Problem):
    def __init__(self, initial=(1,1), goal=(3,2)):
        super().__init__(initial, goal)

    def actions(self, state): # defining actions (question swapped traditional x and y axis and it starts at 1,1 instead of 0,0)
        actions = []
        if state[0] < 3:
            actions.append("UP")
        if state[0] > 1:
            actions.append("DOWN")
        if state[1] > 1:
            actions.append("LEFT")
        if state[1] < 3:
            actions.append("RIGHT")
        return actions

    def result(self, state, action): # defining results
        if action == "UP":
            return (state[0] + 1, state[1])
        elif action == "DOWN":
            return (state[0] - 1, state[1])
        elif action == "LEFT":
            return (state[0], state[1] - 1)
        elif action == "RIGHT":
            return (state[0], state[1] + 1)

    def goal_test(self, state):
        return state == self.goal
    
    def path_cost(self, c, state1, action, state2): # defining path cost 
        return c + 1
    
    def curr_path_cost(self): # returns the current path cost
        return self.path_cost
    
    def h(self, node):
        distanceFromGoal = abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1])
        return distanceFromGoal
    
class GridAgent(SimpleProblemSolvingAgentProgram): 
    def formulate_goal(self, state):
        return (3,2)

    def formulate_problem(self, state, goal):
        return GridWorldProblem(state, goal)
    
    def search(self, problem):
        self.solution = ID_astar_search(problem)
        return ID_astar_search(problem)
    
    def print_solution(self):
        if self.solution:
            print("Search Tree:")
            for node in self.solution.path():
                print(node.state)
            print("Path Cost:", self.solution.path_cost)
            print("Actions:", self.solution.solution())
        else:
            print("No solution found.")
    
def ID_astar_search(problem, h=None, display = False): # search starts from initial state as stated in 1.4
    # current node of problem
    node = Node(problem.initial)

    for g in range(sys.maxsize):
        h = problem.h(node) # heuristic is the manhattan distance
        result = DL_astar_search(problem, g) # increases depth by one for each fail
        if result != 'cutoff':
            return result
        
def DL_astar_search(problem, limit = 1):
    display = False
    h = memoize(problem.h, 'h')
    return my_depth_limited_first_graph_search(problem, lambda n: n.path_cost + h(n), limit, display)

def my_depth_limited_first_graph_search(problem, f, limit = 1, display=False):
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        if limit <= 0: # if limit is reached, return cutoff
            return 'cutoff'
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node
        else:
            limit -= 1 # decrement limit
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None

if __name__ == "__main__":
    main()