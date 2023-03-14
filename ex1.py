#exercício 1 
nota1= float(input("Informe a primeira nota: "))
nota2= float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
mediaEx=float(input("Qual a média de atividades? "))

media = (nota1+(nota2*2)+(nota3*3)+mediaEx)/7

if media < 4:
    print("Aluno reprovado!")
else: 
    print("Aluno aprovado!")
print (media)
