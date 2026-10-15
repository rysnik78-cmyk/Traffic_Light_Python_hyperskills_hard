import os


class TrafficManSys():
    def __init__(self):
        self.welcome()
        self.number_of_roads = self.input_positive("Input the number of roads: ")
        self.interval = self.input_positive("Input the interval: ")
        self.main_menu()


    def input_positive(self, communication = ''):
        print(communication, end='')
        error_string = 'Error! Incorrect input. Try againg: '
        while True:
            try:
                number = int(input())
            except ValueError:
                print(error_string, end='')
                continue
            if number <= 0:
                print(error_string, end='')
                continue
            return number

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
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case "2":
                    print("Road deleted")
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case "3":
                    print("System opened")
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case _:
                    print('Incorrect option')
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue


if __name__ == "__main__":

    tms_session = TrafficManSys()


