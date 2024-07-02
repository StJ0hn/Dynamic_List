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
        elemento = str(input("Qual item você deseja adicionar? ")).upper()
        lista_de_compras.append(elemento)
        print(f'O item {elemento} adicionado à lista com \033[1;32mSUCESSO\033[m.')
    except:
        print('Item \033[1;31mINVÁLIDO\033[m, tente novamente.')


#Função para remover itens da lista:
def remover_item():
    global lista_de_compras
    try:
        item_remover = str(input('Qual item você deseja remover da lista? ')).upper()
        if item_remover in lista_de_compras:
            lista_de_compras = [item for item in lista_de_compras if item != item_remover]
            print(f'O item {item_remover} foi removido da lista com \033[1;32mSUCESSO\033[m.')
        else:
            print('Item não encontrado na lista.')
    except Exception as e:
        print(f'Erro ao remover o item da lista: {str(e)}')