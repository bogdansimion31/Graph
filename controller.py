

class Controller:

    def __init__(self,repo):
        self._repo=repo

    def get_start_times(self):
        return self._repo.get_start_times()

    def get_end_times(self):
        return self._repo.get_end_times()

    def calculate(self,sorted_list):
        self._repo.calculate_time(sorted_list)

    def generate_random_graph(self,number_of_vertices,number_of_edges):
        self._repo.generate_random_graph(number_of_vertices,number_of_edges)

    def read_activities(self, filename):
        self._repo.read_activities(filename)

    def read_graph(self,filename):
        self._repo.read_graph(filename)

    def write_graph(self,filename):
        self._repo.write_graph(filename)

    def get_number_vertices(self):
        return self._repo.get_number_vertices()

    def is_edge(self,x,y):
        return self._repo.is_Edge(x,y)

    def get_in_degree(self,x):
        return self._repo.get_in_degree(x)

    def get_out_degree(self,x):
        return self._repo.get_out_degree(x)

    def get_edge_value(self,x,y):
        return self._repo.get_edge_value(x,y)

    def modify_edge_value(self,x,y,new):
        self._repo.modify_edge_value(x,y,new)

    def add_edge(self,x,y,value):
        self._repo.add_Edge(x,y,value)

    def remove_edge(self,x,y):
        self._repo.remove_edge(x,y)

    def add_vertex(self,x):
        self._repo.add_vertex(x)

    def remove_vertex(self,x):
        self._repo.remove_vertex(x)

    def parse_nIn(self,x):
        return self._repo.parse_Nin(x)

    def parse_nOut(self,x):
        return self._repo.parse_Nout(x)

    def find_shortest_path(self, x, y):
        return self._repo.find_shortest_path(x,y)

    def find_lowestCostWalk_FloydWarshall(self,x,y):
        if self._repo._distance!={}:
            return self._repo.find_lowestCostWalk_FloydWarshall(x,y)
        else:
            return self._repo.build_lowestCostWalk_FloydWarshall(x,y)

    def topo_sort(self):
        return self._repo.tarjan_algorithm()
