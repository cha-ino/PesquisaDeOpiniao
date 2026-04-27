qtd_excelente = 0
qtd_ruim = 0

while True:
    try:
        qtd_clientes = int(input("Digite 10 para teste ou 50 para pesquisa completa: "))
        if qtd_clientes in [10, 50]:
            break
        else:
            print("Opção inválida! Digite apenas 10 ou 50.")
    except ValueError:
        print("Entrada inválida! Digite apenas números (10 ou 50).")

for i in range(1, qtd_clientes + 1):
    print(f"Cliente {i}")
    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Valor inválido! Utilize apenas números para a idade.")

    while True:
        print("Opinião sobre o atendimento:")
        print("(1) - EXCELENTE")
        print("(2) - BOM")
        print("(3) - RUIM")
        try:
            opiniao = int(input("Qual sua opinião ao atendimento? (1/2/3): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Opção inválida! Digite apenas 1, 2 ou 3.")
        except ValueError:
            print("Valor inválido! Utilize apenas números das opções válidas (1, 2 ou 3).")

    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1

print("RESULTADOS DA PESQUISA")
print(f"Quantidade de opiniões EXCELENTE: {qtd_excelente}")
print(f"Quantidade de opiniões RUIM: {qtd_ruim}")