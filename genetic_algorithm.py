'''
Knapsack problem, we have weights and values 
weights = constraint
values = optimize

What we need
-> a genetic representation of a solution
-> a function to generate new solutions
-> fitness function: to check the fitness of a genome
-> select function: select the genomes to generate the next generation
-> crossover function: to modify two genomes
-> mutation function: mutates a genome

'''

import time
from functools import partial
from collections import namedtuple
from typing import List, Callable, Tuple
from random import choices, randint, randrange, random

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]               # whats callable?
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFUnc = Callable[[Genome], Genome]
Thing = namedtuple('Thing', ['name', 'value', 'weight'])


# value is relative, weight in gms
things = [
    Thing('Laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee Mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192)
]

more_things = [
    Thing('Mint', 5, 25),
    Thing('Socks', 10, 38),
    Thing('Tissues', 15, 80),
    Thing('Phone', 500, 200),
    Thing('Baseball Cap', 100, 70),
] + things


# generate random population
def generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)

def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

# custom fitness function for knapsack problem
def fitness(genome: Genome, things, weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of same length")
    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i]==1:
            weight += thing.weight
            value += thing.value

        if weight>weight_limit:
            return 0
    return value

# select best two pairs
def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    )

# crossover function, splits at random length and swaps
def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length") # should not be faced in our implementation
    length = len(a)
    if length < 2:
        return a, b
    p = randint(1, len(a)-1)
    return a[:p] + b[p:], b[:p] + a[p:]

# mutation function, num = number of mutationss
def mutation(genome: Genome, num: int=1, probability: float=0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else 1 - genome[index]
    return genome


# main evolution
def run_evolution(
    populate_func: PopulateFunc,
    fitness_func: FitnessFunc,
    fitness_limit: int,             # if our solution exceed this limits then we stop the evolution
    selection_func: SelectionFunc = selection_pair,
    crossover_func: CrossoverFunc = single_point_crossover,
    mutation_func: MutationFUnc = mutation,
    generation_limit: int = 100,
) -> Tuple[Population, int]:
    
    population = populate_func()
    for i in range(generation_limit):
        population = sorted(
            population,
            key = lambda genome: fitness_func(genome),
            reverse=True            # try with false here
        )
        if fitness_func(population[0]) >= fitness_limit:
            break

        # elitism, add best two genomes to next generation, survival of fittest
        next_generation = population[0:2]

        # need (n-2)/2 parents to produce next n genomes
        for j in range(int(len(population)/2) - 1):
            parents = selection_func(population, fitness_func)      # aren't we selection same best two parents here?
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]
    
        population = next_generation

    population = sorted(
        population,
        key = lambda genome: fitness_func(genome),
        reverse=True           
    )
    return population, i


start = time.time()
population, generations = run_evolution(
    populate_func = partial(
        generate_population, size=10, genome_length=len(more_things)
    ),
    fitness_func=partial(
        fitness, things=more_things, weight_limit=3000
    ),
    fitness_limit=1310, # pre calculated for this problem
    generation_limit=100
)
end = time.time()

def genome_to_things(genome: Genome, things):
    result = []
    for i, thing in enumerate(things):
        if genome[i]==1:
            result += [thing.name]
    return result

print(f"number of generations: {generations}")
print(f"time: {end - start}s")
print(f"best solution: {genome_to_things(population[0], more_things)}")