class Historico:
    def __init__(self):
        self._operacoes = []


    def adicionar(self, operacao):
        self._operacoes.append(operacao)


    def listar(self):
        for op in self._operacoes:
            print(op)