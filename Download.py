from pytube  import YouTube, Playlist
from getpass import getuser
#from pytube.exceptions import *



class download:
    desktop   = "Download" # "C:/Users/" + getuser() + "/Desktop" (utilizar com getpass)
    baixando  = "Iniciando o download...\n"
    conclusao = "Arquivo salvo na pasta {0}! \n\n" .format(desktop)
    excecao   = "Existe algum vídeo indisponível, o mesmo não pôde ser baixado! \nContinuando o processo, aguarde...\n"
                

    
    def __init__(self):
        return

    
    # Baixa vídeo
    def video(self, link):
        yt = YouTube(link)
        print (self.baixando)
        yt.streams.get_highest_resolution().download(self.desktop)
        return print (self.conclusao)
    


    # Baixa playlist de vídeos
    def pl_video(self, link):
        pl = Playlist(link)
        print (self.baixando)
        for url in pl.video_urls:
            try:
                yt = YouTube(url)
            except Exception:
                print (self.excecao)
            else:
                yt.streams.get_highest_resolution().download(self.desktop)
        return print (self.conclusao)
        

        
    # Baixa como áudio
    def audio(self, link):
        audio = YouTube(link)
        print (self.baixando)
        audio.streams.filter(only_audio = True).filter(file_extension = "mp4").first().download(self.desktop)
        return print (self.conclusao)
            
        

    # Baixa playlist de áudio
    def pl_audio(self, link):
        playlist = Playlist(link)
        print (self.baixando)
        for url in playlist.video_urls:
            try:
                audio = YouTube(url)
            except Exception:
                print (self.excecao)
                pass
            else:
                audio.streams.filter(only_audio = True).filter(file_extension = "mp4").first().download(self.desktop)
        return print (self.conclusao)
        
## FIM DA APLICAÇÃO ##
