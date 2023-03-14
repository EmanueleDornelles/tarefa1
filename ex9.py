#exercício 9 
a1 = int (input("Informe o valor inicial: "))
n = int(input("Informe o número de termos: "))
q = int(input("Informe a razão: "))

if q < 2: 
  print("Não é possível calcular com um número menor que 2!")
else:
 sn = (a1*(q**n -1)) / (q-1)
 print(sn)