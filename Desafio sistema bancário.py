menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe um valor para Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f} reais\n"

        else:
            print("Valor para Depósito inválido. Por favor, informe um valor válido.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor para Saque: "))

        if numero_saques >=3:
            print("Limite de Saques Atingido. (3 Saques diários)")

        elif valor > 500:
            print("Valor de Saque acima do permitido (Até 500,00 reais)")    

        elif valor <= saldo:
            saldo -= valor
            extrato += f"Saque de: R$ {valor:.2f} reais\n"
            numero_saques += 1
            print (f"Valor sacado: R$ {valor:.2f} reais")

        else:
            print("Saldo insuficiente para realizar este Saque.")

    elif opcao == "e":
        print("------EXTRATO DETALHADO------")
        print(extrato)
        print("-----------------------------")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
