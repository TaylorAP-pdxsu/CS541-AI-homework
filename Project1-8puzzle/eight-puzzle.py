from Grid import Grid
import Agent

def main():

    # best first h_1
    trials = 5
    sum_total = 0
    print(f"---Best First - misplaced---")
    for i in range(5):
        sum = 0
        grid = Grid(9)
        bf_h1 = Agent.Best_First(grid)
        bf_h1.solve_misplaced()
        sum += bf_h1.total_moves
        sum_total += sum
        print(f"Trial {i + 1} Turns: {sum}")
    print(f"Average Turns: {sum_total / trials}")


    print()
    # best first h_2
    sum_total = 0
    print(f"---Best First - manhttan---")
    for i in range(5):
        sum = 0
        grid = Grid(9)
        bf_h2 = Agent.Best_First(grid)
        bf_h2.solve_manhattan()
        sum += bf_h2.total_moves
        sum_total += sum
        print(f"Trial {i + 1} Turns: {sum}")
    print(f"Average Turns: {sum_total / trials}")


    print()
    # A* h_1
    sum_total = 0
    print(f"---A* - misplaced---")
    for i in range(5):
        sum = 0
        grid = Grid(9)
        as_h1 = Agent.A_star(grid)
        
        sum += as_h1.solve_misplaced()
        sum_total += sum
        print(f"Trial {i + 1} Turns: {sum}")
    print(f"Average Turns: {sum_total / trials}")


    print()
    # A* h_2
    sum_total = 0
    print(f"---A* - manhattan---")
    for i in range(5):
        sum = 0
        grid = Grid(9)
        as_h2 = Agent.A_star(grid)
        sum += as_h2.solve_manhattan()
        sum_total += sum
        print(f"Trial {i + 1} Turns: {sum}")
    print(f"Average Turns: {sum_total / trials}")

if __name__ == "__main__":
    main()
