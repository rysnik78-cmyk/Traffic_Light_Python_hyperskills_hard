import math
import os
import time
from threading import Thread
import subprocess
from collections import deque

class TrafficManSys():

    def __init__(self):
        self.threads = None
        self.start_time = None
        self.welcome()
        self.state = 'Not Started'
        number_of_roads = self.input_positive("Input the number of roads: ")
        interval = self.input_positive("Input the interval: ")
        self.threads = Thread(target=self.stop_watch, name='QueueThread')
        self.threads.start()
        self.roads_queue = RoadsQueue(number_of_roads, interval)
        self.main_menu()

    def input_positive(self, communication = ''):
        print(communication, end='')
        error_string = 'Error! Incorrect input. Try again: '
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
                    print(self.roads_queue.delete_road(not self.state=='Not Started'))
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case "3":
                    if self.state == 'Not Started':
                        self.start_time = time.perf_counter()
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
        while True:
            if self.state=='System':
                subprocess.run("cls", shell=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                passed = time.perf_counter() - self.start_time
                print(f'! {int(passed)}s. have passed since system startup !')
                print(f'! Number of roads: {self.roads_queue.max_queue_size} !')
                print(f'! Interval: {self.roads_queue.interval} !')
                print(self.roads_queue.list_of_roads(passed))
                print('! Press "Enter" to open menu !')
                # print(self.state)
                time.sleep(1)
            if self.state == 'Bye':
                break

class RoadsQueue:
    def __init__(self, number_of_roads, interval):
        self.max_queue_size = number_of_roads
        self.traffic_deque = deque(maxlen=self.max_queue_size)
        self.queue_elements_count = 0
        self.interval = interval
        self.cycle_beginning_time = 0
        self.total_cycle_time = 0
        # self.road_name_list = []

    def road_status(self, street_number, current_time_from_cycle_beginning):

        if (street_number * self.interval) > current_time_from_cycle_beginning >= (street_number - 1) * self.interval:
            opened = 'open'
            seconds_to = math.ceil((street_number * self.interval) - current_time_from_cycle_beginning)
        else:
            opened = 'closed'
            delta = ((street_number - 1) * self.interval) - current_time_from_cycle_beginning
            if delta > 0:
                seconds_to = math.ceil(delta)
            else:
                seconds_to = math.ceil(self.total_cycle_time - current_time_from_cycle_beginning + (street_number - 1) * self.interval)

        return f'{opened} for {seconds_to}s.'

    def add_road(self, road):
        if self.queue_elements_count == self.max_queue_size:
            return 'Queue is full'
        else:
            self.traffic_deque.append(road)
            self.queue_elements_count += 1
            self.total_cycle_time = self.interval * self.queue_elements_count
            return f'{road} added'

    def delete_road(self, system_started):
        if self.queue_elements_count > 0:
            self.queue_elements_count -= 1
            self.total_cycle_time = self.interval * self.queue_elements_count
            if system_started:
                self.cycle_beginning_time += self.interval
            return f'{self.traffic_deque.popleft()} deleted!'
        else:
            return 'queue is empty'

    def list_of_roads(self, overall_current_time):
        if self.queue_elements_count == 0:
            return ''
        else:
            list_of_roads = ''
            if overall_current_time - self.cycle_beginning_time >= self.total_cycle_time:
                self.cycle_beginning_time += self.total_cycle_time
            current_time_of_cycle = overall_current_time - self.cycle_beginning_time
            for i in range(1, self.queue_elements_count + 1):
                road = self.traffic_deque.popleft()
                list_of_roads += f'Road "{road}" will be {self.road_status(i, current_time_of_cycle)}'
                if i < self.queue_elements_count:
                    list_of_roads += '\n'
                self.traffic_deque.append(road)
            return list_of_roads

if __name__ == "__main__":
    tms_session = TrafficManSys()