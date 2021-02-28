from pytube            import YouTube, Playlist
#from pytube.exceptions import *


class download:
    pasta      = "Download"
    conclusao  = "Arquivo salvo na pasta Download! \n\n"
    exception  = "Existe algum vídeo indisponível, o mesmo não pôde ser baixado! \nContinuando o processo, aguarde...\n"
    regexmatch = "Link digitado incorreto"
                


    
    def __init__(self):
        return

    
    # Baixa vídeo
    def video(self, link):
        yt = YouTube(link)
        yt.streams.first().download(self.pasta)
        return print (self.conclusao)
    


    # Baixa playlist de vídeos
    def pl_video(self, link):
        playlist = Playlist(link)
        for url in playlist.video_urls:
            try:
                video = YouTube(url)
            except Exception:
                print (self.excecao)
            else:
                video.streams.first().download(self.pasta)
        return print (self.conclusao)
        

        
    # Baixa como áudio
    def audio(self, link):
        video = YouTube(link)
        video.streams.filter(only_audio = True).first().download(self.pasta)
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
                audio.streams.filter(only_audio = True).first().download(self.pasta)
        return print (self.conclusao)
        
## FIM DA APLICAÇÃO ##
