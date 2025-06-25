"""
Aplicando em um unico sistema
* Cadastro
* Contas
* Verificação das Contas
"""

nomes = []
senhas = []

def cadastrar_nomes():
  print("=========CADASTRO==========")
  nome = input("Digite um nome: ")
  nomes.append(nome)
  senha = input("Digite uma senha: ")
  senhas.append(senha)
  print("Usuário cadastrado com sucesso!")
  return nomes, senhas

import random

nomes = []
senhas = []

def cadastrar_nomes():
    print("=========CADASTRO==========")
    nome = input("Digite um nome: ")
    nomes.append(nome)
    senha = input("Digite uma senha: ")
    senhas.append(senha)
    print("Usuário cadastrado com sucesso!")
    return nomes, senhas

def verificar_resposta(resposta, resultado_correto, operacao):
    if operacao == "4":  # divisão - aceitar pequeno erro por conta das casas decimais
        if abs(resposta - resultado_correto) < 0.01:
            print("✅ Parabéns, você acertou!")
        else:
            print(f"❌ Errou! O resultado correto era {resultado_correto:.2f}")
    else:
        if resposta == resultado_correto:
            print("✅ Parabéns, você acertou!")
        else:
            print(f"❌ Errou! O resultado correto era {resultado_correto}")

def contas_automaticas():
    print("=========CONTAS==========")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Digite o número da operação desejada: ")

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print(f"Números sorteados: {num1} e {num2}")

    if opcao == "1":
        resultado_correto = num1 + num2
        resposta = float(input("Qual o resultado da soma? "))
    elif opcao == "2":
        resultado_correto = num1 - num2
        resposta = float(input("Qual o resultado da subtração? "))
    elif opcao == "3":
        resultado_correto = num1 * num2
        resposta = float(input("Qual o resultado da multiplicação? "))
    elif opcao == "4":
        while num2 == 0:
            num2 = random.randint(1, 100)
        resultado_correto = num1 / num2
        resposta = float(input("Qual o resultado da divisão? (até 2 casas decimais) "))
    else:
        print("Opção inválida!")
        return

    verificar_resposta(resposta, resultado_correto, opcao)


while True:
    print("=========MENU==========")
    print("1. Cadastrar usuário")
    print("2. Contas automáticas")
    print("3. Sair")
    opiciones = int(input("Escolha uma opção: "))

    if opiciones == 1:
        cadastrar_nomes()
    elif opiciones == 2:
        contas_automaticas()
    elif opiciones == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")
