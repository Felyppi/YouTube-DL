from pytube  import YouTube, Playlist
from getpass import getuser
#from pytube.exceptions import *



class download:
    #desktop   = "C:/Users/" + getuser() + "/Desktop"
    desktop   = "Download"
    conclusao = "Arquivo salvo na pasta Download! \n\n"
    excecao   = "Existe algum vídeo indisponível, o mesmo não pôde ser baixado! \nContinuando o processo, aguarde...\n"
                

    
    def __init__(self):
        return

    
    # Baixa vídeo
    def video(self, link):
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(self.desktop)
        return print (self.conclusao)
    


    # Baixa playlist de vídeos
    def pl_video(self, link):
        pl = Playlist(link)
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
        audio.streams.filter(only_audio = True).filter(file_extension = "mp4").first().download(self.desktop)
        return print (self.conclusao)
            
        

    # Baixa playlist de áudio
    def pl_audio(self, link):
        playlist = Playlist(link)
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
