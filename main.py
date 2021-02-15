from DownloadVideo import video # Classe contendo a implementação da biblioteca PyTube
import getpass                  # Captura o usuário logado

print ("#### Script para download de vídeos ou músicas do YouTube ####")
print ("        #### Por: Walber Felyppi Santos Sousa ####")
print ("        #### E-mail: felyppiss@gmail.com      #### \n \n")

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
