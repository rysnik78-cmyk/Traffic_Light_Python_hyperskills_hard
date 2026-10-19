import os
import sys
import time
from threading import Thread, Lock
import subprocess
from collections import deque


l = Lock()

class TrafficManSys():


    def __init__(self):

        self.welcome()
        self.state = 'Not Started'
        self.number_of_roads = self.input_positive("Input the number of roads: ")
        self.roads_queue = RoadsQueue(self.number_of_roads)
        self.interval = self.input_positive("Input the interval: ")
        self.threads = Thread(target=self.stop_watch, name='QueueThread')
        self.threads.start()
        self.state = 'Menu'

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
                    self.state = 'Bye'
                    break
                case "1":
                    road_name = input("Input road name: ")
                    print(self.roads_queue.add_road(road_name))
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case "2":
                    print(self.roads_queue.delete_road())
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case "3":
                    self.state = 'System'
                    input()
                    self.state = 'Menu'
                    continue
                case _:
                    print('Incorrect option')
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

    def stop_watch(self ):
        start_time = time.time()
        while True:
            if self.state=='System':
                subprocess.run("cls", shell=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                passed = time.time() - start_time
                print(f'! {round(passed)}s. have passed since system startup !')
                print(f'! Number of roads: {self.number_of_roads} !')
                print(f'! Interval: {self.interval} !\n')
                print(self.roads_queue.list_of_roads())
                print('! Press "Enter" to open menu !')
                # print(self.state)
                time.sleep(1)
            if self.state == 'Bye':
                break

class RoadsQueue:
    def __init__(self, number_of_roads):
        self.queue_size = number_of_roads
        self.traffic_deque = deque(maxlen=self.queue_size)
        self.queue_elements_count = 0
        # self.road_name_list = []

    def add_road(self, road):
        if self.queue_elements_count == self.queue_size:
            return 'Queue is full'
        else:
            self.traffic_deque.append(road)
            self.queue_elements_count += 1
        return f'{road} added'


    def delete_road(self):
        if self.queue_elements_count > 0:
            self.queue_elements_count -= 1
            return f'{self.traffic_deque.popleft()} deleted!'
        else:
            return 'queue is empty'

    def list_of_roads(self):
        if self.queue_elements_count == 0:
            return ''
        else:
            list_of_roads = ''
            for i in range(self.queue_elements_count):
                road = self.traffic_deque.popleft()
                list_of_roads += f'{road}\n'
                self.traffic_deque.append(road)
            return list_of_roads




if __name__ == "__main__":

    tms_session = TrafficManSys()


