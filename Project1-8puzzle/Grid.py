import numpy as np
import random
from Node import Node

class Grid:
    def __init__(self, size):
        self.numSize = size
        numbers = ["b", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.grid = []
        y_coord = 0
        for i in range(self.numSize):
            index = random.randint(0, self.numSize-1)
            self.grid.append(Node(i, numbers[index], (i % 3, y_coord)))
            del numbers[index]
            self.numSize -= 1
            y_coord = y_coord + 1 if (i + 1) % 3 == 0 else y_coord

        # top-left node
        self.grid[0].add_edge(self.grid[1])
        self.grid[0].add_edge(self.grid[3])
        #top-mid node
        self.grid[1].add_edge(self.grid[0])
        self.grid[1].add_edge(self.grid[2])
        self.grid[1].add_edge(self.grid[4])
        #top-right
        self.grid[2].add_edge(self.grid[1])
        self.grid[2].add_edge(self.grid[5])
        #mid-left
        self.grid[3].add_edge(self.grid[0])
        self.grid[3].add_edge(self.grid[4])
        self.grid[3].add_edge(self.grid[6])
        #mid-mid
        self.grid[4].add_edge(self.grid[3])
        self.grid[4].add_edge(self.grid[1])
        self.grid[4].add_edge(self.grid[5])
        self.grid[4].add_edge(self.grid[7])
        #mid-right
        self.grid[5].add_edge(self.grid[2])
        self.grid[5].add_edge(self.grid[8])
        self.grid[5].add_edge(self.grid[4])
        #bot-left
        self.grid[6].add_edge(self.grid[3])
        self.grid[6].add_edge(self.grid[7])
        #bot-mid
        self.grid[7].add_edge(self.grid[6])
        self.grid[7].add_edge(self.grid[4])
        self.grid[7].add_edge(self.grid[8])
        #bot-right
        self.grid[8].add_edge(self.grid[7])
        self.grid[8].add_edge(self.grid[5])

    def display(self):
        print(f"[pos, value]")
        print(f"[{self.grid[0].pos}|{self.grid[0].coord}|{self.grid[0].value}] [{self.grid[1].pos}|{self.grid[1].coord}|{self.grid[1].value}] [{self.grid[2].pos}|{self.grid[2].coord}|{self.grid[2].value}]")
        print()
        print(f"[{self.grid[3].pos}|{self.grid[3].coord}|{self.grid[3].value}] [{self.grid[4].pos}|{self.grid[4].coord}|{self.grid[4].value}] [{self.grid[5].pos}|{self.grid[5].coord}|{self.grid[5].value}]")
        print()
        print(f"[{self.grid[6].pos}|{self.grid[6].coord}|{self.grid[6].value}] [{self.grid[7].pos}|{self.grid[7].coord}|{self.grid[7].value}] [{self.grid[8].pos}|{self.grid[8].coord}|{self.grid[8].value}]")

    def display_adj_list(self):
        for i in range(self.numSize):
            print(f"Node({self.grid[i].pos}, {self.grid[i].value}): {self.grid[i].display_adj_list()}")

    def find_blank(self) -> str:
        for node in self.grid:
            if node.value == 'b':
                return node.pos
            
    def find_coord(self, value) -> tuple[int,int]:
        for node in self.grid:
            if str(node.pos) == value:
                return node.coord
        return node.coord