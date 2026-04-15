from datetime import time

class atendimento:
    def __init__(self, nome_aluno, tipo_atendimento,data_hora):
        self.nome_cliente = nome_aluno
        self.tipo_atendimento = tipo_atendimento
        self.data_hora = data_hora

    def registrar_atendimento(self):
        print(f"Atendimento registrado para {self.nome_cliente} às {self.data_hora.strftime('%H:%M')} - Tipo: {self.tipo_atendimento}")
        
nome_aluno = input("Digite o nome do aluno: ")
tipo_atendimento = input("Digite o tipo de atendimento: ")
data_hora = time(10, 30)
atendimento1 = atendimento(nome_aluno, tipo_atendimento, data_hora)
atendimento1.registrar_atendimento()

