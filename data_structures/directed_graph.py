import dataclasses
import typing
from collections import defaultdict


@dataclasses.dataclass
class Connection:
    vertex: 'Vertex'
    value: int


class Vertex:

    def __init__(self, name: str) -> None:
        self._name = name
        self._connections: list[Connection] = []

    def __str__(self) -> str:
        return f'[{self.name}]'

    def __hash__(self) -> int:
        return hash(self._name)

    @property
    def name(self) -> str:
        return self._name


class DirectedGraph:

    def __init__(self, vertices: typing.Iterable[Vertex] = ()):
        self._vertices: list[Vertex] = list(vertices)
        self._connections: typing.Mapping[Vertex, list[Connection]] = defaultdict(list)

    @property
    def vertices(self) -> list[Vertex]:
        return self._vertices

    def add_vertex(self, vertex: Vertex) -> None:
        self._vertices.append(vertex)

    def remove_vertex(self, vertex: Vertex) -> None:
        for graph_vertex in self.vertices[:]:
            if graph_vertex == vertex:
                self._vertices.remove(vertex)
                return
        else:
            print(f'There is no {vertex} vertex in the graph')

    def connect_vertices(self, from_: Vertex, to: Vertex, value: int):
        self._connections[from_].append(Connection(vertex=to, value=value))

    def print_graph(self) -> None:
        for vertex in self.vertices:
            print(f'Vertex {vertex} connections:')
            for connection in self._connections[vertex]:
                print(f'{vertex}---{connection.value}-->{connection.vertex}')
            print()

    def get_connections(self, vertex: Vertex) -> list[Connection]:
        return self._connections[vertex]


A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')

graph = DirectedGraph()
graph.add_vertex(A)
graph.add_vertex(B)
graph.add_vertex(C)
graph.add_vertex(D)

graph.connect_vertices(A, B, 5)
graph.connect_vertices(A, C, 3)
graph.connect_vertices(C, B, 1)
graph.connect_vertices(B, D, 2)
graph.connect_vertices(C, D, 7)

