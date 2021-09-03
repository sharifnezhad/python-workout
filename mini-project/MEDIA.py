import ast
import pytube
from pytube import YouTube
# from pytube import Stream
class Media:
    def __init__(self,name,director,imd,url,duration,cast):
        self.name=name
        self.director=director
        self.imd_score=imd
        self.url=url
        self.duration=duration
        self.casts=cast
    def show_info(self,list):
        for i in list:
            if self.name in i['name']:
                if '[' in i['casts']:
                    str=' , '
                    print('name: %s \n'%i['name'],
                          'director: %s\n'% i['director'],
                          'IMDB: %s\n'% i['IMDB'],
                          'url: %s\n'% i['url'],
                          'duration: %s\n'% i['duration'],
                          'episodes :%s\n'% i['episodes'],
                          'casts :',str.join(ast.literal_eval(i['casts'])))
                else:
                    print('name: %s \n' % i['name'],
                          'director: %s\n' % i['director'],
                          'IMDB: %s\n' % i['IMDB'],
                          'url: %s\n' % i['url'],
                          'duration: %s\n' % i['duration'],
                          'episodes :%s\n' % i['episodes'],
                          'casts :%s' % i['casts'] )
    def download(self,url):
        resolution = int(input('Select your movie resolution:\n'
                           '1.1080p\n'
                           '2.720p\n'
                           '3.480p\n'
                           '4.360p\n'
                           '5.240p\n'
                           '6.144p\n'
                           'menu number: '))
        list = ['1080p', '720p', '480p', '360p', '240p', '144p']
        print('Downloading....')
        download_movie = pytube.YouTube(url).streams.filter(res='%s'%list[resolution-1]).first()
        download_movie.download(output_path='./', filename='%s.mp4' % self.name)


