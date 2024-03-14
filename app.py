import os

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
          ''')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair/n')
    
def escolher_opcao(mensagem):
    try:
        opcao_escolhida = int(input(mensagem))
        match opcao_escolhida:
            case 1:
                print('Adicionar restaurante')
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_programa()
            case _:
                opcao_invalida(mensagem_opcao_invalida)
    except:
                opcao_invalida(mensagem_opcao_invalida)

def finalizar_programa():
    os.system('clear')
    print('Finalizando app\n') 

mensagem_escolha_uma_opcao = 'Escolha uma opção: '
mensagem_opcao_invalida = 'Opção inválida. Digite outra opção disponível: '

def opcao_invalida(mensagem):
    escolher_opcao(mensagem)


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao(mensagem_escolha_uma_opcao)



if __name__ == '__main__':
    main()


