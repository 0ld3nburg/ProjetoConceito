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
