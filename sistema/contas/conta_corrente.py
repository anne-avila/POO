from contas.conta import Conta

class ContaCorrente(Conta):
    def sacar(self, valor):
        if valor <= self._saldo:  # Regra padrão.
            self._saldo -= valor
            self._historico.append(f"Saque: {valor}.")
        else:
            print("Saldo insuficiente.")