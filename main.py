from Download import download #Classe contendo a implementação da biblioteca PyTube
from pytube.exceptions import RegexMatchError
#import getpass               #Captura o usuário logado

print ("#### Script para download de vídeos ou músicas do YouTube ####")
print ("####        Autor: Walber Felyppi Santos Sousa            ####")
print ("####            E-mail: felyppiss@gmail.com               #### \n\n")

while(True): #Mantém o programa rodando indefinidamente
    try:
        opcao = input("Seleciona uma das opções a seguir:\n1: Vídeo   2: Playlist vídeo   3: Áudio   4: Playlist áudio\n")
        link  = input("Insira o link do video ou playlist: \n")

        #usuario = getpass.getuser()
        #local   = "C:/Users/" + usuario + "/Desktop"
 
        if  (opcao == '1'):
            download().video    (link)

        elif (opcao == '2'):
            download().pl_video (link)

        elif (opcao == '3'):
            download().audio    (link)

        elif (opcao == '4'):
            download().pl_audio (link)

    except RegexMatchError:
        print ("\nInforme o link correto!\n\n")
        pass
    
    except KeyboardInterrupt:
        print ('\nProcesso reiniciado!\n\n')
        pass
    
    except BaseException as err:
        print ('\nErro interno em main.py!', err, '\n\n')
        pass
