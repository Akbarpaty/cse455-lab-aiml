import random

num_items = 8
bin_capacity = 10
population_size = 6
generations = 10
mutation_rate = 0.1

items = [random.randint(1, 9) for _ in range(num_items)]

def initialize_population():
    return [[random.randint(0, num_items - 1) for _ in range(num_items)] for _ in range(population_size)]

def fitness(chromosome):
    bins = [[] for _ in range(num_items)]
    for i, bin_num in enumerate(chromosome):
        bins[bin_num].append(items[i])
    
    bins = [b for b in bins if sum(b) <= bin_capacity and b]
    return len(bins)  
def select_parent(population):
    total_fitness = sum(1 / (fitness(chromo) + 1) for chromo in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chromo in population:
        current += 1 / (fitness(chromo) + 1)
        if current > pick:
            return chromo
    return population[-1]
def crossover(parent1, parent2):
    point = random.randint(1, num_items - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2
def mutate(chromosome):
    if random.random() < mutation_rate:
        index = random.randint(0, num_items - 1)
        chromosome[index] = random.randint(0, num_items - 1)
    return chromosome
population = initialize_population()
for _ in range(generations):
    population = sorted(population, key=fitness)
    new_population = population[:2]
    while len(new_population) < population_size:
        parent1, parent2 = select_parent(population), select_parent(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])
    population = new_population

best_solution = min(population, key=fitness)
print("Best Bin Packing:", best_solution)
print("Minimum Bins Used:", fitness(best_solution))
