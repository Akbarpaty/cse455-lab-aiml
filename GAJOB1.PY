import random

num_jobs = 5
num_machines = 3
population_size = 6
generations = 10
mutation_rate = 0.1

processing_times = [random.randint(1, 10) for _ in range(num_jobs)]

def initialize_population():
    return [[random.randint(0, num_machines - 1) for _ in range(num_jobs)] for _ in range(population_size)]

def fitness(chromosome):
    machine_loads = [0] * num_machines
    for job, machine in enumerate(chromosome):
        machine_loads[machine] += processing_times[job]
    return max(machine_loads) 

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
    point1, point2 = sorted(random.sample(range(num_jobs), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def mutate(chromosome):
    if random.random() < mutation_rate:
        index = random.randint(0, num_jobs - 1)
        chromosome[index] = random.randint(0, num_machines - 1)
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


best_schedule = min(population, key=fitness)
print("Best Job Schedule:", best_schedule)
print("Minimum Completion Time:", fitness(best_schedule))
