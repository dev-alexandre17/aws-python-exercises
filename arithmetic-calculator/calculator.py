import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    
    program = True
    
    while program:
        print(f'=== CALCULADORA ===\n')

        print(f'=== MENU ===\n')
        print(f'1. Adição')
        print(f'2. Subtração')
        print(f'3. Multiplicação')
        print(f'4. Divisão\n')

        opc = str(input('Escolha uma opção: '))
        
        if opc not in ['1', '2', '3', '4']:
            limpar_tela()
            print(f'Erro: Opção inválida. Por favor, escolha uma opção válida.\n')      
        else:
            try:
                num1 = float(input(f'Digite o primeiro número: '))
                num2 = float(input(f'Digite o segundo número: '))
            except ValueError:
                limpar_tela()
                print(f'Erro: Digite apenas números válidos.\n')
                continue
            match opc:
                case '1':
                    resultado = num1 + num2
                    print(f'Resultado da adição: {resultado}\n')
                case '2':
                    resultado = num1 - num2
                    print(f'Resultado da subtração: {resultado}\n')
                case '3':
                    resultado = num1 * num2
                    print(f'Resultado da multiplicação: {resultado}\n')
                case '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f'Resultado da divisão: {resultado}\n')
                    else:
                        print(f'Erro: Divisão por zero não é permitida.\n')
                case _:
                    print(f'\nOpção inválida. Por favor, escolha uma opção válida.\n')
                    
            control = input(f'Deseja realizar outra operação? (s/n): ')
            limpar_tela()
            
            if control.lower() != 's':
                program = False
                print(f'Encerrando a calculadora. Até logo!\n')
            
main()


