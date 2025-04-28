from Grid import Grid

class PathNode:
    def __init__(self, parent, state, pos, g, h, turns):
        self.parent = parent
        self.children = []
        self.agentPos = pos
        self.state_world:Grid = state
        self.turns = turns
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f