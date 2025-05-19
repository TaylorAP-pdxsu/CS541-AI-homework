import random
import time

class Individual:
    def __init__(self, id=0, mom=None, dad=None, split=0, mutpct=0):
        # Now gene_code is a dict: queen_id -> (x, y)
        self.gene_code = {}

        if mom and dad:
            self.id = str(mom.id) + str(dad.id)
            self.crossover(mom, dad, split)
            if random.random() < (mutpct / 100.0):
                self.mutate()
        else:
            self.id = str(id)

        if not (mom and dad):  # Only randomize if not offspring
            self.randomize_queens()

        self.fitness = self.calc_fitness()

    def randomize_queens(self):
        for queen_id in range(8):
            if queen_id in self.gene_code:
                continue
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if (x, y) not in self.gene_code.values():
                    break
            self.gene_code[queen_id] = (x, y)

    def crossover(self, mom, dad, split):
        self.gene_code = ({q_id: pos for q_id, pos in mom.gene_code.items() if 0 <= q_id <= split}
                            | {q_id: pos for q_id, pos in dad.gene_code.items() if split < q_id < 8})
        if len(self.gene_code) < 8: # we had a conflict so size is less than 8
            self.randomize_queens()

    def mutate(self):
        gene_id = random.randint(0, 7)
        while True:
            pos = (random.randint(0,7), random.randint(0,7))
            if pos not in self.gene_code.values():
                self.gene_code[gene_id] = pos
                break

    def calc_fitness(self) -> int:
        conflicts = 0
        queens_positions = list(self.gene_code.values())

        for i, (x1, y1) in enumerate(queens_positions):
            for j, (x2, y2) in enumerate(queens_positions):
                if i == j:
                    continue
                if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                    conflicts += 1

        # Each conflict counted twice (queen A vs queen B and queen B vs queen A)
        return 1 / (1 + conflicts // 2)

    def display(self):
        # Build the board as a list of strings
        board = [['-' for _ in range(8)] for _ in range(8)]

        for (x, y) in self.gene_code.values():
            board[y][x] = 'Q'

        for y in range(8):
            print(f"{y} | " + ' '.join(board[y]))

        print("    _______________")
        print("    0 1 2 3 4 5 6 7")
        print(f"Fitness = {self.fitness}")
