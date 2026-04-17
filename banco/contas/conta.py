class Conta:  # Classe Base para as contas.
    def __init__(self, cliente, numero)  # Init básico da classe base.
        self._cliente = cliente
        self._numero = numero
        self._saldo = 0
        self._historico = []


    def depositar(self, valor):  # Método de depósito padrão de todas as contas.
        if valor > 0:
            self._saldo += valor
            self._historico.append(f"Depósito: {valor}.")
        else:
            print("Valor inválido.")

    
    def sacar(self, valor):  # Classe base diz que deve haver esse método, mas cada tipo de conta é diferente.
        raise NotImprementedError

    
    def get_saldo(self):  # Getter do Saldo.
        return self._saldo

    
    def get_historico(self):  # Getter do Historico.
        return self._historico