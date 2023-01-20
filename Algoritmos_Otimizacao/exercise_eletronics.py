import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

eletronics = [
    ('Refrigerator A', 0.751, 999.90),
    ('Smartphone', 0.0000899, 2199.12),
    ('TV 55', 0.400, 4346.99),
    ('TV 50', 0.290, 3999.90),
    ('TV 42', 0.200, 2999.90),
    ('Notebook A', 0.00350, 2499.90),
    ('Fan', 0.496, 199.90),
    ('MicroWave A', 0.0424, 308.66),
    ('MicroWave B', 0.0544, 429.90),
    ('MicroWave C', 0.0319, 299.29),
    ('Refrigerator B', 0.635, 849.00),
    ('Refrigerator C', 0.870, 1199.89),
    ('Notebook B', 0.498, 1999.90),
    ('Notebook C', 0.527, 3999.00),
    
]

max_size = 3

selected = {}
# functions
#selection = [0, 1, 1, 1, 1 ... ] # example of solution
def print_result(selection):
    for i in range(len(selection)):
        if selection[i] == 1:
            print('%s - %s' % (eletronics[i][0], eletronics[i][2]))

def fitness_function(selection):
    total_size = 0
    total_value = 0
    for i in range(len(selection)):
        if selection[i] == 1:
            total_size += eletronics[i][1]
            total_value += eletronics[i][2]
    if total_size > max_size:
        total_value = 1
    return total_value

#print(fitness_function(schedule))

fitness = mlrose.CustomFitness(fitness_function)
problem = mlrose.DiscreteOpt(length=14, fitness_fn=fitness, maximize=True, max_val=2)

#HILL CLIMB
print('Hill Climb solution: ')
best_solution, best_price = mlrose.hill_climb(problem, random_state=3)
print(best_solution, best_price)
print_result(best_solution)
print('------------')

#SIMULATED ANNEALING
print('Simulated annaling solution: ')
best_solution, best_price = mlrose.simulated_annealing(problem, schedule=mlrose.decay.GeomDecay(init_temp=10000), random_state=1)
print(best_solution, best_price)
print_result(best_solution)
print('------------')

#GENETIC ALGORITHM
print('Genetic Alg solution: ')
best_solution, best_price = mlrose.genetic_alg(problem, pop_size=500, mutation_prob=0.2)
print(best_solution, best_price)
print_result(best_solution)
print('------------')