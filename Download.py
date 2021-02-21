from pytube            import YouTube, Playlist
from pytube.exceptions import RegexMatchError, VideoUnavailable


class download:    
    def __init__(self):
        return

    

    # Baixa vídeo
    def video(self, link):
        try:
            video = YouTube(link)
            video.streams.first().download('Download')
            return print ("Arquivo salvo em Download! \n\n\n")
        
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
    def pl_video(self, link):
        try:
            playlist = Playlist(link)
            for video in playlist.videos:
                video.streams.first().download('Download')
            return print ("Arquivo salvo em Download! \n\n\n")
        
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
    def audio(self, link):
        try:
            video = YouTube(link)
            video.streams.filter(only_audio = True).first().download('Download')
            return print ("Arquivo salvo em Download! \n\n\n")
            
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
    def pl_audio(self, link):
        try:
            playlist = Playlist(link)
            for video in playlist.videos:
                video.streams.filter(only_audio = True).first().download('Download')
            return print ("Arquivo salvo em Download! \n\n\n")
        
        except VideoUnavailable:
            print ('Existe algum vídeo indisponível, o mesmo não foi baixado! \n')
            pass
        
        except BaseException:
            print('Algum erro desconhecido! \n')
            pass
        
## FIM DA APLICAÇÃO ##
