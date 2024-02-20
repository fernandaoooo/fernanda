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
   print('Função [Adicionar tarefa] selecionada.')
   dados[0].append(input('Digite o título da tarefa: '))
   dados[1].append(input('Digite a descrição da tarefa: '))
   dados[2].append('Pendente')
   for i in range(len(dados)):
    print (f'Nova tarefa adicionada: {dados[0]}\nDescrição: {dados[1]}\nStatus: {dados[2]}')

def lis_tarefa():
    print('Função [Listar tarefas] selecionada.')
    print(f'{dados[0]},{dados[1]}')

def visu_tarefa():
    print('Função [Visualizar tarefa] selecionada.')


def con_tarefa():
    print('Função [Marcar tarefa como concluída] selecionada.')
    question = int(input('Qual a tarefa que deseja marcar como concluída?'))
    


def pen_tarefa():
    print('Função [Marcar uma tarefa como pendente] selecionada.')


main()
while True:
    res = input('Deseja continuar utilizando o Gerenciador?')
    if res == 's': main()
    else: break