

class Menu():
    def __init__(self , controller):
        self._controller = controller

    def run_menu(self):
        while True:
            print("Choose option: ")
            print("0.read/write from/to file")
            print("1.get the number of vertices;")
            print("2.check edge between two vertices")
            print("3.get in degree of a vertex")
            print("4.get out degree of a vertex")
            print("5.retrieve the information of an edge")
            print("6.modify the information of an edge")
            print("7.add edge")
            print("8.remove edge")
            print("9.add vertex")
            print("10.remove vertex")
            print("11.exit")
            print("12.generate random graph")
            print("13.find shortest path between two vertices")
            print("14.find lowest cost walk between two vertices (using Floyd-Warshall) ")
            print("15.read activities from file")
            print("16.sort the graph topologically ")
            print("17.calculate times")

            option = input()
            ok = True

            while ok:
                try:
                    option = int(option)
                    ok = False
                except:
                    print('invalid input!')
                    option=input()

            if option == 0:
                print("introduce filename")
                filename = str(input())
                print("1.read from file")
                print("2.write to file")
                option = int(input())
                if option == 1:
                    self._controller.read_graph(filename)
                else:
                    self._controller.write_graph(filename)
            elif option == 1:
                number_of_vertices = self._controller.get_number_vertices()
                print("the number of vertices is: "+str(number_of_vertices))
            elif option == 2:
                print("enter the vertices")
                print("vertex 1: ")
                first_vertex = int(input())
                print("vertex 2: ")
                second_vertex = int(input())
                is_edge = self._controller.is_edge(first_vertex,second_vertex)
                if is_edge:
                    print("yes")
                else:
                    print("no")
            elif option == 3:
                print("input vertex: ")
                vertex = int(input())
                in_degree = self._controller.get_in_degree(vertex)
                print(in_degree)
                print(self._controller.parse_nIn(vertex))
            elif option == 4:
                print("input vertex: ")
                vertex = int(input())
                out_degree = self._controller.get_out_degree(vertex)
                print(out_degree)
                print(self._controller.parse_nOut(vertex))
            elif option == 5:
                print("input vertex 1: ")
                first_vertex = int(input())
                print("input vertex 2: ")
                second_vertex = int(input())
                information = self._controller.get_edge_value(first_vertex,second_vertex)
                print(information)
            elif option == 6:
                print("input vertex 1: ")
                first_vertex = int(input())
                print("input vertex 2: ")
                second_vertex = int(input())
                print("input new value: ")
                new_value = int(input())
                self._controller.modify_edge_value(first_vertex,second_vertex,new_value)
            elif option == 7:
                print("input vertex 1: ")
                first_vertex = int(input())
                print("input vertex 2: ")
                second_vertex = int(input())
                print("input value: ")
                value = int(input())
                self._controller.add_edge(first_vertex,second_vertex,value)
            elif option == 8:
                print("input vertex 1: ")
                first_vertex = int(input())
                print("input vertex 2: ")
                second_vertex = int(input())
                self._controller.remove_edge(first_vertex,second_vertex)
            elif option == 9:
                print("input vertex: ")
                vertex = int(input())
                self._controller.add_vertex(vertex)
            elif option == 10:
                print("input vertex: ")
                vertex = int(input())
                self._controller.remove_vertex(vertex)
            elif option == 11:
                break
            elif option == 12:
                print("input number of vertices: ")
                number_of_vertices=int(input())
                print("input number of edges: ")
                number_of_edges = int(input())
                self._controller.generate_random_graph(number_of_vertices,number_of_edges)
            elif option == 13:
                print("input starting vertex:")
                starting_vertex = int(input())
                print("input ending vertex:")
                ending_vertex = int(input())
                path_list, distance = self._controller.find_shortest_path(starting_vertex, ending_vertex)
                if distance == -1:
                    print("there is no such path!")
                else:
                    for index in path_list:
                        print(index)
                    print(distance)
            elif option == 14:
                print("input starting vertex:")
                starting_vertex = int(input())
                print("input ending vertex:")
                ending_vertex = int(input())
                path_list = []
                value, path_list = self._controller.find_lowestCostWalk_FloydWarshall(starting_vertex,ending_vertex)
                if value == 999999999:
                    print("there is no walk between the two vertices!")
                else:
                    print("the closest walk value is ", value, " and the path is:")
                    for index in path_list:
                        print(index)
            elif option == 16:
                sorted_list=self._controller.topo_sort()
                if sorted_list == []:
                    print("invalid input!")
                else:
                    sorted_list.remove(-1)
                    sorted_list.remove(-2)
                    for index in sorted_list:
                        print(index)
            elif option == 15:
                print("introduce filename")
                filename = str(input())
                self._controller.read_activities(filename)
            elif option == 17:
                sorted_list = self._controller.topo_sort()
                self._controller.calculate(sorted_list)
                sorted_list.remove(-1)
                sorted_list.remove(-2)
                start_times=self._controller.get_start_times()
                end_times=self._controller.get_end_times()
                for index in sorted_list:
                    print(index," earliest start time: ",start_times[index][0]," latest start time: ", end_times[index][0],end=" ")
                    print(index," earliest end time: ",start_times[index][1]," latest end time: ", end_times[index][1],end="")
                    if start_times[index][0] == end_times[index][0]:
                        print(" critical activity!",end="")
                    print(" ")
                print("Total project time is: ",start_times[-2][0])

            else:
                print("invalid option!")