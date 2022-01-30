#!/usr/bin/env python3

import datetime, json, os, sys

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_weekday():
    return datetime.date.today().strftime('%A')

def get_time():
    return int(datetime.datetime.now().strftime('%H%M'))

def select_class(jsonobj):
    weekday = get_weekday()
    time = int(get_time())
    if weekday in jsonobj:
        if time >= 1000 and time < 1020 :
           class_rn = jsonobj['form_class'][0]
        elif time >= 1020 and time < 1105 :
            class_rn = jsonobj[weekday][0]
        elif time >= 1105 and time < 1200 :
            class_rn = jsonobj[weekday][1]
        else:
            print('There is no class at this time.')
            input('Press enter to exit.')
            sys.exit()
    else:
        print('There is no class at this time.')
        input('Press enter to exit.')
        sys.exit()
    return class_rn

def parse_class(class_rn):
    class_period = class_rn['period']
    class_teacher = class_rn['teacher']
    class_link = class_rn['link']
    return class_period, class_teacher, class_link

def class_msg(class_period, class_teacher, class_link):
    if class_period == '':
        print('You are joining the form class.')
        print('Form teacher is: ' + class_teacher)
        print("The link we're going to use is: " + class_link)
        consent = input('Do you consent to join the class? (y/n) ')
        if consent == 'y' or consent == '':
            class_open(class_link)
        else:
            print('You have declined to join the class.')
            input('Press enter to exit.')
            quit()
    else:
        print('You are joining class no ' + class_period + '.')
        print('Teacher is: ' + class_teacher)
        print("The link we're going to use is: " + class_link)
        consent = input('Do you consent to join the class? (y/n) ')
        if consent == 'y' or consent == '':
            class_open(class_link)
        else:
            print('You have declined to join the class.')
            input('Press enter to exit.')
            quit()


def class_open(class_link):
    if sys.platform == 'win32':
        os.system('start ' + class_link)
    elif sys.platform == 'linux':
        os.system('xdg-open ' + class_link)
    elif sys.platform == 'darwin':
        os.system('open ' + class_link)

def main():
    jsonobj = load_json('class-routine.json')
    class_rn = select_class(jsonobj)
    class_period, class_teacher, class_link = parse_class(class_rn)
    class_msg(class_period, class_teacher, class_link)

if __name__ == '__main__':
    main()