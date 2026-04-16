import csv

with open("alunos.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)
    print("Cabeçalho:", cabecalho)
    print("-" * 30)
    
    for linha in leitor:
        nome = linha[0]
        idade = linha[1]
        curso = linha[2]
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Curso: {curso}")
        print("-" * 30)