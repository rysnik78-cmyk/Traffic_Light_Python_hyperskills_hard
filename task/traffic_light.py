
class TrafficManSys():
    def __init__(self):
        self.welcome()
        self.main_menu()

    def welcome(self):
        print('Welcome to the traffic management system!')

    def show_menu(self):
        print('Menu:')
        menu_list = ['Quit', 'Add', 'Delete', 'System']
        for i in range(len(menu_list)):
            index = i + 1
            print(f'{index % 4}. {menu_list[index % 4]}')

    def main_menu(self) -> None:
        while True:
            self.show_menu()
            break
            """
            command = input("Choose option: ").strip()

            match command:
                case "0":
                    print("Exit!")
                    break
                case "1":
                    continue

                case "2":
                    continue

                case "3":
                    continue
                case _:
                        print('Bad command!\n')
            """

if __name__ == "__main__":

    tms_session = TrafficManSys()


