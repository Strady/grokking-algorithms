import typing
from data_structures import DirectedGraph, Vertex
from objdict import ObjDict
from tabulate import tabulate


class DijkstraAlgorithmTable:

    def __init__(self, graph: DirectedGraph, start_vertex: Vertex) -> None:
        self._table = {vertex: ObjDict(cost=float('inf'), parent=None) for vertex in graph.vertices}
        self._table[start_vertex].cost = 0

    def print_table(self) -> None:
        raw_table = [[str(vertex), row.cost, str(row.parent)] for vertex, row in self._table.items()]
        print(tabulate(raw_table, headers=['Vertex', 'Cost', 'Parent']), end='\n\n')

    def get_cost(self, vertex: Vertex) -> typing.Union[int, float]:
        return self._table[vertex].cost

    def set_cost(self, vertex: Vertex, cost: int) -> None:
        self._table[vertex].cost = cost

    def get_parent(self, vertex: Vertex) -> typing.Optional[Vertex]:
        return self._table[vertex].parent

    def set_parent(self, vertex: Vertex, parent: Vertex) -> None:
        self._table[vertex].parent = parent

    @property
    def table(self) -> dict[Vertex, ObjDict]:
        return self._table

    def __iter__(self):
        return iter(self._table.items())


class DijkstraAlgorithmRunner:

    def __init__(self, graph: DirectedGraph):
        self._graph: DirectedGraph = graph
        self._table: typing.Optional[DijkstraAlgorithmTable] = None
        self._processed: list[Vertex] = []

    def process_graph(self, start_vertex: Vertex) -> None:
        self._table = DijkstraAlgorithmTable(graph=self._graph, start_vertex=start_vertex)
        self._processed.clear()
        print('Initial table state:')
        self._table.print_table()
        processing_vertex = self._find_lowest_cost_node()
        while processing_vertex is not None:
            print(f'\x1b[1;33mProcessing vertex {processing_vertex}.\x1b[0m', end='\n\n')

            cost = self._table.get_cost(vertex=processing_vertex)
            for connection in self._graph.get_connections(vertex=processing_vertex):
                print(f'Calculating new cost for vertex {connection.vertex}')
                new_cost = cost + connection.value
                prev_cost = self._table.get_cost(connection.vertex)
                print(f'New cost is {new_cost}, previous cost is {prev_cost}')
                if prev_cost > new_cost:
                    print('\x1b[1;36mNew cost is less than previous one.\x1b[0m')
                    print(f'Changing vertex {connection.vertex} parent '
                          f'from {self._table.get_parent(connection.vertex)} to {processing_vertex}.')
                    print(f'Changing cost from {prev_cost} to {new_cost}.')
                    print()
                    self._table.set_cost(vertex=connection.vertex, cost=new_cost)
                    self._table.set_parent(vertex=connection.vertex, parent=processing_vertex)
            self._processed.append(processing_vertex)
            processing_vertex = self._find_lowest_cost_node()
            print('Resulting table:')
            self._table.print_table()
        print(f'\x1b[1;32mGraph processing for starting vertex {start_vertex} is finished.\x1b[0m')

    def _find_lowest_cost_node(self) -> typing.Optional[Vertex]:
        lowest_cost = float('inf')
        min_vertex = None
        for vertex, row in self._table:
            if vertex not in self._processed and row.cost < lowest_cost:
                lowest_cost = row.cost
                min_vertex = vertex
        return min_vertex

    def print_route(self, start: Vertex, finish: Vertex):
        if start == finish:
            print('Start and finish can not be at the same vertex!')
            return

        processing_vertex = finish
        route = []
        while processing_vertex is not None:
            route.append(processing_vertex)
            parent = self._table.get_parent(processing_vertex)
            processing_vertex = parent

        print('->'.join(str(vertex) for vertex in reversed(route)))


# Example 1

start = Vertex('START')
a = Vertex('A')
b = Vertex('B')
finish = Vertex('FINISH')

graph = DirectedGraph(vertices=(start, a, b, finish))
graph.connect_vertices(start, a, 6)
graph.connect_vertices(start, b, 2)
graph.connect_vertices(a, finish, 1)
graph.connect_vertices(b, a, 3)
graph.connect_vertices(b, finish, 5)

alg_runner = DijkstraAlgorithmRunner(graph=graph)
alg_runner.process_graph(start_vertex=start)
alg_runner.print_route(start=start, finish=finish)


# Example 2

start = Vertex('START')
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
finish = Vertex('FINISH')

graph = DirectedGraph(vertices=(start, a, b, c, d, finish))
graph.connect_vertices(start, a, 5)
graph.connect_vertices(start, c, 2)
graph.connect_vertices(c, a, 8)
graph.connect_vertices(a, b, 4)
graph.connect_vertices(c, d, 7)
graph.connect_vertices(a, d, 2)
graph.connect_vertices(b, d, 6)
graph.connect_vertices(b, finish, 3)
graph.connect_vertices(d, finish, 1)

alg_runner = DijkstraAlgorithmRunner(graph=graph)
alg_runner.process_graph(start_vertex=start)
alg_runner.print_route(start=start, finish=finish)


# Example 3

start = Vertex('START')
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
finish = Vertex('FINISH')

graph = DirectedGraph(vertices=(start, a, b, c, finish))
graph.connect_vertices(start, a, 10)
graph.connect_vertices(a, b, 20)
graph.connect_vertices(b, finish, 30)
graph.connect_vertices(b, c, 1)
graph.connect_vertices(c, a, 1)

alg_runner = DijkstraAlgorithmRunner(graph=graph)
alg_runner.process_graph(start_vertex=start)
alg_runner.print_route(start=start, finish=finish)

