from Grid import Grid
import Agent

def main():
    
    grid = Grid(9)
    grid.display()
    print()

    agent = Agent.Best_First(grid)
    print(f"misplaced: {agent.misplaced_tiles(grid)}")
    print(f"distance: {agent.manhattan_dist(grid)}")

    print()
    print(f"---Manhattan---")
    agent.solve_manhattan()

    print(f"Total Moves: {agent.total_moves}")

if __name__ == "__main__":
    main()
