import FILMCLASS
import CLIPCLASS
import DOCUMENTARYCLASS
import SERIESCLASS
import ACTOR
import time
import os

def loading():
    print('loading program...')
    myFile = open('database.txt', 'r')
    info = myFile.read().split('\n')
    myFile.close()

    for i in range(len(info)):
        if '[' in info[i]:
            info_list = info[i].split(',',7)
        else:
            info_list = info[i].split(',')
        mydic = {}
        INFO_MOVIES.append(
            {'type':info_list[0],'name': info_list[1], 'director': info_list[2], 'IMDB': info_list[3], 'url': info_list[4],'duration': info_list[5],'episodes': info_list[6],'casts': info_list[7]})
    print('The information was loaded successfully')
    time.sleep(2)
    os.system('cls')
def update_file():
    my_file = open('database.txt', 'w')
    for i in range(len(INFO_MOVIES)):
        if i != len(INFO_MOVIES) - 1:
            my_file.write(INFO_MOVIES[i]['type'] + ',' + INFO_MOVIES[i]['name'] + ',' + INFO_MOVIES[i]['director'] + ',' + str(INFO_MOVIES[i]['IMDB']) + ',' + INFO_MOVIES[i]['url'] + ',' +INFO_MOVIES[i]['duration'] + ',' + str(INFO_MOVIES[i]['episodes'])+','+str(INFO_MOVIES[i]['casts']) +'\n')
        else:
            my_file.write(INFO_MOVIES[i]['type'] + ',' + INFO_MOVIES[i]['name'] + ',' + INFO_MOVIES[i]['director'] + ',' + str(INFO_MOVIES[i]['IMDB']) + ',' + INFO_MOVIES[i]['url'] + ',' +INFO_MOVIES[i]['duration'] + ',' +str(INFO_MOVIES[i]['episodes'])+','+str(INFO_MOVIES[i]['casts']))
    my_file.close()
    exit()
def film():
    while True:
        menu_number = int(input('1.add film\n'
                                '2.edit film\n'
                                '3.search film\n'
                                '4.search advanced\n'
                                '5.remove film\n'
                                '6.qrcode url\n'
                                '7.download film\n'
                                '8. back\n'
                                'menu_number:: '))
        if menu_number==8:
            break
        if menu_number==1:
            name=input('film name: ').lower()
            director=input('director name: ').lower()
            IMDB=float(input('IMDB Score: '))
            url=input('url: ')
            duration=input('duration: ' )
            cast=ACTOR.Actor.list_actor()
            info_user=FILMCLASS.Film(INFO_MOVIES,name,director,IMDB,url,duration,cast)
            result=info_user.add_film()
            if result==False:
                print('This movie is available')
            else:
                INFO_MOVIES.append(result)
                print('New movie added')
        elif menu_number==2:
            name=input('name: ').lower()
            result=FILMCLASS.Film(INFO_MOVIES,name).edit_film()
            if result==False:
                print('There is no movie with this name')
            else:
                for i in INFO_MOVIES:
                    if name in i['name']:
                        i[result[1]]=result[0]
        elif menu_number==3:
            FILMCLASS.Film(INFO_MOVIES).search_film()
        elif menu_number==4:
            a=input('time A (ex: 25:00):')
            b=input('time B (ex: 28:00):')
            FILMCLASS.Film(INFO_MOVIES).search_advanced_film(a,b)
        elif menu_number==5:
            name=input('film name: ').lower()
            result=FILMCLASS.Film(INFO_MOVIES,name).remove_film()
            if type(result) == int:
                count = -1
                for i in range(len(INFO_MOVIES)):
                    if INFO_MOVIES[i]['type'] == 'film':
                        count += 1
                        if count == result:
                            del INFO_MOVIES[i]
                            break
            else:
                print(result)
        elif menu_number==6:
            name=input('film name: ').lower()
            print(FILMCLASS.Film(INFO_MOVIES,name).qrrcode_film())
        elif menu_number==7:
            name=input('film name: ').lower()
            result=FILMCLASS.Film(INFO_MOVIES,name).download_film()
            print(result)
def clip():
    while True:
        menu_number = int(input('1.add clip\n'
                                '2.edit clip\n'
                                '3.search clip\n'
                                '4.search advanced\n'
                                '5.remove clip\n'
                                '6.qrcode url\n'
                                '7.download film\n'
                                '8. back\n'
                                'menu_number:: '))
        if menu_number==8:
            break
        if menu_number==1:
            name=input('clip name: ').lower()
            director=input('director name: ').lower()
            IMDB=float(input('IMDB Score: '))
            url=input('url: ')
            duration=input('duration: ' )
            cast=ACTOR.Actor.list_actor()
            info_user=CLIPCLASS.Clip(INFO_MOVIES,name,director,IMDB,url,duration,cast)
            result=info_user.add_clip()
            if result==False:
                print('This movie is available')
            else:
                INFO_MOVIES.append(result)
                print('New movie added')
        elif menu_number==2:
            name=input('name: ').lower()
            result=CLIPCLASS.Clip(INFO_MOVIES,name).edit_clip()
            if result==False:
                print('There is no movie with this name')
            else:
                for i in INFO_MOVIES:
                    if name in i['name']:
                        i[result[1]]=result[0]

        elif menu_number==3:
            CLIPCLASS.Clip(INFO_MOVIES).search_clip()
        elif menu_number==4:
            a=input('time A (ex: 25:00):')
            b=input('time B (ex: 28:00):')
            CLIPCLASS.Clip(INFO_MOVIES).search_advanced_clip(a,b)
        elif menu_number==5:
            name=input('clip name: ').lower()
            result=CLIPCLASS.Clip(INFO_MOVIES,name).remove_clip()
            if type(result) == int:
                count = -1
                for i in range(len(INFO_MOVIES)):
                    if INFO_MOVIES[i]['type'] == 'clip':
                        count += 1
                        if count == result:
                            del INFO_MOVIES[i]
                            break
            else:
                print(result)

        elif menu_number==6:
            name=input('clip name: ').lower()
            print(CLIPCLASS.Clip(INFO_MOVIES,name).qrrcode_clip())
        elif menu_number == 7:
            name = input('film name: ').lower()
            result = FILMCLASS.Film(INFO_MOVIES, name).download_film()
            print(result)
def documentary():
    while True:
        menu_number = int(input('1.add documentary\n'
                                '2.edit documentary\n'
                                '3.search documentary\n'
                                '4.search advanced\n'
                                '5.remove documentary\n'
                                '6.qrcode url\n'
                                '7.download film\n'
                                '8. back\n'
                                'menu_number:: '))
        if menu_number == 8:
            break
        if menu_number == 1:
            name = input('documentary name: ').lower()
            director = input('director name: ').lower()
            IMDB = float(input('IMDB Score: '))
            url = input('url: ')
            duration = input('duration: ')
            cast = ACTOR.Actor.list_actor()
            episode=int(input('Number of episodes of the series: '))
            info_user = DOCUMENTARYCLASS.Documentary(INFO_MOVIES, name, director, IMDB, url, duration, cast,episode)
            result = info_user.add_documentary()
            if result == False:
                print('This movie is available')
            else:
                INFO_MOVIES.append(result)
                print('New movie added')
        elif menu_number == 2:
            name = input('name: ').lower()
            result = DOCUMENTARYCLASS.Documentary(INFO_MOVIES, name).edit_documentary()
            if result == False:
                print('There is no movie with this name')
            else:
                for i in INFO_MOVIES:
                    if name in i['name']:
                        i[result[1]] = result[0]

        elif menu_number == 3:
            DOCUMENTARYCLASS.Documentary(INFO_MOVIES).search_documentary()
        elif menu_number == 4:
            a = input('time A (ex: 25:00):')
            b = input('time B (ex: 28:00):')
            DOCUMENTARYCLASS.Documentary(INFO_MOVIES).search_advanced_documentary(a, b)
        elif menu_number == 5:
            name = input('documentary name: ').lower()
            result = DOCUMENTARYCLASS.Documentary(INFO_MOVIES, name).remove_documentary()
            if type(result) == int:
                count = -1
                for i in range(len(INFO_MOVIES)):
                    if INFO_MOVIES[i]['type'] == 'documentary':
                        count += 1
                        if count == result:
                            del INFO_MOVIES[i]
                            break
            else:
                print(result)
        elif menu_number == 6:
            name = input('documentary name: ').lower()
            print(DOCUMENTARYCLASS.Documentary(INFO_MOVIES, name).qrrcode_documentary())
        elif menu_number==7:
            name=input('film name: ').lower()
            result=FILMCLASS.Film(INFO_MOVIES,name).download_film()
            print(result)
def series():
    while True:
        menu_number = int(input('1.add series\n'
                                '2.edit series\n'
                                '3.search series\n'
                                '4.search advanced\n'
                                '5.remove series\n'
                                '6.qrcode url\n'
                                '7.download film\n'
                                '8. back\n'
                                'menu_number:: '))
        if menu_number == 8:
            break
        if menu_number == 1:
            name = input('series name: ').lower()
            director = input('director name: ').lower()
            IMDB = float(input('IMDB Score: '))
            url = input('url: ')
            duration = input('duration: ')
            cast = ACTOR.Actor.list_actor()
            episode=int(input('Number of episodes of the series: '))
            info_user = SERIESCLASS.Series(INFO_MOVIES, name, director, IMDB, url, duration, cast,episode)
            result = info_user.add_series()
            if result == False:
                print('This movie is available')
            else:
                INFO_MOVIES.append(result)
                print('New movie added')
                print(INFO_MOVIES)
        elif menu_number == 2:
            name = input('name: ').lower()
            result = SERIESCLASS.Series(INFO_MOVIES, name).edit_series()
            if result == False:
                print('There is no movie with this name')
            else:
                for i in INFO_MOVIES:
                    if name in i['name']:
                        i[result[1]] = result[0]

        elif menu_number == 3:
            SERIESCLASS.Series(INFO_MOVIES).search_series()
        elif menu_number == 4:
            a = input('time A (ex: 25:00):')
            b = input('time B (ex: 28:00):')
            SERIESCLASS.Series(INFO_MOVIES).search_advanced_series(a, b)
        elif menu_number == 5:
            name = input('series name: ').lower()
            result = SERIESCLASS.Series(INFO_MOVIES, name).remove_series()
            if type(result)==int:
                count=-1
                for i in range(len(INFO_MOVIES)):
                    if INFO_MOVIES[i]['type']=='series':
                        count += 1
                        if count==result:
                            del INFO_MOVIES[i]
                            break
            else:
                print(result)
        elif menu_number == 6:
            name = input('series name: ').lower()
            print(SERIESCLASS.Series(INFO_MOVIES, name).qrrcode_series())
        elif menu_number==7:
            name=input('series name: ').lower()
            result=SERIESCLASS.Series(INFO_MOVIES,name).download_series()
            print(result)


INFO_MOVIES=[]
loading()
while True:
    movie_type=int(input('choose your movie type:\n'
                            '1.film\n'
                            '2.clip\n'
                            '3.series\n'
                            '4.documentary\n'
                            '5.exit and save\n'
                            'menu_number:: '))
    if movie_type==5:
        update_file()

    if movie_type==1:
        film()
    elif movie_type==2:
        clip()
    elif movie_type==3:
        series()
    elif movie_type==4:
        documentary()






