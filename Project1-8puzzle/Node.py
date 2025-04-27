

class Node:
    def __init__(self, pos, value, coord: tuple[int, int]):
        self.pos = pos
        self.coord = coord
        self.value = value
        self.adjacent = []
        self.hCost = 0

    def add_edge(self, node:"Node"):
        self.adjacent.append(node)

    def display_adj_list(self) -> str:
        line = ""
        for i in range(len(self.adjacent)):
            line += f"[{self.adjacent[i].pos}, {self.adjacent[i].value}] -> "
        return line
    
    def in_position(self) -> bool:
        if self.value == 'b':
            return True
        if str(self.pos) == self.value:
            return True
        return False