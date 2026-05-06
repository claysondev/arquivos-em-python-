#esse codigo pega o primeiro e o ultimo estado da lista.

estados = ["sao paulo","rio de janeiro","amazonas", "espirito santos"]

print("---o primeiro estado é---\n", estados[0])
print("---o ultimo estado é---\n", estados[-1])
print("\n")

#fim





#esse codigo pega a maior nota e a menor nota.

notas = [5.0 , 7.0 , 9.0]

print("=== a maior nota é ===\n", min(notas))
print("=== a maior nota é ===\n",max(notas))
print("\n")

#fim


#esse codigo lista todos os produtos da lista dentro da lista.
produtos =  ["mouse, teclado, monitor,computador"]

for produto in produtos:
    print(produtos)
    
print("\n")
#fim


#se numero for maior que 5 nao existe linha, apenas inferior a 5.
numero = int(input("Digite um número: "))

    
if 1 <= numero <= 5:
        print("A linha existe!")
else:
        print("Linha inválida")



















