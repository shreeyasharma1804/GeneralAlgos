class dependency_resolution:

    def __init__(self):
        self.dependency_graph = {}
        self.indegrees = {}

    def add_dependency(self, b , a):
        if(b in self.dependency_graph):
            self.dependency_graph[b].append(a)
        else:
            self.dependency_graph[b] = [a]

        if(a in self.indegrees):
            self.indegrees[a] = self.indegrees[a]+1
        else:
            self.indegrees[a] = 1

    def resolve_dependencies(self, node, visited):
        if(node in visited):
            return
        if(node not in self.dependency_graph):
            visited[node] = 1
            return
        for nei in self.dependency_graph[node]:
            visited[node] = 1
            self.resolve_dependencies(nei, visited)

graph = dependency_resolution()
graph.add_dependency("B", "A")
graph.add_dependency("C", "A")
graph.add_dependency("E", "B")
graph.add_dependency("E", "C")
graph.add_dependency("F", "C")
graph.add_dependency("G", "B")
graph.add_dependency("G", "D")
graph.add_dependency("H", "F")
graph.add_dependency("H", "E")
graph.add_dependency("I", "G")

all_dependencies = {}
graph.resolve_dependencies('H', all_dependencies)
print(all_dependencies)
