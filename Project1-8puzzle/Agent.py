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
        self.stop = 500
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

        return self.total_moves
        
    def solve_manhattan(self):
        self.heuristic = self.manhattan_dist
        while self.move() != 0 and self.total_moves < self.stop:
            self.total_moves += 1


class A_star(Agent):
    def __init__(self, world):
        super().__init__(world)
        self.pq = []

    def move(self) -> int:
        # Tree node (parent, state/world, pos, g, h)
        root = PathNode(None, copy.deepcopy(self.world), self.currPos, 0, self.heuristic(self.world), 0)
        heapq.heappush(self.pq, root)

        for node in self.world.grid[self.currPos].adjacent:
            copy_world = copy.deepcopy(self.world)
            copy_world.grid[self.currPos].value = copy_world.grid[node.pos].value
            copy_world.grid[node.pos].value = 'b'
            root.children.append(PathNode(root, copy_world, node.pos, root.f, self.heuristic(copy_world), 1))
            heapq.heappush(self.pq, root.children[-1])

        return self.pathing(heapq.heappop(self.pq))

    def pathing(self, root) -> int:

        for node in root.state_world.grid[root.agentPos].adjacent:
            copy_world = copy.deepcopy(self.world)
            copy_world.grid[self.currPos].value = copy_world.grid[node.pos].value
            copy_world.grid[node.pos].value = 'b'
            root.children.append(PathNode(root, copy_world, node.pos, root.f, self.heuristic(copy_world), root.turns + 1))
            heapq.heappush(self.pq, root.children[-1])

        self.total_moves += 1
        if self.total_moves > self.stop:
            return root.turns
        
        if root.h == 0:
            return root.turns
        
        return self.pathing(heapq.heappop(self.pq))

    def solve_misplaced(self) -> int:
        self.heuristic = self.misplaced_tiles
        return self.move()

    def solve_manhattan(self) -> int:
        self.heuristic = self.manhattan_dist
        return self.move()
        
        