from contas.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        limite = 1000  # Regra diferente do comum.
        if valor <= self._saldo and valor <= limite:
            self._saldo -= valor
            self._historico.append(f"Saque: {valor}.")
        else:
            print("Saque não permitido.")