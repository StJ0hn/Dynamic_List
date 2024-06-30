from funcionalidades import *


emoji_sorridente = "\U0001F600"

while True:
    cabeçalho()
    try:
        ação = int(input("\033[1;37mO que você deseja fazer?\033[m "))
        if ação	== 1:
            adicionar_item()
            print(lista_de_compras)
        elif ação == 2:
            remover_item()
            print(lista_de_compras)
        elif ação == 4:
            print(f"Obrigado por usar o \033[1;34mList.sys\033[m, volte sempre!! {emoji_sorridente}")
            break
        else:
            print("Tente novamente.")
    except:
        print("Entrada inválida, tente novamente.")
