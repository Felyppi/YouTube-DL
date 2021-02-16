from pytube import YouTube, Playlist
from pytube.exceptions import *

class download:    
    def __init__(self):
        return



    # Baixa vídeo
    def video(self, link, local):
        try:
            video = YouTube(link)
            video.streams.first().download(local)
            return print("Download concluído com sucesso!\n\n\n")
        except RegexMatchError:
            print ('Informe o link corretamente! \n')
            pass
        except VideoUnavailable:
            print ('Existe algum vídeo indisponível, o mesmo não foi baixado! \n')
            pass
        except BaseException:
            print('Algum erro desconhecido! \n')
            pass



        
    # Baixa como áudio
    def audio(self, link, local):
        try:
            video = YouTube(link)
            video.streams.filter(only_audio = True).first().download(local)
            return print("Download concluído com sucesso!\n\n\n")
        except RegexMatchError:
            print ('Informe o link corretamente! \n')
            pass
        except VideoUnavailable:
            print ('Existe algum vídeo indisponível, o mesmo não foi baixado! \n')
            pass
        except BaseException:
            print('Algum erro desconhecido! \n')
            pass

        


        
        
    # Baixa playlist de vídeos
    def pl_video(self, link, local):
        try:
            playlist = Playlist(link)
            for video in playlist.videos:
                video.streams.first().download(local)
            return print("Download concluído com sucesso!\n\n\n")
        except RegexMatchError:
            print ('Informe o link corretamente! \n')
            pass
        except VideoUnavailable:
            print ('Existe algum vídeo indisponível, o mesmo não foi baixado! \n')
            pass
        except BaseException:
            print('Algum erro desconhecido! \n')
            pass
                
        


        
    # Baixa playlist de áudio
    def pl_audio(self, link, local):
        try:
            playlist = Playlist(link)
            for video in playlist.videos:
                video.streams.filter(only_audio = True).first().download(local)
            return print("Download concluído com sucesso!\n\n\n")
        except VideoUnavailable:
            print ('Existe algum vídeo indisponível, o mesmo não foi baixado! \n')
            pass
        except BaseException:
            print('Algum erro desconhecido! \n')
            pass
        
## FIM DA APLICAÇÃO ##
