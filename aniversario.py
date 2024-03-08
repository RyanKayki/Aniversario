import os
import datetime

aniversariantes = []
datas = []

while True:
    os.system('cls')

    print("SISTEMA DE LOGIN E SENHA")
    print("1 - Cadastrar aniversariantes (DATA E NOME)")
    print("2 - Mostrar todos cadastros")
    print("3 - Limpar cadastros")

    while True:
        codigo = input("Insira a opção desejada: ")
        if codigo.isnumeric():
            codigo = int(codigo)
            if 1 <= codigo <= 3:
                break
        print("OPÇÃO INVÁLIDA!")

    os.system('cls')

    if codigo == 1:
        print("1 - CADASTRO:")

        usuario = input("Insira o nome do aniversariante: ")
        if usuario in aniversariantes:
            print("O Aniversariante já está cadastrado!")
        else:
            while True:
                try:
                    usuario_data = input("\n Informe a data do seu aniversário (formato DD/MM/AAAA): ")
                    dia, mes, ano = map(int, usuario_data.split("/"))
                    data_pronta = datetime.date(ano, mes, dia)
                    if data_pronta > datetime.date.today():
                        break
                    else:
                        print("\n Data inválida! Informe uma data futura.")
                except ValueError:
                    print("\n Formato de data inválido!")

            print("Aniversariante cadastrado com sucesso!")
            datas.append(data_pronta)
            aniversariantes.append(usuario)

    elif codigo == 2:
        print("\n ***Acesso ao SISTEMA*** ")
        hoje = datetime.date.today()

        if len(datas) > 0:
            for i in range(len(datas)):
                dias_restantes = datas[i] - hoje
                print(f'\n {aniversariantes[i]}, faltam {dias_restantes.days} dias para seu aniversário!')
            os.system("pause")
        else:
            print("\n Nenhum aniversário cadastrado.")
            os.system("pause")

    elif codigo == 3:
        datas = []
        aniversariantes = []
        print("\n Listas limpas com sucesso!")
        os.system('pause')
    else:
        print("OPÇÃO INVÁLIDA!")
        os.system('pause')
