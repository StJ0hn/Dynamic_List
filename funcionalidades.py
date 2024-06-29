def cabeçalho():
    print(
    '''
          PLATAFORMA DE CRIAÇÃO DE QUESTIONÁRIOS
    =================================================
                       \033[1;34mQuest.Onion\033[m
    =================================================
    \033[1;33m                    MENU
    1 - Criar pergunta(s);
    2 - Responder pergunta(s) já cadastrada(s);
    3 - Mostrar resposta(s);
    4 - Encerrar o programa.\033[m ''')

questoes={}


lista_perguntas = []
def Fazer_pergunta(n_perguntas=None):
    try:
        if n_perguntas is None:
            while True:
                try:
                    n_perguntas = int(input("Preencha o campo com um número INTEIRO representado a quantidade de perguntas que deseja elaborar: "))
                    break
                except ValueError:
                    print('Por favor, insira um número inteiro válido')

        for i in range(n_perguntas):
            pergunta = input(f'Qual a {i+1}° pergunta que você deseja elaborar? ')
            questoes[f'{i+1}º pergunta'] = pergunta

            lista_perguntas.append(questoes)
        print("Pergunta(s) elaborada(s) com sucesso.")
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')

    return lista_perguntas  
def responder_perguntas():
    global lista_perguntas
    
    try:
        if not lista_perguntas:
            print("Não há perguntas cadastradas para responder.")
            return []

        respostas = []
        
        for i, pergunta_dict in enumerate(lista_perguntas):
            pergunta = list(pergunta_dict.values())[0]
            resposta = input(f"Responda à {i+1}ª pergunta: '{pergunta}' ")
            respostas.append(resposta)
        print("Respostas registradas com sucesso.")
    
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')

    return respostas


def mostrar_respostas(lista_perguntas, respostas):
    if not respostas:
        print("Não há respostas para mostrar.")
    else:
        print("Respostas fornecidas:")
        for i, resposta in enumerate(respostas):
            pergunta = lista_perguntas[i][0]  # Acessa diretamente a pergunta da tupla
            print(f"Resposta à '{pergunta}': {resposta}")



respostas = responder_perguntas()