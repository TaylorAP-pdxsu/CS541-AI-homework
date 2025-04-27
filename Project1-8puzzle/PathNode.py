

class PathNode:
    def __init__(self, parent, state, g, h):
        self.parent = parent
        self.children = []
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f