import numpy as np

class Vertex:
    def __init__(self, rotule, distance_objective):
        self.rotule = rotule
        self.visited = False
        self.adjacent = []
        self.distance_objective = distance_objective

    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        print(f'\nAdjacent cities to {self.rotule}')
        for i in self.adjacent:
            print(i.vertex.rotule, i.cost)

class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        self.distanceAstar = vertex.distance_objective + self.cost

#The same as the one in grafo.py, just to keep everything separated
class Graph:
    arad = Vertex('Arad', 366)
    zerind = Vertex('Zerind', 374)
    oradea = Vertex('Oradea', 380)
    sibiu = Vertex('Sibiu', 253)
    timisoara = Vertex('Timisoara', 329)
    lugoj = Vertex('Lugoj', 244)
    mehadia = Vertex('Mehadia', 241)
    dobreta = Vertex('Dobreta', 242)
    craiova = Vertex('Craiova', 160)
    rimnicu = Vertex('Rimnicu', 193)
    fagaras = Vertex('Fagaras', 178)
    pitesti = Vertex('Pitesti', 98)
    bucharest = Vertex('Bucharest', 0)
    giurgiu = Vertex('Giurgiu', 77)

    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad,75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))
    sibiu.add_adjacent(Adjacent(arad, 140))
    
    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(rimnicu, 146))
    craiova.add_adjacent(Adjacent(pitesti, 138))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(bucharest, 101))
    pitesti.add_adjacent(Adjacent(craiova, 138))

    rimnicu.add_adjacent(Adjacent(pitesti, 97))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(craiova, 146))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))


class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    # O(n)
    def print(self):
        if(self.last_position == -1):
            print('Vector is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i].vertex.rotule, ' - ',
                self.values[i].cost, ' - ',
                self.values[i].vertex.distance_objective, ' - ',
                self.values[i].distanceAstar)

    #O(n)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity')
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].distanceAstar > value.distanceAstar:
                break
            if i==self.last_position:
                position = i+1;
            
        x = self.last_position
        while x >= position:
            self.values[x+1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1

class AStar:
    def __init__(self, objective):
        self.objective = objective
        self.found = False

    def find(self, current):
        print('---------')
        print(f'Current: {current.rotule}')
        current.visited = True

        if current == self.objective:
            self.found = True
        else:
            ordered_vector = OrderedVector(len(current.adjacent))
            for adjacent in current.adjacent:
                if adjacent.vertex.visited == False:
                    adjacent.visited = True
                    ordered_vector.insert(adjacent)
            ordered_vector.print()

            if ordered_vector.values[0] != None:
                self.find(ordered_vector.values[0].vertex)


# testes
graph = Graph()
print(graph.arad.adjacent[0].vertex.rotule, graph.arad.adjacent[0].vertex.distance_objective)
print(graph.arad.adjacent[0].distanceAstar, graph.arad.adjacent[0].cost)

vector = OrderedVector(3)
vector.insert(graph.arad.adjacent[0])
vector.insert(graph.arad.adjacent[1])
vector.insert(graph.arad.adjacent[2])

vector.print()

Astar = AStar(graph.bucharest)
Astar.find(graph.arad)