# Dados dos serviços
servicos = [
    [1, "Lavagem Simples", 30],
    [2, "Lavagem Completa", 50],
    [3, "Enceramento", 80],
    [4, "Higienização Interna", 100]
]

# Lista de atendimentos
atendimentos = []

# Função para registrar atendimento
def registrar():
    placa = input("Placa: ")
    tipo = input("Tipo (Carro/Moto): ")

    print("\nServiços:")
    for s in servicos:
        print(s[0], "-", s[1], "- R$", s[2])

    cod = int(input("Código do serviço: "))

    # validação simples
    valido = False
    for s in servicos:
        if s[0] == cod:
            valor = s[2]
            valido = True

    if valido:
        atendimentos.append([placa, tipo, cod, valor])
        print("OK!\n")
    else:
        print("Código inválido!\n")


# Listar atendimentos
def listar():
    for a in atendimentos:
        for s in servicos:
            if s[0] == a[2]:
                nome = s[1]
        print(a[0], "-", a[1], "-", nome, "- R$", a[3])
    print()


# Total arrecadado
def total():
    soma = 0
    for a in atendimentos:
        soma += a[3]
    print("Total: R$", soma, "\n")


# Quantidade de serviços
def quantidade():
    cont = [0, 0, 0, 0]

    for a in atendimentos:
        cont[a[2] - 1] += 1

    for i in range(4):
        print(servicos[i][1], ":", cont[i])
    print()


# Menu
while True:
    print("1-Registrar 2-Listar 3-Total 4-Quantidade 5-Sair")
    op = input("Opção: ")

    if op == "1":
        registrar()
    elif op == "2":
        listar()
    elif op == "3":
        total()
    elif op == "4":
        quantidade()
    elif op == "5":
        break
    else:
        print("Erro!\n")