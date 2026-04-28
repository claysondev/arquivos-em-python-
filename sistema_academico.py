# Sistema Acadêmico Simplificado

nomes = []
matriculas = []
notas1 = []
notas2 = []
notas3 = []
medias = []
situacoes = []

limite = 30
semestre_fechado = False 


def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def definir_situacao(media):
    if media >= 7:
        return "aprovado"
    elif media >= 5:
        return "recuperação"
    else:
        return "reprovado"


while True:
    print("\n---- MENU ----")
    print("1. cadastrar aluno")
    print("2. lançar/alterar notas")
    print("3. listar alunos")
    print("4. relatórios")
    print("5. buscar aluno")
    print("6. fechar semestre")
    print("0. sair")

    opcao = input("escolha: ")

    # sair
    if opcao == "0":
        confirmar = input("deseja sair? (s/n): ")
        if confirmar.lower() == "s":
            break

    # cadastrar
    elif opcao == "1":
        if len(nomes) >= limite:
            print("limite de alunos atingido!")
            continue

        nome = input("nome: ")

        if nome in nomes:
            print("nome já cadastrado!")
            continue

        matricula = input("matrícula: ")

        if matricula in matriculas:
            print("matrícula já existe!")
            continue

        nomes.append(nome)
        matriculas.append(matricula)
        notas1.append(0)
        notas2.append(0)
        notas3.append(0)
        medias.append(0)
        situacoes.append("sem nota")

        print("aluno cadastrado!")

    # notas
    elif opcao == "2":
        if semestre_fechado:
            print("semestre fechado! não pode alterar notas.")
            continue

        mat = input("digite a matrícula: ")

        if mat in matriculas:
            i = matriculas.index(mat)

            try:
                n1 = float(input("nota 1: "))
                n2 = float(input("nota 2: "))
                n3 = float(input("nota 3: "))

                if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10:
                    notas1[i] = n1
                    notas2[i] = n2
                    notas3[i] = n3

                    media = calcular_media(n1, n2, n3)
                    medias[i] = media
                    situacoes[i] = definir_situacao(media)

                    print("notas atualizadas!")
                else:
                    print("notas inválidas!")
            except:
                print("erro ao digitar notas!")
        else:
            print("aluno não encontrado!")

    # listar
    elif opcao == "3":
        if len(nomes) == 0:
            print("nenhum aluno cadastrado.")
        else:
            print("\nmatrícula | nome | média | situação")
            for i in range(len(nomes)):
                print(matriculas[i], "|", nomes[i], "|", round(medias[i], 2), "|", situacoes[i])

    # relatórios
    elif opcao == "4":
        if len(medias) == 0:
            print("sem dados.")
        else:
            maior = max(medias)
            menor = min(medias)
            media_geral = sum(medias) / len(medias)

            aprovados = situacoes.count("aprovado")
            percentual = (aprovados / len(situacoes)) * 100

            print("média geral:", round(media_geral, 2))
            print("maior média:", maior)
            print("menor média:", menor)
            print("percentual aprovação:", round(percentual, 2), "%")
            print("aprovados:", aprovados)
            print("recuperação:", situacoes.count("recuperação"))
            print("reprovados:", situacoes.count("reprovado"))
            print("diferença (maior-menor):", maior - menor)

    # buscar
    elif opcao == "5":
        busca = input("nome ou matrícula: ")

        if busca in nomes:
            i = nomes.index(busca)
        elif busca in matriculas:
            i = matriculas.index(busca)
        else:
            print("aluno não encontrado!")
            continue

        print("nome:", nomes[i])
        print("notas:", notas1[i], notas2[i], notas3[i])
        print("média:", medias[i])
        print("situação:", situacoes[i])

    # fechar semestre
    elif opcao == "6":
        confirmar = input("deseja fechar o semestre? (s/n): ")
        if confirmar.lower() == "s":
            semestre_fechado = True
            print("semestre fechado!")

    else:
        print("opção inválida!")