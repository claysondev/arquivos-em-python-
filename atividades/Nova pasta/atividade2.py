import math


print("="*30)
print("BEM VINDO AO MENU PRINCIPAL")
print("="*30)


opcao = int(input("1- fatorial\n2- raiz\n3- potencia\n""Digite a opção desejada: "))

if opcao == 1:
    numero = int(input("Digite um número para calcular o fatorial: "))
    resultado = math.factorial(numero)
    print(f"O fatorial de {numero} é: {resultado:.2f}")

elif opcao == 2:
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    resultado = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {resultado:.2f}")
    
elif opcao == 3:
    base = float(input("Digite a base: "))
    numero = float(input("Digite o numero: "))
    resultado = math.pow(base, numero)
    print(f"{base} elevado a {numero} é: {resultado:.2f}")
    
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

