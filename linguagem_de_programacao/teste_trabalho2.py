print('Bem vindo ao Software Gerenciador de Tarefas!')
def main():
    while True:
        try:
            choose = int(input('Funcionalidades:\n[1] - Adicionar tarefa;\n[2] - Listar tarefas;\n[3] - Visualizar tarefa;\n[4] - Marcar uma tarefa como concluída;\n[5] - Marcar uma tarefa como pendente.\nDigite o número da funcionalidade desejada: '))
        except ValueError:
            print('Por favor, digite um número!')
        else:
            if choose == 1: ad_tarefa()
            elif choose == 2: lis_tarefa()
            elif choose == 3: visu_tarefa()
            elif choose == 4: con_tarefa()
            elif choose == 5: pen_tarefa()
            break


dados = [[],[],[]]

def ad_tarefa():
   dados[0].append(input('Digite o título da tarefa: '))
   dados[1].append(input('Digite a descrição da tarefa: '))
   dados[2].append('Pendente')
print('Tarefa adicionada com sucesso!')

def lis_tarefa():
    for i in range(len(dados[0])):
        print(f'Título: {dados[0][i]}\nDescrição: {dados[1][i]}')

def visu_tarefa():
    for i,p in enumerate(len(dados[0])):
        print(f'Título: {dados[0][i]}\nDescrição: {dados[1][i]}')
    question = int(input('Qual a tarefa que deseja visualizar?'))
    for i in range(len(dados)):
        print(f'{dados[question][i]},{dados[question+1][i]}')

def con_tarefa():
    try:
        question = int(input('Qual a tarefa que deseja marcar como concluída?'))
    except ValueError:
        print('Por favor, digite um número!')
    

def pen_tarefa():
    question = int(input('Qual a tarefa que deseja marcar como pendente?'))

main()
while True:
    res = input('Deseja continuar utilizando o Gerenciador?')
    if res == 's': main()
    else: print('Obrigado por utilizar nosso Software!') 
    break