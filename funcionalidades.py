#Função para mostrar a descrição e o menu:
def cabeçalho():
    print(
    '''
          LISTA DINÂMICA
    =================================================
                       \033[1;34mList.sys\033[m
    =================================================
    \033[1;33m                    MENU
    1 - Adicionar item;
    2 - Remover item(s);
    3 - Mostrar item(s);
    4 - Encerrar o programa.\033[m ''')


lista_de_compras = []
#Função para Adicionar itens à lista: 
def adicionar_item():
    global elemento
    try:
        elemento = str(input("Qual elemento deseja adicionar? ")).upper()
        lista_de_compras.append(elemento)
        print(f'O item {elemento} adicionado à lista com \033[1;32mSUCESSO\033[m.')
    except:
        print('Item \033[1;31mINVÁLIDO\033[m, tente novamente.')


#Função para remover itens da lista:
def remover_item():
    remover = elemento
    try:
        remover = str(input('Qual item você deseja remover da lista? '))
        lista_de_compras[:].remove(remover)
    except:
        if elemento not in lista_de_compras[:]:
            print('item não encontrado')
        else:
            print('o item não foi removido, tente novamente.')
