# 9. Класс «Геокоордината» с полями «градусы», «минуты», «секунды», «доли секунд».
# Класс «Метеодатчик» с полями «долгота» и «широта» (геокоординаты), «ID»,
# «температура», «влажность». Декоратор превращает число-результат в строку,
# добавляя символ «°». Декорировать геттер температуры.

import WeatherSensor as ws

def validation(x, condition, message):
    print(message)
    while True:
        try:
            x = float(input(">>> "))
            if condition(x):
                return x
            else:
                print("Input error!")
        except ValueError:
            print("Input error!")

def main_menu():
    print(f'\n1. Enter new WeatherSeonsor data (console)\n'
          f'2. Enter new WeatherSeonsor data (file)\n'
          f'3. Print data (console)\n'
          f'4. Print data (file)\n'
          f'5. Exit')
    choice = 0
    choice = validation(choice, lambda x: (1 <= x <= 5) and (x % 1 == 0), '')
    return choice

def print_menu():
    print(f'1. Print all data\n'
          f'2. Print longitude\n'
          f'3. Print latitude\n'
          f'4. Print ID\n'
          f'5. Print temperature\n'
          f'6. Print wetness')
    choice = 0
    choice = validation(choice, lambda x: (1 <= x <= 6) and (x % 1 == 0), '')
    return choice

def input_coordinates():
    degrees = 0
    degrees = int(validation(degrees, lambda x: (0 <= x < 360) and (x % 1 == 0), 'Degrees'))

    minutes = 0
    minutes = int(validation(minutes, lambda x: (0 <= x < 60) and (x % 1 == 0), 'Minutes'))

    seconds = 0
    seconds = int(validation(seconds, lambda x: (0 <= x < 60) and (x % 1 == 0), 'Seconds'))
            
    mseconds = 0
    mseconds = int(validation(mseconds, lambda x: (0 <= x < 1000) and (x % 1 == 0), 'Milliseconds'))
    return degrees, minutes, seconds, mseconds

def input_weather_data():
    print('Enter longitude')
    lst = input_coordinates()
    longitude = ws.GeoCoordinate(lst[0], lst[1], lst[2], lst[3])

    print('Enter latitude')
    lst = input_coordinates()
    latitude = ws.GeoCoordinate(lst[0], lst[1], lst[2], lst[3])

    id = input('Enter ID\n>>> ')
            
    temperature = 0
    temperature = validation(temperature, lambda x: -100 < x < 100, 'Enter temperature')
    wetness = 0
    wetness = validation(wetness, lambda x: -100 < x < 100, 'Enter wetness, %')
    return ws.WeatherSensor(longitude, latitude, id, temperature, wetness)

def read_weather_data(ws_dict):
    lst = ws_dict['Longitude'].split('.')
    longitude = ws.GeoCoordinate(lst[0], lst[1], lst[2], lst[3])

    lst = ws_dict['Latitude'].split('.')
    latitude = ws.GeoCoordinate(lst[0], lst[1], lst[2], lst[3])

    id = ws_dict['ID']
    temperature = float(ws_dict['Temperature'].strip('°'))
    wetness = float(ws_dict['Wetness'].strip('%'))
    return ws.WeatherSensor(longitude, latitude, id, temperature, wetness)


exit_flag = False
weather_data = ws.WeatherSensor()
while (not exit_flag):
    choice = main_menu()
    match choice:
        case 1:
            weather_data = input_weather_data()
        case 2:
            weather_data_dict = {}
            with open('inp.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    key, value = line.split(':', 1)
                    weather_data_dict[key.strip()] = value.strip()
            weather_data = read_weather_data(weather_data_dict)
            print('Succsessfully read from "inp.txt"')
        case 3:
            if (not weather_data.is_empty()):
                choice_print = print_menu()
                match choice_print:
                    case 1:
                        print(weather_data)
                    case 2:
                        print(weather_data.longitude)
                    case 3:
                        print(weather_data.latitude)
                    case 4:
                        print(weather_data.id)
                    case 5:
                        print(weather_data.temperature)
                    case 6:
                        print(f'{weather_data.wetness} %')
            else: print('No data')
        case 4:
            if (not weather_data.is_empty()):
                with open('out.txt', 'w', encoding='utf-8') as out_file:
                    choice_print = print_menu()
                    match choice_print:
                        case 1:
                            print(weather_data, file=out_file)
                        case 2:
                            print(weather_data.longitude, file=out_file)
                        case 3:
                            print(weather_data.latitude, file=out_file)
                        case 4:
                            print(weather_data.id, file=out_file)
                        case 5:
                            print(weather_data.temperature, file=out_file)
                        case 6:
                            print(f'{weather_data.wetness} %', file=out_file)
                print('Successfully printed to file "out.txt"')
            else: print('No data')
        case 5:
            exit_flag = True
