
class TrafficManSys():
    def __init__(self):
        self.welcome()
        self.number_of_roads = int(input("Input the number of roads: "))
        self.interval = int(input("Input the interval: "))
        self.main_menu()

    def welcome(self):
        print('Welcome to the traffic management system!')

    def show_menu(self):
        print('Menu:')
        menu_list = ['Quit', 'Add road', 'Delete road', 'Open system']
        for i in range(len(menu_list)):
            index = i + 1
            print(f'{index % 4}. {menu_list[index % 4]}')

    def main_menu(self) -> None:
        while True:
            self.show_menu()
            command = input().strip()
            match command:
                case "0":
                    print("Bye!")
                    break
                case "1":
                    print("Road added")
                    continue
                case "2":
                    print("Road deleted")
                    continue
                case "3":
                    print("System opened")
                    continue
                case _:
                    print('Bad command!\n')
                    continue

if __name__ == "__main__":

    tms_session = TrafficManSys()


