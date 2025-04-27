from Grid import Grid
from Node import Node
from typing import Callable

# heuristics -
# -- number of misplaced tiles
# -- total manhattan distance

class Agent:
    def __init__(self, world:Grid):
        self.world:Grid = world
        self.startPos: str = world.find_blank()
        self.currPos: str = self.startPos
        self.heuristic: Callable
        self.next_cost: Callable

    def calc_cost(self) -> int:
        return self.heuristic() + self.next_cost()
    
    def display(self):
        print(f"Start: {self.startPos}")
        print(f"Curr: {self.currPos}")

    def misplaced_tiles(self):
        count = 0
        for i in self.world.grid:
            if self.world.grid[i].in_position() == False:
                count += 1
        return count
    
    def manhattan_dist(self):
        

class Best_First(Agent):
    def __init__(self, world):
        super().__init__(world)

