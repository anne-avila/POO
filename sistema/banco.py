from contas.conta_poupanca import ContaPoupanca
from contas.conta_corrente import ContaCorrente

class Banco:
    def __init__(self):
        self._contas = []


    def criar_conta(self, cliente, tipo):
        numero = len(self._contas) + 1

        if tipo == "cc":
            conta = ContaCorrente(cliente, numero)
        elif tipo == "cp":
            conta = ContaPoupanca(cliente, numero)
        else:
            print("Tipo de conta inválido.")
            return None


        self._contas.append(conta)
        return conta


    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta.get_numero() == numero:
                return conta
        return None


    def listar_contas(self):
        return self._contas