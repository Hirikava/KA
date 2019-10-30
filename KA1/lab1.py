
class Edge:
    def __init__(self,dst1,dst2,weight):
        self.vr1 = dst1
        self.vr2 = dst2
        self.weight = weight

    def __eq__(self, other):
        return (self.vr1 == other.vr1 and self.vr2 == other.vr2) or (self.vr2 == other.vr1 and self.vr1 == other.vr2)


edgies = list()
with open("in.txt") as file:
    countOfVertices = int(file.readline())
    for i in range(0,countOfVertices):
        tokens = file.readline().split(' ')
        j = 0
        while int(tokens[j]) != 0:
            newEdge = Edge(i,int(tokens[j]) - 1,int(tokens[j + 1]))
            if newEdge not in edgies:
                edgies.append(newEdge)
            j += 2

areas = list()
for i in range(0,countOfVertices):
    areas.append(i)

list_of_adjacency = dict()
for i in range(0,countOfVertices):
    list_of_adjacency[i] = list()

edgies.sort(key=lambda x: x.weight)
sum = 0
for edge in edgies:
    if(areas[edge.vr1] != areas[edge.vr2]):
        for areas_descriptor in areas:
            if(areas[areas_descriptor] == areas[edge.vr1]):
                areas[areas_descriptor] = areas[edge.vr2]
        list_of_adjacency[edge.vr1].append(edge.vr2)
        list_of_adjacency[edge.vr2].append(edge.vr1)
        sum += edge.weight

for i in range(0,countOfVertices):
    list_of_adjacency[i].sort(key=lambda x:x)

with open('out.txt','w') as file:
    for i in list_of_adjacency:
        file.write(str(i + 1)+":")
        for j in list_of_adjacency[i]:
            file.write(' ')
            file.write(str(j + 1))
        file.write('\n')
    file.write(str(sum))



