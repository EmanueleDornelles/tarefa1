#exercício 5 
def menu(): 
  print("Cadastro de clientes")
  print("0 - Fim")
  print("1 - Inclui")
  print("2 - Altera")
  print("3 - Exclui")
  print("4 - Consulta")

menu()
escolha = input("Escolha a operação que deseja realizar: ")

if escolha == '0':
  print("Operação fechada")
elif escolha == '1':
  print("Cliente incluído")
elif escolha == '2':
  print("Alteração feita")
elif escolha == '3':
  print("Cliente excluído")
elif escolha == '4':
  print("Consulta realizada")
else:
  print("Informe um número válido!!")
