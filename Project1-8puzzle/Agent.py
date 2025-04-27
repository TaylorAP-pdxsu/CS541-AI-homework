from Grid import Grid
from Node import Node
from PathNode import PathNode
from typing import Callable
import numpy as np
import copy
import heapq

# heuristics -
# -- number of misplaced tiles
# -- total manhattan distance

class Agent:
    def __init__(self, world:Grid):
        self.world:Grid = world
        self.startPos: str = world.find_blank()
        self.currPos: str = self.startPos
        self.total_moves = 0
        self.stop = 10
        self.heuristic: Callable
        self.prev_cost = 0

    def calc_cost(self, world) -> int:
        return self.heuristic(world) + self.prev_cost
    
    def display(self):
        print(f"Start: {self.startPos}")
        print(f"Curr: {self.currPos}")

    def misplaced_tiles(self, world):
        count = 0
        for node in world.grid:
            if node.in_position() == False:
                count += 1
        return count
    
    def manhattan_dist(self, world) -> int:
        dist = 0
        for node in world.grid:
            if node.value == 'b':
                continue
            if node.in_position() == True:
                continue
            coord = world.find_coord(node.value)
            dist += np.abs(node.coord[0] - coord[0]) + np.abs(node.coord[1] - coord[1])
        return dist

class Best_First(Agent):
    def __init__(self, world):
        super().__init__(world)

    def move(self) -> int:
        world_copies = {}
        best_move = (self.world.grid[self.currPos].adjacent[0], 100)
        cost = 0

        for node in self.world.grid[self.currPos].adjacent:
            # set dict
            world_copies[node.pos] = copy.deepcopy(self.world)
            #set curr pos's value to move pos's value
            world_copies[node.pos].grid[self.currPos].value = world_copies[node.pos].grid[node.pos].value
            #set move pos's value to b
            world_copies[node.pos].grid[node.pos].value = 'b'
            cost = self.calc_cost(world_copies[node.pos])
            print(f"Path - {node.pos}, {cost}")
            if cost < best_move[1]:
                best_move = (node, cost)
        
        self.world.grid[self.currPos].value = self.world.grid[best_move[0].pos].value
        self.world.grid[best_move[0].pos].value = 'b'
        self.currPos = best_move[0].pos
        return cost
    
    def solve_misplaced(self):
        self.heuristic = self.misplaced_tiles
        while self.move() != 0 and self.total_moves < self.stop:
            self.total_moves += 1
            print(f"Turn: {self.total_moves}")
            print()
            self.world.display()
            print("----------------------")
        
    def solve_manhattan(self):
        self.heuristic = self.manhattan_dist
        while self.move() != 0 and self.total_moves < self.stop:
            self.total_moves += 1
            print(f"Turn: {self.total_moves}")
            print()
            self.world.display()
            print("----------------------")

class A_star(Agent):
    def __init__(self, world):
        super().__init__(world)

    def move(self) -> int:
        pq = []
        root = PathNode(None, copy.deepcopy(self.world), 0, self.heuristic(self.world))
        heapq.heappush(pq, root)

        for node in root.children:
