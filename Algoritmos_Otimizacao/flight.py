import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

people = [
    ('Lisboa', 'LIS'),
    ('Madrid', 'MAD'),
    ('Paris', 'CDG'),
    ('Dublin', 'DUB'),
    ('Bruexelas', 'BRU'),
    ('Londres', 'LHR')
]

destiny = 'FCO'

# flights = {('BRU', 'FCO'): ['15:44', '18:55', 382]}
flights = {}
for line in open('Algoritmos_Otimizacao/flights.txt'):
    # print(line.split(','))
    origin, destiny, departure, arrival, price = line.split(',')
    flights.setdefault((origin, destiny), [])
    flights[(origin, destiny)].append((departure, arrival, int(price)))

# functions
#schedule = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3] # example of solution
def print_flights(schedule):
    id_flight = -1
    total_price = 0
    for i in range(len(schedule) // 2):
        name = people[i][0]
        origin = people[i][1]
        id_flight += 1
        going = flights[(origin, destiny)][schedule[id_flight]]
        total_price += going[2]
        id_flight +=1
        returning = flights[(destiny, origin)][schedule[id_flight]]
        total_price += returning[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (name, origin, going[0], going[1], going[2], returning[0], returning[1], returning[2]))
        print('Total price: ', total_price)

# print_flights(schedule)

def fitness_function(schedule):
    id_flight = -1
    total_price = 0
    for i in range(len(schedule) // 2):
        origin = people[i][1]
        id_flight += 1
        going = flights[(origin, destiny)][schedule[id_flight]]
        total_price += going[2]
        id_flight +=1
        returning = flights[(destiny, origin)][schedule[id_flight]]
        total_price += returning[2]

    return total_price

#print(fitness_function(schedule))

fitness = mlrose.CustomFitness(fitness_function)
problem = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

#HILL CLIMB
print('Hill Climb solution: ')
best_solution, best_price = mlrose.hill_climb(problem, random_state=3)
print(best_solution, best_price)
print_flights(best_solution)
print('------------')

#SIMULATED ANNEALING
print('Simulated annaling solution: ')
best_solution, best_price = mlrose.simulated_annealing(problem, schedule=mlrose.decay.GeomDecay(init_temp=10000), random_state=1)
print(best_solution, best_price)
print_flights(best_solution)
print('------------')

#GENETIC ALGORITHM
print('Genetic Alg solution: ')
best_solution, best_price = mlrose.genetic_alg(problem, pop_size=500, mutation_prob=0.2, random_state=1)
print(best_solution, best_price)
print_flights(best_solution)
print('------------')