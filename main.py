from DownloadVideo import video # Classe contendo a implementação da biblioteca PyTube
import getpass                  # Captura o usuário logado


while(True): # Mantém o programa rodando indefinidamente
    
    opcao = str(input("1: Vídeo   2: Playlist vídeo   3: Áudio   4: Playlist áudio \n"))
    link  = str(input("Insira o link do video ou playlist: \n"))

    usuario = getpass.getuser()
    local   = "C:/Users/" + usuario + "/Desktop"
    

    if   (opcao == '1'):
        video().download_single       (link, local)

    elif (opcao == '2'):
        video().download_mult         (link, local)

    elif (opcao == '3'):
        video().download_single_audio (link, local)

    elif (opcao == '4'):
        video().download_mult_audio   (link, local)
