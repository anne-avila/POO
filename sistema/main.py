from banco import Banco
from clientes.cliente import Cliente

banco = Banco()

while True:
    print("\n1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Saldo")
    print("5 - Histórico")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        tipo = input("Tipo (cc/cp): ").strip().lower()

        cliente = Cliente(nome)
        conta = banco.criar_conta(cliente, tipo)

        if conta:
            print(f"Conta criada! Número: {conta.get_numero()}")

    elif op == "2":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)

        if conta:
            valor = float(input("Valor: "))
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    elif op == "3":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)

        if conta:
            valor = float(input("Valor: "))
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

    elif op == "4":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)

        if conta:
            print("Saldo:", conta.get_saldo())
        else:
            print("Conta não encontrada.")

    elif op == "5":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)

        if conta:
            print(conta.get_historico())
        else:
            print("Conta não encontrada.")

    elif op == "0":
        break

    else:
        print("Opção inválida")