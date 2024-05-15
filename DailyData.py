import time, datetime,string,textwrap

from datetime import date, timedelta
#from datetime import datetime
from numpy import little_endian
import os, random
try:
    file = open("My_Data.txt","r")
    my_data_lines = file.readlines()
    from numpy import right_shift
    today = date.today()
    split_line = str(today).split("-")
except FileNotFoundError:
    print("A list has not been found")
months = ["January","Feburary","March","April","May","June","July","August","September","October","November","December"]

def GetList(list_name):
    line = 0
    list_start_found = False
    while list_start_found == False:
        if my_data_lines[line].find(list_name) != -1:
            list_start_found = True
        else:
            line += 1
    list_start = line
    line = line + 1
    list_end_found = False
    while list_end_found == False:
        if my_data_lines[line] == "\n":
            list_end_found = True
        else:
            line += 1
    list_end = line
    found_list = []
    for i in range (list_start + 1,list_end):
        found_list.append(my_data_lines[i].rstrip("\n"))
    return found_list

def DisplayMenu():
    print("\n")
    print("MAIN MENU".rjust(24," "))
    time.sleep(0.01)
    print("\n")
    print("1"+("ADD A LINE").rjust(40,"-"))
    time.sleep(0.01)
    print("2"+("ADD A DREAM").rjust(40,"-"))
    time.sleep(0.01)
    print("3"+("ADD A LESSON").rjust(40,"-"))
    time.sleep(0.01)
    print("4"+("ADD PERSON MET").rjust(40,"-"))
    time.sleep(0.01)
    print("5"+("VIEW DATA").rjust(40,"-"))
    time.sleep(0.01)
    print("6"+("FILM LIST MANAGER").rjust(40,"-"))
    time.sleep(0.01)
    print("7"+("SAVE AND QUIT").rjust(40,"-"))
    print("\n")
    valid_input = False
    while valid_input == False:
        user_input = input()
        if user_input == "1":
            print("\n")
            valid_input = True
            AddLines()
            print("\n")
            DisplayMenu()

        elif user_input == "2":
            print("\n")
            valid_input = True
            AddDream()
            print("\n")
            DisplayMenu()

        elif user_input == "3":
            print("\n")
            valid_input = True
            AddLesson()
            print("\n")
            DisplayMenu()

        elif user_input == "4":
            print("\n")
            valid_input = True
            AddPerson()
            print("\n")
            DisplayMenu()

        elif user_input == "5":
            print("\n")
            valid_input = True
            print("VIEW DATA".rjust(25," "))
            time.sleep(0.01)
            print("\n")
            print("1"+("VIEW LINE A DAY").rjust(40,"-"))
            time.sleep(0.01)
            print("2"+("VIEW DREAMS").rjust(40,"-"))
            time.sleep(0.01)
            print("3"+("VIEW LESSONS").rjust(40,"-"))
            time.sleep(0.01)
            print("4"+("VIEW PEOPLE").rjust(40,"-"))
            time.sleep(0.01)
            print("5"+("VIEW INPUTS FROM A DAY").rjust(40,"-"))
            time.sleep(0.01)
            print("6"+("BACK TO MENU").rjust(40,"-"))
            print("\n")
            valid_input_b = False
            while valid_input_b == False:
                user_input_b = input()
                if user_input_b == "1":
                    print("\n")
                    valid_input_b = True
                    print("\n")
                    print("VIEW LINE A DAY:".rjust(25," "))
                    time.sleep(0.01)
                    print("\n")
                    print("1"+("AS A LIST").rjust(40,"-"))
                    time.sleep(0.01)
                    print("2"+("WITH A SEARCH WORD").rjust(40,"-"))
                    time.sleep(0.01)
                    print("3"+("BACK TO MENU").rjust(40,"-"))
                    print("\n")
                    valid_input_c = False
                    while valid_input_c == False:
                        user_input_c = input()
                        if user_input_c == "1":
                            valid_input_c = True
                            DisplayLongStringList(line_a_day,"LINE:")

                        elif user_input_c == "2":
                            valid_input_c = True
                            print("What word would you like to search by?")
                            user_input_word = input()
                            SearchByWord(user_input_word,line_a_day,"LINE:")

                        elif user_input_c == "3":
                            valid_input_c = True

                elif user_input_b == "2":
                    print("\n")
                    valid_input_b = True
                    print("\n")
                    print("VIEW DREAMS:".rjust(24," "))
                    time.sleep(0.01)
                    print("\n")
                    print("1"+("AS A LIST").rjust(40,"-"))
                    time.sleep(0.01)
                    print("2"+("WITH A SEARCH WORD").rjust(40,"-"))
                    time.sleep(0.01)
                    print("3"+("BACK TO MENU").rjust(40,"-"))
                    time.sleep(0.01)
                    print("\n")
                    valid_input_c = False
                    while valid_input_c == False:
                        user_input_c = input()
                        if user_input_c == "1":
                            valid_input_c = True
                            DisplayLongStringList(dreams,"DREAMS:")

                        elif user_input_c == "2":
                            valid_input_c = True
                            print("What word would you like to search by?")
                            user_input_word = input()
                            SearchByWord(user_input_word,dreams,"DREAMS:")

                        elif user_input_c == "3":
                            valid_input_c = True
                    

                elif user_input_b == "3":
                    print("\n")
                    valid_input_b = True
                    DisplayList(lessons,"LESSONS:")
                
                elif user_input_b == "4":
                    print("\n")
                    valid_input_b = True
                    DisplayLongStringList(people,"PEOPLE:")

                elif user_input_b == "5":
                    print("\n")
                    valid_input_b = True
                    DisplayInputsByDay()

                elif user_input_b == "6":
                    print("\n")
                    valid_input_b = True
            print("\n")
            print("\n")
            DisplayMenu()

        elif user_input == "6":
            print("\n")
            valid_input = True
            os.system("python FLM.py")
            DisplayMenu()
        

        elif user_input == "7":
            print("\n")
            valid_input = True
            WriteToFile()
            quit()
        
        


def AddLines():
    latest_entry = line_a_day[len(line_a_day)-2]
    x = latest_entry.split("/")
    latest_date = datetime.date(int(x[0]), int(x[1]), int(x[2]))
    out_of_date = latest_date < today
    if latest_date == today:
        print("UP TO DATE")
    elif out_of_date == True:
        loop = True
        extra_days = 1
        while loop == True:
            print("Enter your line for",(latest_date + timedelta(days=extra_days)))
            print("Type N to pass")
            user_input = input()
            if user_input == "n" or user_input == "N":
                
                correct_fomat_date = DateFormat(latest_date + timedelta(days=extra_days))
                line_a_day.append(correct_fomat_date)
                line_a_day.append(user_input)
                extra_days = extra_days + 1
                if (latest_date + timedelta(days=extra_days)) == (today + timedelta(days=1)):
                    print("here")
                    loop = False
                    counter = 0
                    lesson_strings = []
                    for lesson in lessons:
                        if counter == 0:
                            counter = 1
                        elif counter == 1:
                            lesson_strings.append(lesson)
                            counter = 0
                    if len(lesson_strings) > 15:
                        print("\n\nRemember: "+lesson_strings[random.randint(0,len(lesson_strings)-1)])
                        DisplayMenu()
                
            else:
                correct_fomat_date = DateFormat(latest_date + timedelta(days=extra_days))
                line_a_day.append(correct_fomat_date)
                line_a_day.append(user_input)
                extra_days = extra_days + 1
                if (latest_date + timedelta(days=extra_days)) == (today + timedelta(days=1)):
                    print("UP TO DATE")
                    counter = 0
                    lesson_strings = []
                    for lesson in lessons:
                        if counter == 0:
                            counter = 1
                        elif counter == 1:
                            lesson_strings.append(lesson)
                            counter = 0
                    if len(lesson_strings) > 15:
                        print("\n\nRemember: "+lesson_strings[random.randint(0,len(lesson_strings)-1)])
                    loop = False
                    DisplayMenu()

def DisplayInputsByDay():
    print("Which day?   (YYYY/MM/DD)")
    valid_input = False
    while valid_input == False:
        user_input = input()
        if user_input == "n" or user_input == "N":
            valid_input = True
        elif len(user_input) == 10:
            print("\n")
            valid_input = True
            yesterday = datetime.date(int(user_input[:4]),int(user_input[5:7]),int(user_input[8:]))
            yesterday = DateFormat(yesterday - timedelta(days=1))
            
            SearchByDate(line_a_day,user_input,"LINE A DAY:")
            SearchByDate(line_a_day,yesterday,"PREVIOUS DAY:")
            SearchByDate(people,user_input,"YOU MET:")
            SearchByDate(wake_up_times,user_input,"YOU WOKE UP AT:")
            SearchByDate(dreams,user_input,"YOU DREAMED:")
            SearchByDate(lessons,user_input,"YOU LEARNED:")
            

def SearchByDate(the_list,date,list_name):
    counter = 0
    returns = []
    for i in range (0,int(int(len(the_list))/2)):
        if date in the_list[counter]:
            returns.append(the_list[counter+1])
        counter += 2
    String = ("%-18s %-64s")
    if len(returns) != 0:
        for thing in returns:
            wrapped_lines = textwrap.wrap(thing,110)
            print(String %(list_name,wrapped_lines[0]))
            for i in range (1,len(wrapped_lines)):
                print(String %(" ",wrapped_lines[i]))

def DisplayList(the_list, list_type):
    print("\n")
    String = ("%-13s %-64s")
    print(String %("DATE:",list_type))
    flipper = 0
    for thing in the_list:
        if flipper == 0:
            date = thing
            if (date.endswith('\n')) == True:
                date = date.strip('\n')
            flipper = 1
        elif flipper == 1:
            message = thing
            print(String %(date,message))
            flipper = 0

def DisplayLongStringList(the_list, list_type):
    print("\n")
    String = ("%-13s %-64s")
    print(String %("DATE:",list_type))
    flipper = 0
    for thing in the_list:
        if flipper == 0:
            date = thing
            if (date.endswith('\n')) == True:
                date = date.strip('\n')
            flipper = 1
        elif flipper == 1:
            wrapped_lines = textwrap.wrap(thing,126)
            print(String %(date,wrapped_lines[0]))
            for i in range(1,len(wrapped_lines)):
                print(String %("",wrapped_lines[i]))
            
            flipper = 0
            if list_type != "LINE:":
                print("\n")

def SearchByWord(word,the_list,type):
    word_combinations = [word,word+"s",word+"'s",word+"'",]
    for i in range (0,3):
        separation = list(word_combinations[i])
        separation[0] = separation[0].swapcase()
        word_combinations.append("".join(separation))
    word_combinations.append(word.upper())
    counter = 0
    list_temp = []
    for i in range(0,int(len(the_list)/2)):
        for accepted_word in word_combinations:
            if the_list[counter] not in list_temp:
                if accepted_word in the_list[counter + 1]:
                    list_temp.append(the_list[counter])
                    list_temp.append(the_list[counter+1])
        counter += 2
    if len(list_temp) == 0:
        print("\n")
        print("None found with that word")
    elif type == "DREAMS:":
        DisplayLongStringList(list_temp,type)
    else:
        DisplayList(list_temp, type)




def DateFormat(format_date):
    if int(format_date.month) < 10:
        if int(format_date.day) < 10:
            return (str(format_date.year)+"/0"+str(format_date.month)+"/0"+str(format_date.day))
        else:
            return (str(format_date.year)+"/0"+str(format_date.month)+"/"+str(format_date.day))
    else:
        if int(format_date.day) < 10:
            return (str(format_date.year)+"/"+str(format_date.month)+"/0"+str(format_date.day))
        else:
            return (str(format_date.year)+"/"+str(format_date.month)+"/"+str(format_date.day))

def AddDream():
    print("What was your dream?")
    dream = input()
    if dream != "N" and dream != "n":
        todays_date = DateFormat(today)
        dreams.append(todays_date)
        dreams.append(dream)
    DisplayMenu()

def AddPerson():
    print("Who did you meet?")
    person = input()
    if person != "N" and person != "n":
        todays_date = DateFormat(today)
        people.append(todays_date)
        people.append(person)
    DisplayMenu()

def AddLesson():
    print("What is the lesson?")
    lesson = input()
    if lesson != "N" and lesson != "n":
        todays_date = DateFormat(today)
        lessons.append(todays_date)
        lessons.append(lesson)
    DisplayMenu()

def DisplayData():
    print(wake_up_times)
    print(dreams)
    print(line_a_day)

def WriteToFile():
    my_data_lines = []
    my_data_lines.append("    LINE A DAY:")
    for i in range (0,len(line_a_day)):
        my_data_lines.append(line_a_day[i])
    for i in range (0,2):
        my_data_lines.append("\n")
    my_data_lines.append("    DREAMS:")
    for i in range (0,len(dreams)):
        my_data_lines.append(dreams[i])
    for i in range (0,2):
        my_data_lines.append("\n")    
    my_data_lines.append("    LESSONS:")
    for i in range (0,len(lessons)):
        my_data_lines.append(lessons[i])
    for i in range (0,2):
        my_data_lines.append("\n")
    my_data_lines.append("    PEOPLE:")
    for i in range (0,len(people)):
        my_data_lines.append(people[i])
    for i in range (0,2):
        my_data_lines.append("\n")
    file = open("My_Data.txt","w")
    for line in my_data_lines:
        file.write(str(line))
        file.write("\n")
    file.close()


def graph():
    import matplotlib.pyplot
    from matplotlib.dates import DateFormatter
    
    flipper = 0
    dates_to_numbers = []
    times = []
    for item in temp_list:
        if flipper == 0:
            date = datetime.date(int(item[:4]),int(item[5:7]),int(item[8:]))
            dates_to_numbers.append(matplotlib.dates.date2num(date))
            flipper = 1
        else:
            time = int(item[:2]) + (int(item[3:])/60)
            times.append(time)
            flipper = 0
    matplotlib.pyplot.figure(figsize=(14, 7))
    matplotlib.pyplot.plot_date(dates_to_numbers, times, marker=',', linestyle=':', color='r', markersize=2)
    matplotlib.pyplot.xlabel("DATE")
    matplotlib.pyplot.ylabel("TIME")
    matplotlib.pyplot.legend()
    myFmt = DateFormatter("%b-%y")
    matplotlib.pyplot.gca().xaxis.set_major_formatter(myFmt)
    matplotlib.pyplot.show()


dreams = GetList("DREAMS:")
line_a_day = GetList("LINE A DAY:")
lessons = GetList("LESSONS:")
people = GetList("PEOPLE:")
DisplayMenu()

