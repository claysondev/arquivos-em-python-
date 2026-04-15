import random

#foi criado um vetor chamado "alunos" para receber os nomes digitados
def cadastrar_alunos():
    alunos = []
    for i in range (5):
    
        nome = input (f"Digite o nome do aluno {i+1}: ")
        alunos.append(nome)
    return alunos
    
def sortear_aluno(lista):
    sorteado = random. choice(lista)
    return sorteado

lista_alunos = cadastrar_alunos()
resultado = sortear_aluno( lista_alunos)
print ("Aluno sorteado:", resultado)

