from grafo import Graph
from OrderedVector import OrderedVector

class Greedy:
    def __init__(self, objective):
        self.objective = objective
        self.found = False

    def find(self, current):
        print('-------')
        print(f'current: {current.rotule}')
        current.visited = True

        if current == self.objective:
            self.found = True
        else:
            ordered_vector = OrderedVector(len(current.adjacent))
            for adjacent in current.adjacent:
                if adjacent.vertex.visited == False:
                    adjacent.vertex.visited == True
                    ordered_vector.insert(adjacent.vertex)
            ordered_vector.print()

            if ordered_vector.values[0] != None:
                self.find(ordered_vector.values[0])

graph = Graph()
vector = OrderedVector(5)
vector.insert(graph.arad)
vector.insert(graph.craiova)
vector.insert(graph.bucharest)
vector.insert(graph.dobreta)

vector.print()

vector.insert(graph.lugoj)

vector.print()

print(vector.values[0], vector.values[0].rotule)

print('----------')

greedy = Greedy(graph.bucharest)
greedy.find(graph.arad)