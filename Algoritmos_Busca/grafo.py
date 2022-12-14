#Creating city map

from cmath import pi

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

#testing
graph = Graph()

