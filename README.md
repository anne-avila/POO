# Sistema de Caixa Eletrônico (ATM) em Python

## Descrição

Este projeto consiste na implementação de um sistema de caixa eletrônico (ATM) utilizando Programação Orientada a Objetos (POO) em Python. O sistema simula operações bancárias básicas, permitindo a criação e gerenciamento de contas, além de operações financeiras como depósito e saque.

---

## Funcionalidades

* Criar conta (corrente ou poupança)
* Depositar dinheiro
* Sacar dinheiro
* Consultar saldo
* Visualizar histórico de operações

---

## Conceitos de POO Utilizados

### Pacotes

O sistema foi organizado em pacotes para melhor estruturação:

* `contas`
* `clientes`
* `operacoes`

---

### Classes e Objetos

Foram implementadas classes como:

* `Conta`
* `ContaCorrente`
* `ContaPoupanca`
* `Cliente`
* `Banco`

---

### Herança

As classes `ContaCorrente` e `ContaPoupanca` herdam da classe base `Conta`.

---

### Polimorfismo

O método `sacar()` possui comportamentos diferentes dependendo do tipo de conta.

---

### Agregação

A classe `Banco` é responsável por gerenciar múltiplas contas.

---

### Composição

Cada conta possui um histórico de operações, que só existe em função da conta.

---

### Encapsulamento

Atributos foram definidos como privados e acessados por métodos apropriados.

---

## Como Executar

1. Clone o repositório:

```bash
git clone <link-do-repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd sistema
```

3. Execute o programa:

```bash
python main.py
```

---

## Exemplo de Uso

```
1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Saldo
5 - Histórico
0 - Sair
```

---

## Regras de Negócio

* Não é permitido sacar valores maiores que o saldo
* Todas as operações são registradas no histórico
* O sistema valida entradas do usuário
* Mensagens de erro são exibidas para operações inválidas

---

## Estrutura do Projeto

```
sistema/
│
├── contas/
├── clientes/
├── operacoes/
├── banco.py
├── main.py
└── README.md
```

---

## Autor

Anne Ávila
---

## Data

Abril de 2026
