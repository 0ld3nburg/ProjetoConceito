#Entrada de dados

aluno = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

#Estrutura If para verificar o conceito de acordo com a nota
if nota < 3:
    print(f"O aluno tirou {nota} e se enquadra no conceito E")
elif (nota >= 3) and (nota < 5):
    print(f"O aluno tirou {nota} e se enquadra no conceito D")
elif (nota >= 5) and (nota < 7):
    print(f"O aluno tirou {nota} e se enquadra no conceito C")
elif (nota >= 7) and (nota < 9):
    print(f"O aluno tirou {nota} e se enquadra no conceito B")
else: 
    print(f"O aluno tirou {nota} e se enquadra no conceito A")

# Estrutura While para verificar se o usuário deseja continuar

maisDados = input("Deseja inserir mais dados? s/sim n/não ")
while maisDados != "s" and maisDados != "n":
    maisDados = input("Resposta incorreta, tente novamente. Deseja inserir mais dados? s/sim n/não ")

# Estrutura While para continuar

while maisDados == "s":
    aluno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    if nota < 3:
        print(f"O aluno tirou {nota} e se enquadra no conceito E")
    elif (nota >= 3) and (nota < 5):
        print(f"O aluno tirou {nota} e se enquadra no conceito D")
    elif (nota >= 5) and (nota < 7):
        print(f"O aluno tirou {nota} e se enquadra no conceito C")
    elif (nota >= 7) and (nota < 9):
        print(f"O aluno tirou {nota} e se enquadra no conceito B")
    else:
        print(f"O aluno tirou {nota} e se enquadra no conceito A")

    maisDados = input("Deseja inserir mais dados? s/sim n/não ")
    while maisDados != "s" and maisDados != "n":
        maisDados = input("Resposta incorreta, tente novamente. Deseja inserir mais dados? s/sim n/não ")

#Quit para finalizar o código caso a resposta seja "n"
quit()
