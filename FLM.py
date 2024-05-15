import os, sys
import time, datetime,string,textwrap

from datetime import date, timedelta
try:
   
    file = open("2020 Vision.txt","r")
    lines = file.readlines()
    import time
    
    from imdb import Cinemagoer
    from itertools import islice
    from datetime import date
    from datetime import datetime
    from numpy import right_shift
except (FileNotFoundError,ModuleNotFoundError):
    print("A list has not been found")
    print("Would you like to one? (Y/N)")
    INPUT = input()
    if INPUT == "Y" or "y":
        os.system('pip install imdbpy')
        os.system('pip install numpy')
        os.system('pip install itertools')
        os.system('pip install matplotlib')
        file = open("2020 Vision.txt","w+")
        print("A list has not been found so one has been created")
        print("A textfile has been created in the same folder as this program")
        print("Please do not delete or edit the textfile")
        print(" ")
        time.sleep(0.5)
        lines = []
        lines.append("    FILMS SEEN")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    RANKED LIST OF FILMS SEEN")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    TO WATCH")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    DATES")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    RUN TIMES")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    IDS")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    FILM CAST")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    GENRES")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    RATINGS")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    COMPOSERS")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    YEAR")
        for i in range (0,2):
            lines.append("\n")
        lines.append("    VIEW COUNT")
        for i in range (0,2):
            lines.append("\n")
        lines.append("0")
        for i in range (0,5):
            lines.append("\n")
        for line in lines:
            file.write(line)
            file.write("\n")
        file.close()
        file = open("2020 Vision.txt","r")
        lines = file.readlines()
    else:
        sys.exit()

    

def MakeBackup():
    if len(OutPutLines) > 10:
        BackupFile = open("2020 Vision Backup.txt","w+")
        for line in OutPutLines:
            BackupFile.write(str(line))
            BackupFile.write("\n")
        BackupFile.close()



def CountList():
    global EndOfList
    Checked = 0
    n = 0
    while Checked == 0:
        if lines[n] == "\n":
            Checked = 1
        else:
            n += 1
    EndOfList = n



def SortList():
    AlreadyCompared = []
    Sorted = False
    while Sorted == False:
        SortCount = 0
        for i in range (0,len(ListOfFilms)-2):
            Pass = 0
            for b in range (0,len(AlreadyCompared)):
                if (AlreadyCompared[b].find(ListOfFilms[i]) != -1) and (AlreadyCompared[b].find(ListOfFilms[i+1]) != -1):
                    print("pass",ListOfFilms[i],ListOfFilms[i+1])
                    SortCount = SortCount + 1
                    Pass = 1
            if Pass == 0:
                print("What is better? \n1        ",ListOfFilms[i],"\n2        ",ListOfFilms[i+1])
                ValidInput = False
                while ValidInput == False:
                    Choice = input()
                    if Choice == "2" or Choice == "1":
                        ValidInput = True
                    else:
                        print("What is better? \n1        ",ListOfFilms[i],"\n2        ",ListOfFilms[i+1])
                if Choice == "2":
                    ComparedString = (ListOfFilms[i+1] + " and " + ListOfFilms[i])
                    AlreadyCompared.append(ComparedString)
                    Buffer = ListOfFilms[i+1]
                    ListOfFilms[i+1] = ListOfFilms[i]
                    ListOfFilms[i] = Buffer
                elif Choice == "1":
                    ComparedString = (ListOfFilms[i] + " and " + ListOfFilms[i+1])
                    AlreadyCompared.append(ComparedString)
        if SortCount > len(ListOfFilms)-4:
            Sorted = True



def CreateLines():
    lines = []
    lines.append("    FILMS SEEN")
    for i in range (0,len(ChronilogicalOrder)):
        lines.append(ChronilogicalOrder[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("    RANKED LIST OF FILMS SEEN")
    for i in range (0,len(ListOfFilms)):
        lines.append(ListOfFilms[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("  DATES")
    for i in range (0,len(DateList)):
        lines.append(DateList[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("  RUN TIMES")
    for i in range (0,len(RunTimes)):
        lines.append(RunTimes[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("  IDS")
    for i in range (0,len(IDList)):
        lines.append(IDList[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("  FILM CAST")
    for i in range (0,len(FilmCast)):
        string = (IDList[i])
        line = ""
        try:
            for b in range(0,len(FilmCast[string])):
                line = line + FilmCast[string][b] + ","
            lines.append(line)
        except KeyError:
            print("")
    for i in range (0,2):
        lines.append("\n")
    lines.append("  GENRES")
    for i in range (0,len(Genres)):
        string = (IDList[i])
        line = ""
        try:
            for b in range(0,len(Genres[string])):
                line = line + Genres[string][b] + ","
            lines.append(line)
        except KeyError:
            print("")
    for i in range (0,2):
        lines.append("\n")
    lines.append("  RATINGS")
    for i in range (0,len(Ratings)):
        lines.append(Ratings[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("  COMPOSERS")
    for i in range (0,len(Composers)):
        lines.append(Composers[i])
    for i in range (0,2):
         lines.append("\n")
    lines.append("  YEAR")
    for i in range (0,len(releaseYear)):
        lines.append(releaseYear[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("  VIEW COUNT")
    for i in range (0,len(ViewCount)):
        lines.append(ViewCount[i])
    for i in range (0,2):
        lines.append("\n")
    lines.append("\n")
    return lines



class Film:
    def __init__(self,title,cast,runtime,dateWatched,ID):
        self.title = title
        self.cast = []
        self.runtime = runtime
        self.dateWatched = dateWatched
        self.ID = ID



def CreateFilmObjects():
    FilmObjects = []
    for i in range (0,len(ChronilogicalOrder)):
        FilmObjects.append(Film(ChronilogicalOrder[i],FilmCast[IDList[i]],RunTimes[i],DateList[i],IDList[i]))
    return FilmObjects



def GetRunTime():
    n= 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("RUNTIME") != -1:
            Checked = 1
        else:
            n += 1
    RunTime = lines[n+1].rstrip("\n")
    if Checked == 0:
        RunTime = 0
    #print("RUNTIME IS ",RunTime)
    return RunTime



def GetDates():
    global DateList
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("DATES") != -1:
            Checked = 1
        else:
            n += 1
    DATES = n
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            x = x+1
    ENDOFDATES = x
    DateList = []
    for i in range (DATES + 1,ENDOFDATES):
        DateList.append(lines[i].rstrip("\n"))
    return DateList


def GetRuntimes():
    global RunTimes
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("RUN TIMES") != -1:
            Checked = 1
        else:
            n += 1
    RUNTIMES = n
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            x = x+1
    ENDOFRUNTIMES = x
    RunTimes = []
    for i in range (RUNTIMES + 1,ENDOFRUNTIMES):
        RunTimes.append(lines[i].rstrip("\n"))
    return RunTimes



def GetIDs():
    global IDList
    IDList = []
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("IDS") != -1:
            Checked = 1
        else:
            n += 1
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            IDList.append(lines[x].rstrip("\n"))
            x = x+1
    return IDList

def GetRatings():
    global Ratings
    Ratings = []
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("RATINGS") != -1:
            Checked = 1
        else:
            n += 1
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            Ratings.append(lines[x].rstrip("\n"))
            x = x+1
    return Ratings


def GetViewCount():
    global ViewCount
    ViewCount = []
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("VIEW COUNT") != -1:
            Checked = 1
        else:
            n += 1
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            ViewCount.append(lines[x].rstrip("\n"))
            x = x+1
    return ViewCount


def GetComposers():
    global Composers
    Composers = []
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("COMPOSERS") != -1:
            Checked = 1
        else:
            n += 1
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            Composers.append(lines[x].rstrip("\n"))
            x = x+1
    return Composers

def GetReleaseYears():
    global releaseYear
    releaseYear = []
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("YEAR") != -1:
            Checked = 1
        else:
            n += 1
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            releaseYear.append(lines[x].rstrip("\n"))
            x = x+1
    return releaseYear


def GetWatchList():
    ChronilogicalOrder = []
    if len(ListOfFilms) > 1:
        for i in range(1,len(ListOfFilms)+1):
            ChronilogicalOrder.append(lines[i].rstrip("\n"))
    elif len(ListOfFilms) == 1:
        ChronilogicalOrder.append(ListOfFilms[0])
    if len(ChronilogicalOrder) > 0:
        if ChronilogicalOrder[len(ChronilogicalOrder)-1] == "":
            ChronilogicalOrder.remove("")
    return ChronilogicalOrder



def GetRankedList():
    ListOfFilms = []
    n= 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("RANKED LIST OF FILMS SEEN") != -1:
            Checked = 1
        else:
            n += 1
    RANKED = n
    x = n + 1
    Checked = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked = 1
        else:
            x = x + 1        
    ENDOFRANKED = x
    for i in range (RANKED + 1,ENDOFRANKED):
        ListOfFilms.append(lines[i].rstrip("\n"))
    return ListOfFilms



def EditTextFile():
    FileWrite = open("2020 Vision.txt","w")
    for line in OutPutLines:
        FileWrite.write(str(line))
        FileWrite.write("\n")
    FileWrite.close()



def DisplayMenu():
    global RunTime
    time.sleep(0.01)
    print("MENU".rjust(22," "))
    time.sleep(0.01)
    print("\n")
    print("1"+("ADD A WATCHED FILM").rjust(40,"-"))
    time.sleep(0.01)
    print("2"+("VIEW YOUR LISTS").rjust(40,"-"))
    time.sleep(0.01)
    print("3"+("""SAVE AND QUIT""").rjust(40,"-"))
    time.sleep(0.01)
    print("4"+("""TOP 30 ACTORS AND DIRECTORS""").rjust(40,"-"))
    time.sleep(0.01)
    print("5"+("""GRAPH""").rjust(40,"-"))
    time.sleep(0.01)
    print("6"+("""FIND FILMS WITH X IN""").rjust(40,"-"))
    time.sleep(0.01)
    print("7"+("""MOST WATCHED FILMS""").rjust(40,"-"))
    time.sleep(0.01)
    print("8"+("""MORE DATA""").rjust(40,"-"))
    time.sleep(0.01)
    print("9"+("""EXPERIMENTAL ALGORITHM""").rjust(40,"-"))
    time.sleep(0.01)
    print("\n")
    print("\n")
    ValidInput = False
    while ValidInput == False:
        Choice = input()
        if Choice == "1":
            print("\n")
            ValidInput = True
            NewFilm = input("What Film?")
            if ValidInput == False:
                print("You have already seen this film")
            else:
                print("Searching Database...")

                NewFilmIMDB, id, MovieRunTime, Rating, Year, Composer= GetMovieInfo(NewFilm)
                skip = 0
                if NewFilmIMDB == "N/A":
                    print("\n")
                    print("Film couldn't be found in the database \nTry using capitals for the start of each word \nTry putting the year of release at the end: Film Name (2018)")
                    time.sleep(1.6)
                    print("\n")
                    skip = 1
                else:        
                    NewFilm = NewFilmIMDB
            
                if skip == 0:
                    SeenIt = 0
                    IDmethod = 0
                    if id in IDList:
                        SeenIt = 1
                        IDmethod = 1
                    if str(NewFilm) in ChronilogicalOrder and str(Year) == str(releaseYear[ChronilogicalOrder.index(str(NewFilm))]):
                        SeenIt = 1
                    if SeenIt == 0:
                        if NewFilm in ChronilogicalOrder:
                            if str(Year) != str(releaseYear[ChronilogicalOrder.index(str(NewFilm))]):
                                NewFilm = NewFilm + " (" + str(Year) + ")"
                        IDList.append(id) 
                        RunTimes.append(MovieRunTime)
                        ChronilogicalOrder.append(NewFilm)
                        releaseYear.append(Year)
                        Ratings.append(Rating)
                        Composers.append(Composer)
                        ViewCount.append(1)
                        today = date.today()
                        Date = today.strftime("%d/%m/%Y")
                        DateList.append(Date)
                        print("\n")
                        if len(ChronilogicalOrder) == 1:
                            ListOfFilms.append(NewFilm)
                        else:
                            FilmRankedInsertion(NewFilm,ListOfFilms)
                    else:
                        if len(FilmCast) > len(ChronilogicalOrder):
                            FilmCast.popitem()
                            Genres.popitem()
                        print("\nyou have already seen this film, view count inremented by 1. \n")
                        
                        if IDmethod == 1:
                            position = IDList.index(id)
                            ViewCount[position] = int(ViewCount[position]) + 1
                        else:
                            position = ChronilogicalOrder.index(NewFilm)
                            ViewCount[position] = int(ViewCount[position]) + 1
                    
                        
            print("\n")
            DisplayMenu()
        elif Choice == "2":
            ValidInput = True
            print("\n")
            DisplayData()
            print("\n")
            DisplayMenu()
        elif Choice == "22":
            ValidInput = True
            print("\n")
            DisplayDataShort()
            print("\n")
            DisplayMenu()
        elif Choice == "3":
            ValidInput = True
        elif Choice == "4":
            ValidInput = True
            if len(ChronilogicalOrder) > 9:
                FindTopActorsAndDirectors()
            else:
                print("You can use this feature once you have seen 10 films")
            DisplayMenu()
        elif Choice == "5":
            ValidInput = True
            if len(ChronilogicalOrder) > 19:
                Graph()
            else:
                print("You can use this feature once you have seen 20 films")
            print("\n")
            DisplayMenu()
        elif Choice == "6":
            ValidInput = True
            print("\n")
            print("Which Actor or Director?")
            Actor = input()
            print("\n")
            Directors = {}
            Actors = {}
            for i in range (0,len(IDList)):    
                for b in range(0,2):
                    castMember = FilmCast[IDList[i]][b]
                    if castMember == "N/A":
                        break

                    if castMember in Directors:
                        x = Directors[castMember]
                        Directors[castMember] = x + 1
                    else:
                        Directors[castMember] = 1
                for c in range(2,len(FilmCast[IDList[i]])):
                    castMember = FilmCast[IDList[i]][c]
                    if castMember in Actors:
                        x = Actors[castMember]
                        Actors[castMember] = x + 1
                    else:
                        Actors[castMember] = 1

            if Actor in Actors:
                FindNumberOfActorFilms(Actor)
            elif Actor in Directors:
                FindNumberOfActorFilms(Actor)
            else: 
                print("Couldn't find any data on ",Actor)
            DisplayMenu()
        elif Choice == "7":
            ValidInput = True
            ByViewCount()
            print("\n")
            DisplayMenu()
        elif Choice == "8":
            ValidInput = True
            print("MORE DATA".rjust(22," "))
            print("\n")
            print("1"+("LIST FILMS IN ORDER OF X").rjust(40,"-"))
            time.sleep(0.01)
            print("2"+("TOTAL RUNTIME").rjust(40,"-"))
            time.sleep(0.01)
            print("3"+("""LIST COMPOSERS""").rjust(40,"-"))
            time.sleep(0.01)
            print("4"+("""TOP GENRES""").rjust(40,"-"))
            time.sleep(0.01)
            print("5"+("""TOP FILMS OF GENRE X""").rjust(40,"-"))
            time.sleep(0.01)
            print("6"+("""TOP FILMS FROM YEAR X""").rjust(40,"-"))
            time.sleep(0.01)
            ValidInputB = False
            while ValidInputB == False:
                print("\n")
                Choice = input()
                if Choice == "1":
                    ValidInputB = True
                    print("\n")
                    print("LIST FILMS IN ORDER OF:".rjust(22," "))
                    print("\n")
                    print("1"+("""IN ORDER OF IMDB RATING""").rjust(40,"-"))
                    time.sleep(0.01)
                    print("2"+("""IN ORDER OF RELEASE YEAR""").rjust(40,"-"))
                    time.sleep(0.01)
                    ValidInputC = False
                    while ValidInputC == False:
                        Choice = input()
                        if Choice == "1":
                            ValidInputC = True
                            if len(ChronilogicalOrder) > 9:
                                ByRating()
                            else:
                                print("You can use this feature once you have seen 10 films")
                            print("\n")
                        elif Choice == "2":
                            ValidInputC = True
                            ByReleaseYear()
                            print("\n")
                elif Choice == "2":
                    ValidInputB = True
                    print("\n")
                    RunTime = 0
                    for number in RunTimes:
                        RunTime = RunTime + int(number)
                    if len(ChronilogicalOrder) > 0:
                        hours = int(RunTime)/60
                        days = hours/24
                        weeks = days/7
                        print("Since January 1st 2020, You have seen: ")
                        print(round(hours,2),"hours of films")
                        print(round(days,2),"days of films")
                        print(round(weeks,2),"weeks of films")
                        print("\n")
                    else:
                        print("Watch a film before using this feature")
                        print("\n")
                elif Choice == "3":
                    ValidInputB = True
                    print("\n")
                    if len(ChronilogicalOrder) > 19:
                        ComposerCount = {}
                        for i in range(len(Composers)):
                            if Composers[i] not in ComposerCount:
                                ComposerCount[Composers[i]] = 1
                            else:
                                Temp = ComposerCount[Composers[i]]
                                ComposerCount[Composers[i]] = Temp + 1
                        del ComposerCount["no composers"]
                        DictValues = list(ComposerCount.values())
                        TopComposerList = []
                        for numberx in DictValues:
                            x = 0
                            for number in DictValues:
                                if number > x:
                                    x = number
                            DictValues.remove(int(x))
                            TopComposerList.append(x)
                        TopComposerNames = []

                        TopComposerNames = []
                        for Value in TopComposerList:
                            Remove = -1
                            for Composer in ComposerCount:
                                Remove = Remove + 1
                                if int(ComposerCount[Composer]) == int(Value):
                                    TopComposerNames.append(Composer)
                                    del ComposerCount[Composer]
                                    break
                    
                        MaxStringLength = 5           
                        for Composer in TopComposerNames:
                            if len(Composer) > MaxStringLength:
                                MaxStringLength = len(Composer)
                        MaxStringLength = MaxStringLength + 2
                        String = ("%-"+str(MaxStringLength)+"s %-14s")
                        print(String %("COMPOSER:","TOTAL:"))
                        for i in range (0,15):
                            print(String %(TopComposerNames[i],TopComposerList[i]))
                        print("\n")
                        print("\n")
                    else:
                        print("You can use this feature once you have seen 20 films")
                        print("\n")
                elif Choice == "4":
                    ValidInputB = True
                    print("\n")
                    GenreCount = {}
                    for id in IDList:
                        TempGenreList = Genres[id]
                        for thing in TempGenreList:
                            if thing not in GenreCount:
                                GenreCount[thing] = 1
                            else:
                                x = GenreCount[thing]
                                GenreCount[thing] = x + 1
                    TopGenres = SortDict(GenreCount)
                    
                    TopGenreNames = []
                    for Value in TopGenres:
                        Remove = -1
                        for Genre in GenreCount:
                            Remove = Remove + 1
                            if int(GenreCount[Genre]) == int(Value):
                                TopGenreNames.append(Genre)
                                del GenreCount[Genre]
                                break
                    MaxStringLength = 0
                    for Genre in TopGenreNames:
                        if len(Genre) > MaxStringLength:
                            MaxStringLength = len(Genre)
                    MaxStringLength = MaxStringLength + 2
                    String = ("%-"+str(MaxStringLength)+"s %-14s")
                    print(String %("GENRE:","TOTAL:"))
                    for i in range (0,len(TopGenres)):
                        print(String %(TopGenreNames[i],TopGenres[i]))
                    print("\n")
                elif Choice == "5":
                    ValidInputB = True
                    TopFilmsByGenre()
                    print("\n")
                elif Choice == "6":
                    ValidInputB = True
                    TopFilmsByYear()
                    print("\n")
            DisplayMenu() 
        elif Choice == "9":
            ValidInput = True
            if len(ChronilogicalOrder) > 20:
                ActorAlgorithm()
            else:
                print("You can use this feature once you have seen 20 films")
            print("\n")
            DisplayMenu()
        elif Choice == "99":
            ValidInput = True
            print(len(ChronilogicalOrder),"ChronilogicalOrder")
            print(len(IDList),"IDList")
            print(len(ListOfFilms),"ListOfFilms")
            print(len(Genres),"Genres")
            print(len(FilmCast),"FilmCast")
            print(len(DateList),"DateList")
            print(len(RunTimes),"RunTimes")
            print(len(Ratings),"Ratings")
            print(len(Composers),"Composers")
            print(len(releaseYear),"releaseYear")
            print("\n")
            DisplayMenu()
        elif Choice == "98":
            ValidInput = True
            SortList()
            print("\n")
            DisplayMenu()
        elif Choice == "97":
            ValidInput = True
            MovieDB = Cinemagoer()
            print("ID CHECK:")
            idInput = input()
            movie = MovieDB.get_movie(idInput)
            print(movie["title"])
            print("\n")
            DisplayMenu()
        elif Choice == "96":
            ValidInput = True
            MovieDB = Cinemagoer()
            print("ID TO FILM CAST")
            idInput = input()
            movie = MovieDB.get_movie(idInput)
            TempList = []
            try:
                directors = movie["directors"]
                if len(directors) == 1:
                    TempList.append(directors[0]["name"])
                    TempList.append("N/A")
                elif len(directors) > 1:
                    TempList.append(directors[0]["name"])
                    TempList.append(directors[1]["name"])
            except KeyError:
                print("No directors")
                TempList.append("N/A")
                TempList.append("N/A")
            try:
                cast = movie["cast"]
                if len(cast) == 1:
                    TempList.append(cast[0]["name"])
                elif len(cast) > 1:
                    MainCast = 0
                    for i in range (0,len(cast)):
                        TempList.append(cast[i]["name"])
                        if MainCast == 35:
                            break
                        else:
                            MainCast = MainCast + 1
            except:
                print('biug')
            string = ""
            for item in TempList:
                string = string + item + ","
            print(string)
            print("\n")
            DisplayMenu()







def TopFilmsByYear():
    print("Which Year?")
    choice = input()
    index = 0
    GOGO = 0
    yearFilmList = []
    items = releaseYear
    for thing in items:
        if choice in thing:
            GOGO = 1
    if GOGO == 1:
        yearFilmList = []
        for year in items:
            if choice in year:
                yearFilmList.append(ChronilogicalOrder[index])
            index = index + 1

        Listo = []
        index = 0
        for film in ListOfFilms:
            if film in yearFilmList:
                Listo.append(film)

        MaxStringLength = 0
        for film in Listo:
            if len(film) > MaxStringLength:
                MaxStringLength = len(film)
        MaxStringLength = MaxStringLength + 3
        if MaxStringLength < 20:
            MaxStringLength = 20
        String = ("%-4s %-"+str(MaxStringLength)+"s %-"+str(MaxStringLength)+"s")
        print("\n")
        print("Showing results for films released in",choice)
        print(String %(".","FILMS SEEN", "RANKED LIST"))
        print("\n")
        for i in range (0,len(yearFilmList)):
            time.sleep(0.001)
            print(String %((str(i+1)+":"),yearFilmList[i], Listo[i]))
    else:
        print("You haven't seen any films from this year.")


def TopFilmsByGenre():
    print("Which Genre?")
    choice = input()
    index = 0
    GOGO = 0
    genreFilmList = []
    items = Genres.values()
    for thing in items:
        if choice in thing:
            GOGO = 1
    if GOGO == 1:
        genreFilmList = []
        for genre in items:
            if choice in genre:
                genreFilmList.append(ChronilogicalOrder[index])
            index = index + 1

        Listo = []
        index = 0
        for film in ListOfFilms:
            if film in genreFilmList:
                Listo.append(film)

        MaxStringLength = 0
        for film in Listo:
            if len(film) > MaxStringLength:
                MaxStringLength = len(film)
        MaxStringLength = MaxStringLength + 3
        if MaxStringLength < 20:
            MaxStringLength = 20
        String = ("%-4s %-"+str(MaxStringLength)+"s %-"+str(MaxStringLength)+"s")
        print("\n")
        print(String %(".","FILMS SEEN", "RANKED LIST"))
        print("\n")
        for i in range (0,len(genreFilmList)):
            time.sleep(0.001)
            print(String %((str(i+1)+":"),genreFilmList[i], Listo[i]))
    else:
        print("nope")
        

def FindComposerFilms():
    print("Which Composer?")
    search = input()
    index = 0
    FoundList = []
    if search in Composers:
        for composer in Composers:
            if composer == search:
                FoundList.append(ChronilogicalOrder[index])
            index = index + 1
    if FoundList != 0:
        index2 = 1
        print("\n")
        print(".   FILM")
        for film in FoundList:
            if index2 < 10:
                print(str(index2)+":  "+film)
                index2 = index2 + 1
            else:
                print(str(index2)+": "+film)
                index2 = index2 + 1




def SortList():
    AlreadyCompared = []
    Sorted = False
    while Sorted == False:
        SortCount = 0
        for i in range (0,len(ListOfFilms)-2):
            Pass = 0
            for b in range (0,len(AlreadyCompared)):
                if (AlreadyCompared[b].find(ListOfFilms[i]) != -1) and (AlreadyCompared[b].find(ListOfFilms[i+1]) != -1):
                    print("pass",ListOfFilms[i],ListOfFilms[i+1])
                    SortCount = SortCount + 1
                    Pass = 1
            if Pass == 0:
                print("What is better? \n1        ",ListOfFilms[i],"\n2        ",ListOfFilms[i+1])
                ValidInput = False
                while ValidInput == False:
                    Choice = input()
                    if Choice == "2" or Choice == "1":
                        ValidInput = True
                    else:
                        print("What is better? \n1        ",ListOfFilms[i],"\n2        ",ListOfFilms[i+1])
                if Choice == "2":
                    ComparedString = (ListOfFilms[i+1] + " and " + ListOfFilms[i])
                    AlreadyCompared.append(ComparedString)
                    Buffer = ListOfFilms[i+1]
                    ListOfFilms[i+1] = ListOfFilms[i]
                    ListOfFilms[i] = Buffer
                elif Choice == "1":
                    ComparedString = (ListOfFilms[i] + " and " + ListOfFilms[i+1])
                    AlreadyCompared.append(ComparedString)
        if SortCount > len(ListOfFilms)-4:
            Sorted = True



def Graph():
    print("\n")
    print("1"+("NUMBER OF FILMS / TIME").rjust(40,"-"))
    time.sleep(0.01)
    print("2"+("FILMS PER MONTH").rjust(40,"-"))
    time.sleep(0.01)
    print("3"+("FILMS PER RELEASE YEAR").rjust(40,"-"))
    time.sleep(0.01)
    print("\n")
    choice = input()
    if choice == "1":
        import matplotlib.pyplot
        from matplotlib.dates import DateFormatter
        list_of_datetimes = []
        values = []
        index = 109
        CutDateList = DateList[108:]
        for date in CutDateList:
            print(date)
            my_date = datetime.strptime(date, "%d/%m/%Y")
            list_of_datetimes.append(my_date)
            values.append(index)
            index = index + 1
        dates = matplotlib.dates.date2num(list_of_datetimes)
        matplotlib.pyplot.figure(figsize=(14, 7))
        matplotlib.pyplot.plot_date(dates, values, marker=',', linestyle=':', color='r', markersize=2)
        matplotlib.pyplot.xlabel("DATE")
        matplotlib.pyplot.ylabel("FILMS SEEN")
        matplotlib.pyplot.legend()
        myFmt = DateFormatter("%b-%y")
        matplotlib.pyplot.gca().xaxis.set_major_formatter(myFmt)
        matplotlib.pyplot.show()
    elif choice == "2":
        import matplotlib.pyplot as plt
        from matplotlib.dates import DateFormatter
        list_of_datetimes = []
        values = []
        index = 109
        CutDateList = DateList[108:]
        for date in CutDateList:
            my_date = datetime.strptime(date, "%d/%m/%Y")
            list_of_datetimes.append(my_date)
            values.append(index)
            index = index + 1
        DateFrequencies = {}
        for date in list_of_datetimes:
            string = str(date.year) + "/" + str(date.month)
            if string not in DateFrequencies:
                DateFrequencies[string] = 1
            else:
                DateFrequencies[string] = DateFrequencies[string] + 1
        x = DateFrequencies.keys()
        y = DateFrequencies.values()
        x0 = []
        for item in x:
            item = item[2:]
            x0.append(item)
        plt.bar(x0,y)
        plt.xlabel('MONTH')
        plt.ylabel('NUMBER OF FILMS SEEN')
        plt.show()
    elif choice == "3":
        import matplotlib.pyplot as plt
        from matplotlib.dates import DateFormatter
        Dict = {}
        for year in releaseYear:
            if year not in Dict:
                Dict[year] = 1
            else:
                Dict[year] = Dict[year] + 1
        x = list(Dict.keys())
        n = len(x)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if int(x[j]) > int(x[j + 1]) :
                    x[j], x[j + 1] = x[j + 1], x[j]
        x0 = []
        for year in x:
            x0.append(year[2:])
        
        x_labels = list(Dict.keys())
        index = 0
        for thing in x_labels:
            if index % 2 == 0:
                x_labels.remove(thing)
            index = index + 1
        y = []
        for number in x:
            y.append(Dict[number])
        plt.locator_params(axis="x", nbins=4)
        plt.bar(x0,y)
        plt.xlabel('YEAR')
        plt.ylabel('NUMBER OF FILMS FROM YEAR')
        plt.show()



def ByReleaseYear():
    FilmWithDate = {}
    dateIndex = 0
    for film in ChronilogicalOrder:
        FilmWithDate[film] = float(releaseYear[dateIndex])
        dateIndex = dateIndex + 1
    SortedDict = sorted(FilmWithDate.items(), key=lambda x: x[1], reverse=True)
    MaxStringLength = 0
    for film in ChronilogicalOrder:
        if len(film) > MaxStringLength:
            MaxStringLength = len(film)
    MaxStringLength = MaxStringLength + 2
    String = ("%-5s %-"+str(MaxStringLength)+"s")
    print(String %("YEAR:","FILM:"))
    for i in range (0,len(ChronilogicalOrder)):
        print(String %((str(int(SortedDict[i][1]))+":"),SortedDict[i][0]))
    print("\n")


def ByViewCount():
    FilmWithViewCount = {}
    viewIndex = 0
    for film in ChronilogicalOrder:
        FilmWithViewCount[film] = float(ViewCount[viewIndex])
        viewIndex = viewIndex + 1
    SortedDict = sorted(FilmWithViewCount.items(), key=lambda x: x[1], reverse=True)
    MaxStringLength = 0
    for film in ChronilogicalOrder:
        if len(film) > MaxStringLength:
            MaxStringLength = len(film)
    MaxStringLength = MaxStringLength + 2
    String = ("%-"+str(MaxStringLength)+"s %-100s")
    String = ("%-6s %-"+str(MaxStringLength)+"s")
    print(String %("TIMES:","FILM:"))
    for i in range (0,len(ChronilogicalOrder)):
        if int(SortedDict[i][1]) != 1:
            print(String %((str(int(SortedDict[i][1]))),SortedDict[i][0]))
    print("\n")


def ByRating():
    FilmWithRating = {}
    RatingIndex = 0
    for film in ChronilogicalOrder:
        FilmWithRating[film] = float(Ratings[RatingIndex])
        RatingIndex = RatingIndex + 1
    SortedDict = sorted(FilmWithRating.items(), key=lambda x: x[1], reverse=True)
    MaxStringLength = 0
    for film in ChronilogicalOrder:
        if len(film) > MaxStringLength:
            MaxStringLength = len(film)
    MaxStringLength = MaxStringLength + 2
    String = ("%-5s %-"+str(MaxStringLength)+"s")
    print(String %("RATING:","FILM:"))
    for i in range (0,len(ChronilogicalOrder)):
        print(String %((str(SortedDict[i][1])+":"),SortedDict[i][0]))
    print("\n")


def FindNumberOfActorFilms(Actor):
    print("Films with "+Actor+":")
    print("\n")


    ChronicList = []
    ChronicCast = []
    x = 0
    FilmCount = 1
    bruh = []
    for thing in ChronilogicalOrder:
        bruh.append(thing)
        string = IDList[x]
        try:
            if Actor in FilmCast[string][0] or Actor in FilmCast[string][1]:
                ChronicList.append(thing)
                ChronicCast.append("D")
            else:
                if Actor in FilmCast[string] or Actor in FilmCast[string]:
                    ChronicList.append(thing)
                    ChronicCast.append("A")
                    
        except KeyError:
            string = IDList[x]
            
        x = x + 1
    
    Listo = []
    for film in ListOfFilms:
        if film in ChronicList:
            Listo.append(film)

    MaxStringLength = 0
    for film in Listo:
        if len(film) > MaxStringLength:
            MaxStringLength = len(film)
    MaxStringLength = MaxStringLength + 3
    if MaxStringLength < 20:
        MaxStringLength = 20
    String = ("%-4s %-3s %-"+str(MaxStringLength)+"s %-"+str(MaxStringLength)+"s")
    print("\n")
    print(String %("."," ","FILMS SEEN", "RANKED LIST"))
    print("\n")
    for i in range (0,len(ChronicList)):
        time.sleep(0.001)
        print(String %((str(i+1)+":"),ChronicCast[i], ChronicList[i], Listo[i]))

    print("\n")

            
def FindTopActorsAndDirectors():
    global FilmCast
    Directors = {}
    Actors = {}
    for i in range (0,len(IDList)):    
        for b in range(0,2):
            castMember = FilmCast[IDList[i]][b]
            if castMember == "N/A":
                break
            if castMember in Directors:
                x = Directors[castMember]
                Directors[castMember] = x + 1
            else:
                Directors[castMember] = 1
        for c in range(2,len(FilmCast[IDList[i]])):
            castMember = FilmCast[IDList[i]][c]
            if castMember in Actors:
                x = Actors[castMember]
                Actors[castMember] = x + 1
            else:
                Actors[castMember] = 1

    global TopActorNames, TopDirectorNames, TopActors, TopDirectors
    if len(ChronilogicalOrder) > 175:
        TopDirectors = SortDict50(Directors)
        TopActors = SortDict50(Actors)
    else:
        TopDirectors = SortDict(Directors)
        TopActors = SortDict(Actors)
    TopDirectorNames = []
    TopActorNames = []

    for Value in TopActors:
        Remove = -1
        for Actor in Actors:
            Remove = Remove + 1
            if int(Actors[Actor]) == int(Value):
                TopActorNames.append(Actor)
                del Actors[Actor]
                break
    for Value in TopDirectors:
        Remove = -1
        for Director in Directors:
            Remove = Remove + 1
            if int(Directors[Director]) == int(Value):
                TopDirectorNames.append(Director)
                del Directors[Director]
                break
    MaxStringLength = 0
    for actor in TopActorNames:
        if len(actor) > MaxStringLength:
            MaxStringLength = len(actor)
    for director in TopDirectorNames:
        if len(director) > MaxStringLength:
            MaxStringLength = len(director)
    MaxStringLength = MaxStringLength + 2
    String = ("%-"+str(MaxStringLength)+"s %-14"+"s %-"+str(MaxStringLength)+"s %-12"+"s")
    print(String %("ACTOR:","TOTAL:", "DIRECTOR:", "TOTAL:"))
    if len(ChronilogicalOrder) < 30:
        number = 5
    elif len(ChronilogicalOrder) > 175:
        number = 40
    else:
        number = 30
    for i in range (0,number):
        print(String %(TopActorNames[i],TopActors[i], TopDirectorNames[i],TopDirectors[i]))
        time.sleep(0.01)
    print("\n")

def ActorAlgorithm():
    global FilmCast
    Directors = {}
    Actors = {}
    for i in range (0,len(IDList)):    
        for b in range(0,2):
            castMember = FilmCast[IDList[i]][b]
            if castMember == "N/A":
                break
            if castMember in Directors:
                x = Directors[castMember]
                Directors[castMember] = x + 1
            else:
                Directors[castMember] = 1
        for c in range(2,len(FilmCast[IDList[i]])):
            castMember = FilmCast[IDList[i]][c]
            if castMember in Actors:
                x = Actors[castMember]
                Actors[castMember] = x + 1
            else:
                Actors[castMember] = 1

    global TopActorNames, TopDirectorNames, TopActors, TopDirectors
    TopDirectors = SortDict(Directors)
    TopActors = SortDict(Actors)
    TopDirectorNames = []
    TopActorNames = []

    for Value in TopActors:
        Remove = -1
        for Actor in Actors:
            Remove = Remove + 1
            if int(Actors[Actor]) == int(Value):
                TopActorNames.append(Actor)
                del Actors[Actor]
                break
    for Value in TopDirectors:
        Remove = -1
        for Director in Directors:
            Remove = Remove + 1
            if int(Directors[Director]) == int(Value):
                TopDirectorNames.append(Director)
                del Directors[Director]
                break
    ActorAverages = {}
    for actor in TopActorNames:
        ActorAverages[actor] = []
    #FilmCast = GetFilmCast()
    values = (FilmCast.values())
    values = list(values)
    numberInGroup = int((len(FilmCast.values())))
    for i in range(0,numberInGroup):
        rank = ListOfFilms.index(ChronilogicalOrder[i])
        for actor in values[i]:
            if actor in TopActorNames:
                ActorAverages[actor].append((numberInGroup-rank)/numberInGroup)

    ActorAveragesValues = {}
    for actor in TopActorNames:
        Goodness = 0
        Greatness = 0
        Consistency = 0
        for value in ActorAverages[actor]:
            if value > 0.95:
                Consistency = Consistency + 1
                if Greatness > 0:
                    GreatValue = 1+(0.1*(Greatness))
                    Goodness = Goodness + (value*((2)**GreatValue))
                else:
                    Goodness = Goodness + (value*2)
                Greatness = Greatness + 2.5
            elif value > 0.85:
                Consistency = Consistency + 1
                if Greatness > 0:
                    GreatValue = 1+(0.1*(Greatness))
                    Goodness = Goodness + (value*((1.5)**GreatValue))
                else:
                    Goodness = Goodness + (value*1.5)
                Greatness = Greatness + 1.5
            elif value > 0.8:
                Consistency = Consistency + 1
                if Greatness > 0:
                    GreatValue = 1+(0.1*(Greatness))
                    Goodness = Goodness + (value*((1.25)**GreatValue))
                else:
                    Goodness = Goodness + (value*1.25)
                Greatness = Greatness + 0.5
            elif value > 0.6:
                Consistency = Consistency + 1
                Goodness = Goodness + (value*1.15)
            elif value > 0.5:
                Goodness = Goodness + (value*1.1)
            elif value < 0.5:
                Goodness = Goodness + (value*0.85)
            elif value < 0.35:
                Goodness = Goodness + (value*0.5)
            elif value < 0.25:
                Goodness = Goodness + (value*0.3)
            elif value < 0.15:
                Goodness = Goodness + (value*0.2)
        Goodness = Goodness/int(len(ActorAverages[actor]))
        Multiplier = (Consistency * 0.04) + 1
        Goodness = Goodness * Multiplier
        ActorAveragesValues[actor] = Goodness



    DirectorAverages = {}
    for director in TopDirectorNames:
        DirectorAverages[director] = []
    #FilmCast = GetFilmCast()
    values = (FilmCast.values())
    values = list(values)
    numberInGroup = int((len(FilmCast.values())))
    for i in range(0,numberInGroup):
        rank = ListOfFilms.index(ChronilogicalOrder[i])
        for director in values[i]:
            if director in TopDirectorNames:
                DirectorAverages[director].append((numberInGroup-rank)/numberInGroup)

    DirectorAveragesValues = {}
    for director in TopDirectorNames:
        Goodness = 0
        Greatness = 0
        for value in DirectorAverages[director]:
            if value > 0.95:
                if Greatness > 0:
                    GreatValue = 1+(0.1*(Greatness))
                    Goodness = Goodness + (value*((2)**GreatValue))
                else:
                    Goodness = Goodness + (value*2)
                Greatness = Greatness + 2.5
            elif value > 0.85:
                if Greatness > 0:
                    GreatValue = 1+(0.1*(Greatness))
                    Goodness = Goodness + (value*((1.5)**GreatValue))
                else:
                    Goodness = Goodness + (value*1.5)
                Greatness = Greatness + 1.5
            elif value > 0.8:
                if Greatness > 0:
                    GreatValue = 1+(0.1*(Greatness))
                    Goodness = Goodness + (value*((1.25)**GreatValue))
                else:
                    Goodness = Goodness + (value*1.25)
                Greatness = Greatness + 0.5
            elif value > 0.5:
                Goodness = Goodness + (value*1.1)
            elif value < 0.5:
                Goodness = Goodness + (value*0.85)
            elif value < 0.35:
                Goodness = Goodness + (value*0.5)
            elif value < 0.25:
                Goodness = Goodness + (value*0.3)
            elif value < 0.15:
                Goodness = Goodness + (value*0.2)
        Goodness = Goodness/int(len(DirectorAverages[director]))
        DirectorAveragesValues[director] = Goodness


    BestDirectors = SortDict(DirectorAveragesValues)
    BestDirectorNames = []
    sort_ordersD = sorted(DirectorAveragesValues.items(), key=lambda x: x[1], reverse=True)
    for thing in sort_ordersD:
        BestDirectorNames.append(thing)








    BestActors = SortDict(ActorAveragesValues)
    BestActorNames = []
    sort_orders = sorted(ActorAveragesValues.items(), key=lambda x: x[1], reverse=True)
    for thing in sort_orders:
        BestActorNames.append(thing)
    
    MaxStringLength = 0
    for actor in BestActorNames:
        if len(actor[0]) > MaxStringLength:
            MaxStringLength = len(actor[0])
    MaxStringLength = MaxStringLength + 2
    String = ("%-4s %-"+str(MaxStringLength)+"s %-"+str(MaxStringLength)+"s")
    print("\n")
    print(String %("#","ACTOR:", "DIRECTOR:"))
    DeadList = ["Kenny Baker","Anthony Daniels","Stan Lee","Frank Oz"]
    for actor in sort_orders:
        if actor[0] in DeadList:
            sort_orders.remove(actor)
    for i in range (0,15):
        time.sleep(0.001)
        print(String %((str(i+1)+":"),sort_orders[i][0], sort_ordersD[i][0]))
    print("\n")








def FilmRankedInsertion(Film,RankedListSub):
    PositionFound = False
    SubList = list(RankedListSub)
    FilmsLeft = len(SubList)
    FilmReference = "PlaceHolder"
    RatingReference = 0
    FilmsAsked = []
    while PositionFound == False:
        if FilmsLeft > 0:
            if SubList[int(FilmsLeft/2)] not in FilmsAsked:
                       
                if FilmReference != SubList[int(FilmsLeft/2)]:
                    if FilmsLeft % 2 == 0:
                        print("Is",Film,"better than: ",SubList[int(FilmsLeft/2)])
                        FilmReference = SubList[int(FilmsLeft/2)]
                    else:
                        print("Is",Film,"better than: ",SubList[int((FilmsLeft/2)-0.5)])
                        FilmReference = SubList[int(FilmsLeft/2)]
                    print("Y or N")
                    ValidInput = False
                    while ValidInput == False:
                        Choice = input()
                        if Choice == "y" or Choice == "Y" or Choice == "n" or Choice == "N":
                            ValidInput = True
                        else:
                            print("Y or N")
                    FilmsAsked.append(FilmReference)
                    if Choice == "y" or Choice == "Y":
                        if FilmsLeft % 2 == 0:
                            FilmsLeft = FilmsLeft/2
                            del SubList[int(FilmsLeft):int(len(SubList))]
                            RatingReference = 1
                        else:
                            if len(SubList) == 1:
                                RatingReference = 1
                                FilmsLeft = 0
                            else:
                                RatingReference = 1
                                FilmsLeft = (FilmsLeft / 2) - 0.5
                                del SubList[int(FilmsLeft):int(len(SubList))]
                    elif Choice == "n" or Choice == "N":
                        if FilmsLeft % 2 == 0:
                            FilmsLeft = int(len(SubList)/2)
                            del SubList[0:FilmsLeft]
                            FilmsLeft = len(SubList)
                            RatingReference = - 1
                        else:
                            if len(SubList) == 1:
                                RatingReference = - 1
                                FilmsLeft = 0
                            else:
                                RatingReference = - 1
                                FilmsLeft = len(SubList)
                                del SubList[0:int((int(FilmsLeft)/2)-0.5)]
                                FilmsLeft = len(SubList)
                else:
                    FilmsLeft = 0
            else:
                FilmsLeft = 0
        else:
            PositionFound = True
    if RatingReference == 1:
        ListOfFilms.insert((ListOfFilms.index(FilmReference)),Film)
    elif RatingReference == -1:
        ListOfFilms.insert((ListOfFilms.index(FilmReference))+1,Film)
        
            
                    
def DisplayData():
    MaxStringLength = 0
    for film in ListOfFilms:
        if len(film) > MaxStringLength:
            MaxStringLength = len(film)
    MaxStringLength = MaxStringLength + 3
    if MaxStringLength < 20:
        MaxStringLength = 20
    String = ("%-4s %-"+str(MaxStringLength)+"s %-18"+"s %-"+str(MaxStringLength)+"s")
    print(String %(".","FILMS SEEN","DATE", "RANKED LIST"))
    print("\n")
    for i in range (0,len(ChronilogicalOrder)):
        time.sleep(0.001)
        print(String %((str(i+1)+":"),ChronilogicalOrder[i],DateList[i], ListOfFilms[i]))


def DisplayDataShort():
    MaxStringLength = 0
    for film in ListOfFilms:
        if len(film) > MaxStringLength:
            MaxStringLength = len(film)
    MaxStringLength = MaxStringLength + 3
    if MaxStringLength < 20:
        MaxStringLength = 20
    String = ("%-4s %-"+str(MaxStringLength)+"s %-13"+"s")
    print(String %(".","FILMS SEEN","DATE"))
    print("\n")
    for i in range (len(ChronilogicalOrder) - 21 ,len(ChronilogicalOrder)):
        time.sleep(0.001)
        print(String %((str(i+1)+":"),ChronilogicalOrder[i],DateList[i]))



def GetMovieInfo(film):
    global RunTime
    global FilmCast
    MovieDB = Cinemagoer()
    PossibleFilms = MovieDB.search_movie(film)
    if len(PossibleFilms) == 0:
        print("No info found for this film")
    FilmFound = False
    SlimChance = 0
    for PossibleFilm in PossibleFilms:
        if SlimChance == 5:
            IDList.append("N/A")
            break
        SlimChance = SlimChance + 1
        if FilmFound == True:
            break
        id = PossibleFilm.getID()
        movie = MovieDB.get_movie(id)
        try:
            cast = movie["cast"]
            directors = movie["directors"]
        except KeyError:
            break
        print("\n")
        print("Is this the film you saw?  Y or N")
        try:
            print(movie["title"]," (",movie["year"], ")\nDirector: ",directors[0]["name"],"\nStarring: ",cast[0]["name"]," and ",cast[1]["name"])
        except KeyError:
            break
        except IndexError:
            break
        Input = input()
        if Input == "y" or Input == "Y" or Input == "q":
            MovieRunTime = movie["runtime"][0]
            

            movieG = MovieDB.get_movie(str(id))
            genreTemp = movieG["genres"]
            try:
                Rating = movieG["rating"]
            except KeyError:
                Rating = 5.0

            try:
                Composer = (movie["composers"][0])
            except KeyError:
                Composer = ("no composers")
            
            Year = movieG["year"]
            

            Genres[id] = genreTemp
            string = ""
            for item in genreTemp:
                string = string + item + ","
            FilmFound = True
            MainCast = 0
            MainDirectors = 0
            
            string = id
            TempList = []
            try:
                directors = movie["directors"]
                if len(directors) == 1:
                    TempList.append(directors[0]["name"])
                    TempList.append("N/A")
                elif len(directors) > 1:
                    TempList.append(directors[0]["name"])
                    TempList.append(directors[1]["name"])
            except KeyError:
                print("No directors")
                TempList.append("N/A")
                TempList.append("N/A")
            try:
                cast = movie["cast"]
                if len(cast) == 1:
                    TempList.append(cast[0]["name"])
                elif len(cast) > 1:
                    MainCast = 0
                    for i in range (0,len(cast)):
                        TempList.append(cast[i]["name"])
                        if MainCast == 35:
                            break
                        else:
                            MainCast = MainCast + 1
            except KeyError:
                print("No Actors")
            FilmCast[string] = TempList
            string = ""
            today = date.today()
            Date = today.strftime("%d/%m/%Y")
            #FilmObjects.append(Film(movie["title"],FilmCast[id],MovieRunTime,Date,id))
            

    if FilmFound == False:
        return ("N/A","N/A","N/A","N/A","N/A","N/A")
    return (movie["title"],id,MovieRunTime,Rating,Year,Composer)
    


def SortDict(Dict):
    DictValues = list(Dict.values())
    Top10 = []
    bruh = []
    for i in range(0,30):
        bruh.append(i)
        x = 0
        for number in DictValues:
            if int(number) > x:
                x = int(number)
        try:
            DictValues.remove(str(x))
        except ValueError:
            try:
                DictValues.remove(int(x))
            except ValueError:
                break
        Top10.append(x)
    return Top10

def SortDict50(Dict):
    DictValues = list(Dict.values())
    Top10 = []
    bruh = []
    for i in range(0,40):
        bruh.append(i)
        x = 0
        for number in DictValues:
            if int(number) > x:
                x = int(number)
        try:
            DictValues.remove(str(x))
        except ValueError:
            try:
                DictValues.remove(int(x))
            except ValueError:
                break
        Top10.append(x)
    return Top10




def TranslateID():
    print(ChronilogicalOrder)
    MovieDB = imdb.IMDb()
    x = 0
    for id in IDList:
        movie = MovieDB.get_movie(id)
        print(movie["title"])
        print(ChronilogicalOrder[x])
        print("\n")
        x = x +1



def GetID():
    MovieDB = imdb.IMDb()
    Film = "Project Power"
    PossibleFilms = MovieDB.search_movie(Film)
    id = PossibleFilms[0].getID()
    movie = MovieDB.get_movie(id)
    try:
        cast = movie["cast"]
        directors = movie["directors"]
    except KeyError:
        print("wow")
    print("\n")
    print("Is this the film you saw?  Y or N")
    try:
        print(movie["title"]," (",movie["year"], ")\nDirector: ",directors[0]["name"],"\nStarring: ",cast[0]["name"]," and ",cast[1]["name"])
    except KeyError:
        print("wow")
    Input = input()
    if Input == "y" or Input == "Y" or Input == "q":
        print(id)



def GetFilmCast():
    FilmCast = {}
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("FILM CAST") != -1:
            Checked = 1
        else:
            n += 1
    x = n + 1
    Checked = 0
    number = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            line = lines[x].rstrip("\n")
            CastList = [x.strip() for x in line.split(',')]
            del CastList[-1]
            string = (IDList[number])
            
            FilmCast[string] = CastList
            x = x+1
            number = number + 1
    return FilmCast



def GetFilmGenres():
    Genres = {}
    n = 0
    Checked = 0
    while Checked == 0:
        if lines[n].find("GENRES") != -1:
            Checked = 1
        else:
            n += 1
    x = n + 1
    Checked = 0
    number = 0
    while Checked == 0:
        if lines[x] == "\n":
            Checked =1
        else:
            line = lines[x].rstrip("\n")
            genreList = [x.strip() for x in line.split(',')]
            del genreList[-1]
            string = (IDList[number])
            Genres[string] = genreList
            x = x+1
            number = number + 1
    return Genres



def GapFilling():
    film = input("What Film?")
    MovieDB = imdb.IMDb()
    PossibleFilms = MovieDB.search_movie(film)
    if len(PossibleFilms) == 0:
        print("No info found for this film")
    FilmFound = False
    SlimChance = 0
    for PossibleFilm in PossibleFilms:
        if SlimChance == 5:
            IDList.append("N/A")
            break
        SlimChance = SlimChance + 1
        if FilmFound == True:
            break
        id = PossibleFilm.getID()
        movie = MovieDB.get_movie(id)
        try:
            cast = movie["cast"]
            directors = movie["directors"]
        except KeyError:
            break
        print("\n")
        print("Is this the film you saw?  Y or N")
        try:
            print(movie["title"]," (",movie["year"], ")\nDirector: ",directors[0]["name"],"\nStarring: ",cast[0]["name"]," and ",cast[1]["name"])
        except KeyError:
            break
        except IndexError:
            break
        Input = input()
        if Input == "y" or Input == "Y" or Input == "q":
            string = (IDList[len(FilmCast)])
            TempList = []
            try:
                directors = movie["directors"]
                if len(directors) == 1:
                    TempList.append(directors[0]["name"])
                    TempList.append("N/A")
                elif len(directors) > 1:
                    TempList.append(directors[0]["name"])
                    TempList.append(directors[1]["name"])
            except KeyError:
                print("No directors")
                TempList.append("N/A")
                TempList.append("N/A")
            try:
                cast = movie["cast"]
                if len(cast) == 1:
                    TempList.append(cast[0]["name"])
                elif len(cast) > 1:
                    MainCast = 0
                    for i in range (0,len(cast)):
                        TempList.append(cast[i]["name"])
                        if MainCast == 35:
                            break
                        else:
                            MainCast = MainCast + 1
            except KeyError:
                print("No Actors")
            FilmCast[string] = TempList
            break


def FindID():
    number = input("What number in ID list?")
    print(ChronilogicalOrder[int(number)-1])
    film = ChronilogicalOrder[int(number)-1]
    MovieDB = imdb.IMDb()
    PossibleFilms = MovieDB.search_movie(film)
    if len(PossibleFilms) == 0:
        print("No info found for this film")
    FilmFound = False
    SlimChance = 0
    for PossibleFilm in PossibleFilms:
        if SlimChance == 5:
            break
        SlimChance = SlimChance + 1
        if FilmFound == True:
            break
        id = PossibleFilm.getID()
        movie = MovieDB.get_movie(id)
        try:
            cast = movie["cast"]
        except KeyError:
            cast = ["UNKNOWN CAST"]
        try:
            directors = movie["directors"]
        except KeyError:
            directors = ["UNKNOWN DIRECTOR"]
            print("")
        print("\n")
        print("Is this the film you saw?  Y or N")
        try:
            print(movie["title"]," (",movie["year"], ")\nDirector: ",directors[0]["name"],"\nStarring: ",cast[0]["name"]," and ",cast[1]["name"])
        except KeyError:
            break
        except IndexError:
            break
        except TypeError:
            print("")
        Input = input()
        if Input == "y" or Input == "Y" or Input == "q":
            print(id)

            break

def _DebugFilmInfo(film):
    global RunTime
    MovieDB = imdb.IMDb()
    PossibleFilms = MovieDB.search_movie(film)
    if len(PossibleFilms) == 0:
        print("No info found for this film")
    FilmFound = False
    SlimChance = 0
    for PossibleFilm in PossibleFilms:
        if SlimChance == 5:
            IDList.append("N/A")
            break
        SlimChance = SlimChance + 1
        if FilmFound == True:
            break
        id = PossibleFilm.getID()
        movie = MovieDB.get_movie(id)
        try:
            cast = movie["cast"]
            directors = movie["directors"]
        except KeyError:
            break
        print("\n")
        print("Is this the film you saw?  Y or N")
        try:
            print(movie["title"]," (",movie["year"], ")\nDirector: ",directors[0]["name"],"\nStarring: ",cast[0]["name"]," and ",cast[1]["name"])
        except KeyError:
            break
        except IndexError:
            break
        Input = input()
        if Input == "y" or Input == "Y" or Input == "q":
            MovieRunTime = movie["runtime"][0]
            print("Runtime:",MovieRunTime)
            print("ID:",id)
            FilmFound = True
            MainCast = 0
            MainDirectors = 0
            string = id
            TempList = []
            try:
                directors = movie["directors"]
                if len(directors) == 1:
                    TempList.append(directors[0]["name"])
                    TempList.append("N/A")
                elif len(directors) > 1:
                    TempList.append(directors[0]["name"])
                    TempList.append(directors[1]["name"])
            except KeyError:
                print("No directors")
                TempList.append("N/A")
                TempList.append("N/A")
            try:
                cast = movie["cast"]
                if len(cast) == 1:
                    TempList.append(cast[0]["name"])
                elif len(cast) > 1:
                    MainCast = 0
                    for i in range (0,len(cast)):
                        TempList.append(cast[i]["name"])
                        if MainCast == 35:
                            break
                        else:
                            MainCast = MainCast + 1
            except KeyError:
                print("No Actors")
            newString = ""
            for thing in TempList:
                newString += thing
                newString += ","
            print("Cast:",newString)
            if movie["title"] in ChronilogicalOrder:
                print("Position:",ChronilogicalOrder.index(movie["title"]))

def GENRES():
    Genres = {}
    MovieDB = imdb.IMDb()
    for id in IDList:
        movie = MovieDB.get_movie(str(id))
        genreTemp = movie["genres"]
        print(genreTemp)
        Genres[id] = genreTemp 
    return Genres
        
def CreateDatedList():
    global releaseYear
    global Composers
    global Ratings
    releaseYear = []
    Composers = []
    Ratings = []
    MovieDB = imdb.IMDb()
    for id in IDList:
        movie = MovieDB.get_movie(str(id))
        print(movie["title"])
        print(movie["rating"])
        print(movie["year"])
        try:
            print(movie["composers"][0])
            Composers.append(movie["composers"][0])
        except KeyError:
            print("no composers")
            Composers.append("no composers")
        print("\n")
        releaseYear.append(movie["year"])
        Ratings.append(movie["rating"])


DateList = GetDates()
RunTimes = GetRuntimes()
IDList = GetIDs()
ViewCount = GetViewCount()


Ratings = GetRatings()
releaseYear = GetReleaseYears()
Composers = GetComposers()

#CreateDatedList()
#RunTime = RUNTIME(RunTime)
global FilmCast
FilmCast = GetFilmCast()
values = (FilmCast.values())
values = list(values)
ListOfFilms = GetRankedList()
ChronilogicalOrder = GetWatchList()
global Genres
Genres = GetFilmGenres()
OutPutLines = CreateLines()
MakeBackup()
#FilmObjects = CreateFilmObjects()
DisplayMenu()
OutPutLines = CreateLines()
EditTextFile()

















