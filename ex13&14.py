#exercício 13 e 14
lados = int(input("Informe o número de lados do polígono: "))
if lados == 3: 
  print("O polígono é um triângulo!")
elif lados == 4:
  print("O polígono é um quadrado!")
elif lados == 5:
  print("O polígono é um pentágono!")
elif lados >5:
  print("Não foi possível identificar o polígono!")
elif lados <3:
  print("Não é um polígono!")