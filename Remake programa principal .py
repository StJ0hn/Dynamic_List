from funcionalidades import *


emoji_sorridente = "\U0001F600"

while True:
    cabeçalho()
    try:
        ação = int(input("\033[1;32mO que você deseja fazer agora?\033[m "))
        if ação	== 1:
            Fazer_pergunta()
        elif ação == 2:
            responder_perguntas()
        elif ação == 3:
            mostrar_respostas()
        elif ação == 4:
            print(f"Obrigado por usar o \033[1;34mQuest.Onion\033[m, volte sempre!! {emoji_sorridente}")
            break
        else:
            print("Tente novamente.")
    except:
        print("Entrada inválida, tente novamente.")