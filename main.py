from repo import *
from ui import *
from controller import *


def main():
    repo=Graph()
    controller=Controller(repo)
    menu=Menu(controller)
    menu.run_menu()


main()