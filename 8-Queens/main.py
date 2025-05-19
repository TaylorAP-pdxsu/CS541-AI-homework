from individual import Individual
import random
import time
import matplotlib.pyplot as plt


def genetic_algorithm(pop_size, generations, mutpct):
    population = [Individual(id=i, mutpct=mutpct) for i in range(pop_size)]

    best_fitness_history = []
    avg_fitness_history = []
    examples = []  # (worst, median, best) individuals each generation

    for gen in range(generations):
        total_fitness = sum(ind.fitness for ind in population)

        def select_one():
            pick = random.uniform(0, total_fitness)
            current = 0
            for ind in population:
                current += ind.fitness
                if current >= pick:
                    return ind

        new_population = []

        while len(new_population) < pop_size:
            mom = select_one()
            dad = select_one()

            split = random.randint(0, 7)

            child1 = Individual(mom=mom, dad=dad, split=split, mutpct=mutpct)
            child2 = Individual(mom=dad, dad=mom, split=split, mutpct=mutpct)

            new_population.append(child1)
            if len(new_population) < pop_size:
                new_population.append(child2)

        population = new_population

        fitnesses = [ind.fitness for ind in population]
        best_fitness = max(fitnesses)
        avg_fitness = sum(fitnesses) / len(fitnesses)

        best_fitness_history.append(best_fitness)
        avg_fitness_history.append(avg_fitness)

        sorted_pop = sorted(population, key=lambda ind: ind.fitness)
        worst = sorted_pop[0]
        median = sorted_pop[len(sorted_pop) // 2]
        best = sorted_pop[-1]

        examples.append((worst, median, best))

        print(f"Generation {gen+1} Best fitness: {best_fitness:.4f}")

        if best_fitness == 1:
            print("Solution found!")
            break

    return best_fitness_history, avg_fitness_history, examples


def main():
    pop_size = 1000
    generations = 20
    mutpct = 10

    best_fit_hist, avg_fit_hist, examples = genetic_algorithm(pop_size, generations, mutpct)

    # Plotting
    plt.plot(range(1, len(best_fit_hist) + 1), best_fit_hist, label='Best Fitness')
    plt.plot(range(1, len(avg_fit_hist) + 1), avg_fit_hist, label='Average Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Genetic Algorithm Fitness Over Generations')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Display example individuals from first 5 generations
    print("\nExample Individuals (Worst, Median, Best) from first 5 generations:\n")
    for gen_id, (worst, median, best) in enumerate(examples):
        if gen_id % 2 == 0 or gen_id == 0:
            print(f"Generation {gen_id + 1}:\n")
            print(f"fitness (worst, median, best): ({worst.fitness:.4f}, {median.fitness:.4f}, {best.fitness:.4f})")
            print("-" * 30)


if __name__ == "__main__":
    random.seed(time.time())
    main()
