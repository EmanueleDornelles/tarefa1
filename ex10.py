#exercício 10
import datetime
ano=int(input("Qual o ano do seu nascimento? "))
mes= int(input("Insira o número do mês em que você nasceu: "))
dia=int(input("Qual o dia em que você nasceu? "))
dDN = datetime.date(ano,mes,dia)
hoje=datetime.datetime.now().date()
idade=int((hoje-dDN).days/365.25)
if idade<18: 
 print("Você não poderá votar este ano!")
else: 
  print("Você poderá votar!")