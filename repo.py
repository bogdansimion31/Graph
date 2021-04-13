from random import *
import copy

class Graph:
    def __init__(self):
        self._dictOut = {}
        self._dictIn = {}
        self._number_vertices = 0
        self._number_edges = 0
        self._distance = {}
        self._path_dict = {}
        self._start_times = {}
        self._end_times = {}
        self._previous_activities = {}
        self._required_times = {}

    def get_start_times(self):
        start_times=copy.deepcopy(self._start_times)
        return start_times

    def get_end_times(self):
        end_times=copy.deepcopy(self._end_times)
        return end_times

    def calculate_time(self, sorted_vertices):
        self._start_times[sorted_vertices[0]] = [self._required_times[sorted_vertices[0]],self._required_times[sorted_vertices[0]]]

        for index in range(1,len(sorted_vertices)):
            self._start_times[sorted_vertices[index]] = []
            maxi = 0
            for index2 in self._dictIn[sorted_vertices[index]]:
                if index2[0] in self._start_times:
                    if maxi < self._start_times[index2[0]][1]:
                        maxi = self._start_times[index2[0]][1]
            self._start_times[sorted_vertices[index]].append(maxi)
            self._start_times[sorted_vertices[index]].append(maxi+self._required_times[sorted_vertices[index]])

        self._end_times[sorted_vertices[-1]] = [self._start_times[sorted_vertices[-1]][1]-self._required_times[sorted_vertices[-1]],self._start_times[sorted_vertices[-1]][1]]
        for index in range(len(sorted_vertices)-2,0,-1):
            self._end_times[sorted_vertices[index]] = []
            mini = 999999
            for index2 in self._dictOut[sorted_vertices[index]]:
                if index2[0] in self._end_times:
                    if mini > self._end_times[index2[0]][0]:
                        mini = self._end_times[index2[0]][0]
            self._end_times[sorted_vertices[index]].append(mini-self._required_times[sorted_vertices[index]])
            self._end_times[sorted_vertices[index]].append(mini)

    def topo_sort_dfs(self, current_vertex, sorted_list, fully_process_list, in_process_list):
        in_process_list.append(current_vertex)
        for index in self._dictIn[current_vertex]:
            if index[0] in in_process_list:
                return False
            else:
                if index[0] not in fully_process_list:
                    ok = self.topo_sort_dfs(index[0],sorted_list,fully_process_list,in_process_list)
                    if not ok:
                        return False
        in_process_list.remove(current_vertex)
        sorted_list.append(current_vertex)
        fully_process_list.append(current_vertex)
        return True

    def tarjan_algorithm(self):
        sorted_list = []
        fully_process_list = []
        in_process_list = []
        for current_vertex in self._dictIn:
            if int(current_vertex) not in fully_process_list:
                ok = self.topo_sort_dfs(current_vertex,sorted_list,fully_process_list,in_process_list)
                if not ok:
                    sorted_list = []
                    return sorted_list
        return sorted_list

    def generate_random_graph(self, number_of_vertices, number_of_edges):
        del self._dictOut
        del self._dictIn
        self._dictIn = {}
        self._dictOut = {}
        self._number_edges = 0
        self._number_vertices = number_of_vertices
        if number_of_edges > self._number_vertices * self._number_vertices:
            number_of_edges = self._number_vertices * self._number_vertices
        for index in range(number_of_vertices):
            self._dictIn[index] = []
            self._dictOut[index] = []
        for index in range(number_of_edges):
            first_vertex = randrange(0, number_of_vertices)
            second_vertex = randrange(0, number_of_vertices)
            while self.is_Edge(first_vertex, second_vertex):
                first_vertex = randrange(0, number_of_vertices)
                second_vertex = randrange(0, number_of_vertices)
            self.add_Edge(first_vertex, second_vertex, randrange(0, 123789))

    def find_shortest_path(self, starting_vertex, ending_vertex):
        if starting_vertex not in self._dictOut:
            return 0, -1
        if ending_vertex not in self._dictOut:
            return 0, -1
        queue_list = []
        visited_list = []
        previous_dict = {starting_vertex: -1}
        queue_list.append(starting_vertex)
        while len(queue_list) > 0:
            current_vertex = queue_list[0]
            visited_list.append(current_vertex)
            del queue_list[0]
            for index in self._dictOut[current_vertex]:
                if index[0] not in visited_list:
                    queue_list.append(index[0])
                    previous_dict[index[0]] = current_vertex
                    visited_list.append(index[0])

        path_list = [ending_vertex]
        current_vertex = ending_vertex
        distance = 0
        if ending_vertex not in previous_dict:
            return 0, -1
        while previous_dict[current_vertex] != -1:
            distance += 1
            path_list.append(previous_dict[current_vertex])
            current_vertex = previous_dict[current_vertex]
        path_list.reverse()
        return path_list, distance

    def read_activities(self, filename):
        file = open(filename, 'r')
        text = file.read()
        lines = text.split('\n')
        line = lines[0].split(' ')
        n = int(line[0])
        self._number_vertices = n
        self._number_edges = 0
        self._required_times[-1] = 0
        self._required_times[-2] = 0
        count = 0
        self._dictIn[-1] = []
        self._dictIn[-2] = []
        self._dictOut[-1] = []
        self._dictOut[-2] = []
        for index in lines:
            line = index.split(' ')
            if count > 0 and len(line) > 1:
                self._required_times[int(line[0])]=int(line[1])
                for index2 in range(2,len(line)):
                    if int(line[0]) not in self._dictOut:
                        self._dictOut[int(line[0])] = []
                    if int(line[0]) not in self._dictIn:
                        self._dictIn[int(line[0])] = []
                    if int(line[index2]) not in self._dictOut:
                        self._dictOut[int(line[index2])] = []
                    if int(line[index2]) not in self._dictIn:
                        self._dictIn[int(line[index2])] = []
                    self.add_Edge(int(line[index2]), int(line[0]), 0)
            count=count+1
        for index in self._dictOut:
            if not self._dictOut[index] and index != -2:
                self.add_Edge(index, -2, 0)
        for index in self._dictIn:
            if not self._dictIn[index] and index != -1:
                self.add_Edge(-1, index, 0)

        file.close()

    def read_graph(self, filename):
        file = open(filename, 'r')
        text = file.read()
        lines = text.split('\n')
        line = lines[0].split(' ')
        n = int(line[0])
        self._number_vertices = n
        self._number_edges = 0
        # for index in range(n):
        #   self._dictIn[index]=[]
        #  self._dictOut[index]=[]
        for index in lines:
            line = index.split(' ')
            if len(line) == 3:
                if int(line[0]) not in self._dictOut:
                    self._dictOut[int(line[0])] = []
                if int(line[0]) not in self._dictIn:
                    self._dictIn[int(line[0])] = []
                if int(line[1]) not in self._dictOut:
                    self._dictOut[int(line[1])] = []
                if int(line[1]) not in self._dictIn:
                    self._dictIn[int(line[1])] = []
                self.add_Edge(int(line[0]), int(line[1]), int(line[2]))

        file.close()

    def write_graph(self, filename):
        file = open(filename, 'w')
        file.write(str(self._number_vertices) + " " + str(self._number_edges) + '\n')
        for index in self._dictOut:
            for index2 in range(len(self._dictOut[index])):
                file.write(str(index) + " " + str(self._dictOut[index][index2][0]) + " " + str(
                    self._dictOut[index][index2][1]) + '\n')

    def get_in_degree(self, x):

        return len(self._dictIn[x])

    def get_out_degree(self, x):
        return len(self._dictOut[x])

    def get_out_edges(self, x):
        list = []
        for index in range(len(self._dictOut[x])):
            list.append(index)
        return list

    def get_in_edges(self, x):
        list = []
        for index in range(len(self._dictIn[x])):
            list.append(index)
        return list

    def get_edge_value(self, x, y):
        if self.is_Edge(x, y):
            for index in self._dictOut[x]:
                if index[0] == y:
                    return index[1]

    def modify_edge_value(self, x, y, new_value):
        if self.is_Edge(x, y):
            for index in self._dictOut[x]:
                if index[0] == y:
                    index[1] = new_value
            for index in self._dictIn[y]:
                if index[0] == x:
                    index[1] = new_value

    def remove_edge(self, x, y):
        list = []
        for index in self._dictIn[y]:
            if not index[0] == x:
                list.append(index)
        self._dictIn[y] = list
        list = []
        for index in self._dictOut[x]:
            if not index[0] == y:
                list.append(index)
        self._dictOut[x] = list
        self._number_edges -= 1

    def add_vertex(self, x):
        ok = False
        for index in self._dictOut:
            if index == x:
                ok = True
        if not ok:
            self._dictOut[x] = [[-1, -1]]
            self._dictIn[x] = []
            self._number_vertices += 1

    def remove_vertex(self, x):
        for index in self._dictOut[x]:
            list = []
            for index2 in self._dictIn[index[0]]:
                if not index2[0] == x:
                    list.append(index2)
                else:
                    self._number_edges -= 1
            self._dictIn[index[0]] = list
        self._dictOut.pop(x)
        for index in self._dictIn[x]:
            list = []
            for index2 in self._dictOut[index[0]]:
                if not index2[0] == x:
                    list.append(index2)
            self._dictOut[index[0]] = list
        self._dictIn.pop(x)
        self._number_vertices -= 1

    def get_number_vertices(self):
        return self._number_vertices

    def parse_vertices(self):
        return self._dictOut.keys()

    def parse_Nout(self, x):
        return self._dictOut[x]

    def parse_Nin(self, x):
        return self._dictIn[x]

    def is_Edge(self, x, y):
        if x not in self._dictOut:
            return False
        for index in self._dictOut[x]:
            if index[0] == y:
                return True
        return False

    def add_Edge(self, x, y, value):
        if [-1, -1] in self._dictOut[x]:
            self._dictOut[x] = []
        if not self.is_Edge(x, y):
            list = [y, value]
            self._dictOut[x].append(list)
            list = [x, value]
            self._dictIn[y].append(list)
            if y != -1:
                self._number_edges += 1

    def build_lowestCostWalk_FloydWarshall(self, x, y):
        for index in range(self._number_vertices):
            self._distance[index] = {}
            for index2 in range(self._number_vertices):
                self._distance[index][index2] = 999999999

        for index in self._dictOut:
            self._distance[index][index] = 0

        for index in self._dictOut:
            for index2 in self._dictOut[index]:
                self._distance[index][index2[0]] = index2[1]

        for index in self._dictOut:
            self._path_dict[index] = {}
            for index2 in self._dictOut:
                self._path_dict[index][index2] = 0
                if self._distance != 999999999:
                    self._path_dict[index][index2] = index
                else:
                    self._path_dict[index][index2] = -1

        #file = open("new_graph_modified.txt", 'w')
        #file.write(str(self._number_vertices) + " " + str(self._number_edges) + '\n')
        #for index in self._dictOut:
        #    for index2 in range(len(self._dictOut[index])):
        #        file.write(str(index) + " " + str(self._dictOut[index][index2][0]) + " " + str(
       #             self._dictOut[index][index2][1]) + '\n')
       # file.write('\n'+"the intermediate matrices are :"+'\n')

        for index1 in range(self._number_vertices):
            for index2 in range(self._number_vertices):
                for index3 in range(self._number_vertices):
                    if self._distance[index2][index1] + self._distance[index1][index3] < self._distance[index2][index3]:
                        self._distance[index2][index3] = self._distance[index2][index1] + self._distance[index1][index3]
                        self._path_dict[index2][index3] = self._path_dict[index1][index3]
            #for i in self._distance:
            #    for j in range(len(self._distance[i])):
            #        if self._distance[i][j]==999999999:
            #            file.write("inf"+" ")
            #        else:
            #            file.write(str(self._distance[i][j]) + " ")
            #    file.write('\n')
            #file.write('\n')
            #for i in self._distance:
            #    for j in range(len(self._path_dict[i])):
            #        file.write(str(self._path_dict[i][j]) + " ")
            #    file.write('\n')
            #file.write('\n')
        #path_list = [y]
        #vertex1 = x
       # vertex2 = y
        #while self._path_dict[vertex1][vertex2] != vertex1:
        #    path_list.append(self._path_dict[vertex1][vertex2])
        #    vertex2 = self._path_dict[vertex1][vertex2]
        #path_list.append(x)
        #path_list.reverse()
        #file.write("path cost is "+str(self._distance[x][y])+'\n'+"path is: ")
        #for index in path_list:
        #    file.write(str(index)+" ")

        return self.find_lowestCostWalk_FloydWarshall(x, y)

    def find_lowestCostWalk_FloydWarshall(self, x, y):
        if self._distance[x][y] == 999999999:
            path_list = []
        else:
            path_list = [y]
            vertex1 = x
            vertex2 = y
            while self._path_dict[vertex1][vertex2] != vertex1:
                path_list.append(self._path_dict[vertex1][vertex2])
                vertex2 = self._path_dict[vertex1][vertex2]
            path_list.append(x)
            path_list.reverse()
        return self._distance[x][y], path_list
