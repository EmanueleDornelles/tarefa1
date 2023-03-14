#exercício 12
altura = float(input("Informe a altura: "))
def menu(): 
  print("Cadastro")
  print("1 - Feminino")
  print("2 - Masculino")
menu()
escolha = input("Escolha a operação que deseja realizar: ")
if escolha == '1':
  pesoI = (62.1*altura)-44.7
  print("O seu peso ideal é:",pesoI)
elif escolha == '2':
  pesoI = (72.7*altura)-58
  print("O seu peso ideal é:",pesoI)
else: 
  print("Informe uma opção válida")