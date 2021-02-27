from pytube            import YouTube, Playlist
from pytube.exceptions import *


class download:    
    def __init__(self):
        return

    

    # Baixa vídeo
    def video(self, link):
        video = YouTube(link)
        video.streams.first().download('Download')
        return print ("Arquivo salvo em Download! \n\n\n")
        



    # Baixa playlist de vídeos
    def pl_video(self, link):
        playlist = Playlist(link)
        for url in playlist.video_urls:
            try:
                video = YouTube(url)
            except (Exception):
                print ('Existe algum vídeo indisponível, o mesmo não pôde ser baixado! \n')
                print ('Continuando o processo, aguarde...\n')
                pass
            else:
                video.streams.first().download('Download')
        return print ("Arquivo salvo em Download! \n\n\n")
        



        
    # Baixa como áudio
    def audio(self, link):
        video = YouTube(link)
        video.streams.filter(only_audio = True).first().download('Download')
        return print ("Arquivo salvo em Download! \n\n\n")
            
        

        


        
               
    # Baixa playlist de áudio
    def pl_audio(self, link):
        playlist = Playlist(link)
        for url in playlist.video_urls:
            try:
                audio = YouTube(url)
            except Exception:
                print ('Existe algum link indisponível, o mesmo não pôde ser baixado! \n')
                print ('Continuando o processo, aguarde...\n')
                pass
            else:
                audio.streams.filter(only_audio = True).first().download('Download')
        return print ("àudios salvos em Download! \n\n\n")
        
## FIM DA APLICAÇÃO ##
