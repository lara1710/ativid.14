# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:

nota1 = int(input("digite sua nota:"))
nota2 = int(input("digite sua nota:"))
nota3 = int(input("digite sua nota:"))

média = (nota1 + nota2 + nota3)/3

if média >= 7:
    print("aprovado")

elif média<= média < 7:
    print("reprovado")

if média < 5:
    print("recuperação")
    