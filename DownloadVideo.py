import pytube
from pytube            import YouTube, Playlist
from pytube.exceptions import *


class video:    
    def __init__(self):
        return

    # Baixa vídeo
    def download_single(self, link, local):
        video = YouTube(link)
        video.streams.first().download(local)
        
        return print("Download concluído com sucesso!\n\n\n")
        
        
    # Baixa como áudio
    def download_single_audio(self, link, local):
        video = YouTube(link)
        video.streams.filter(only_audio = True).first().download(local)

        return print("Download concluído com sucesso!\n\n\n")
        
        
    # Baixa playlist de vídeos
    def download_mult(self, link, local):
        playlist = Playlist(link)
        try:
            for video in playlist.videos:
                video.streams.first().download(local)
        except BaseException:
            print ('A playlist contém algum vídeo indisponível, a mesma não pôde ser baixada!')
            pass

        return print("Download concluído com sucesso!\n\n\n")
        
        
    # Baixa playlist de áudio
    def download_mult_audio(self, link, local):
        playlist = Playlist(link)
        try:
            for video in playlist.videos:
                video.streams.filter(only_audio = True).first().download(local)
        except BaseException:
            print ('A playlist contém algum vídeo indisponível, a mesma não pôde ser baixada!')
            pass

        return print("Download concluído com sucesso!\n\n\n")


