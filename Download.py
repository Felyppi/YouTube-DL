from pytube import YouTube, Playlist, exceptions


class download:    
    def __init__(self):
        return



    # Baixa vídeo
    def video(self, link, local):
        video = YouTube(link)
        video.streams.first().download(local)

        return print("Download concluído com sucesso!\n\n\n")




        
    # Baixa como áudio
    def audio(self, link, local):
        video = YouTube(link)
        video.streams.filter(only_audio = True).first().download(local)

        return print("Download concluído com sucesso!\n\n\n")

        


        
        
    # Baixa playlist de vídeos
    def pl_video(self, link, local):
        playlist = Playlist(link)
        for video in playlist.videos:
            video.streams.first().download(local)

        return print("Download concluído com sucesso!\n\n\n")
                
        



        
    # Baixa playlist de áudio
    def pl_audio(self, link, local):
        playlist = Playlist(link)
        for video in playlist.videos:
            video.streams.filter(only_audio = True).first().download(local)

        return print("Download concluído com sucesso!\n\n\n")
        
## FIM DA APLICAÇÃO ##
