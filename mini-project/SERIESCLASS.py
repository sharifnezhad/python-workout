import MEDIA
import time
import pyqrcode
import ast

class Series (MEDIA.Media):

    def __init__(self,all_info,name=None,director=None,imd=None,url=None,duration=None,cast=None,episode=0,type='series'):
        MEDIA.Media.__init__(self,name,director,imd,url,duration,cast)
        self.type = type
        self.episodes=episode
        self.series_list=[]
        for i in all_info:
            if self.type==i['type']:
                self.series_list.append(i)

    def add_series(self):
        for i in self.series_list:
            if self.name==i['name']:
                return False
        return {'type':self.type,'name': self.name, 'director': self.director, 'IMDB': self.imd_score, 'url': self.url,
             'duration':self.duration,'episodes': self.episodes, 'casts': self.casts}

    def edit_series(self):
        for i in self.series_list:
            if self.name in i['name']:
                menu_number=int(input('1.name\n'
                                      '2.director\n'
                                      '3.IMDB\n'
                                      '4.url\n'
                                      '5.duration\n'
                                      '6.casts\n'
                                      '7.episodes'))
                list=['name','director','IMDB','url','duration','casts','episodes']
                if menu_number==1:
                    self.name=input('name new: ')
                    return self.name,list[menu_number-1]
                elif menu_number==2:
                    self.director=input('director new: ')
                    return self.director, list[menu_number-1]
                elif menu_number==3:
                    self.imd_score=float(input('IMDB new:'))
                    return self.imd_score, list[menu_number-1]
                elif menu_number==4:
                    self.url=input('url new: ')
                    return self.url,list[menu_number-1]
                elif menu_number==5:
                    self.duration=input('duration new: ')
                    return self.duration, list[menu_number-1]
                elif menu_number==6:
                    name_cast=input('cast: ')


                    for i in self.series_list:
                        if '[' in i['casts']:
                            found = False
                            x = ast.literal_eval(i['casts'])
                            for j in range(len(x)):
                                if name_cast == ast.literal_eval(i['casts'])[j]:
                                    x[j] = input('Alternate cast: ')
                                    print('Your request was successful')
                                    found = True
                                    break
                                elif j + 1 == len(ast.literal_eval(i['casts'])) and found == False:
                                    print('This actor is not on this list :< ')
                            if found == True:
                                self.casts = x
                                break
                        elif name_cast == i['casts']:
                            self.casts = input('Alternate casts: ')
                            print('Your request was successful')
                            break
                    return self.casts, list[menu_number-1]
                elif menu_number==7:
                    self.episodes=int(input('episode new:'))
                    return self.episodes, list[menu_number - 1]
        return False
    def search_series(self):

        name = input('name: ').lower()
        for i in self.series_list:
            if name == i['name']:
                return Series(self.series_list,name).show_info(self.series_list)

        return print('The product is not available')
    def search_advanced_series(self,time_min,time_max):
        time_min=list(map(int, time_min.split(':')))
        time_max=list(map(int, time_max.split(':')))
        secen_min=time_min[0]*60+time_min[1]
        secen_max=time_max[0]*60+time_max[1]
        for i in self.series_list:
            time_series=list(map(int,i['duration'].split(':')))
            secen_movie=int(time_series[0])*60+int(time_series[1])
            if secen_movie>secen_min and secen_movie<secen_max:
                print('name: %s'% i['name'])
        time.sleep(3)
    def remove_series(self):
        num=0
        for i in self.series_list:
            if self.name== i['name']:
                return num
            num+=1
        return 'There is no movie with this name'
    def qrrcode_series(self):
        for i in self.series_list:
            if self.name== i['name']:
                url = pyqrcode.create(i['url'])
                url.png('qrcode-url-series.png',scale=6)
                return 'qrcode created'
        return 'There is no movie movie with this name'
    def download_series(self):
        for i in self.series_list:
            if self.name == i['name']:
                Series(self.series_list, self.name).download(i['url'])
                return 'The movie was downloaded'
        return 'There is no movie with this name'

