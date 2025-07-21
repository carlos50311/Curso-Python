tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
 








































































































# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)
 
 
# print(f(3))
 






























# try:
#     valor = int(input("Digite um valor inteiro: "))
#     valor2 = int(input("Digite outro valor inteiro: "))
#     soma = valor + valor2
#     print(f"A soma dos valores é: {soma}")
# except ValueError:
#     print("Entrada inválida. Por favor, digite apenas números inteiros.")































# dicionario = {"Carlos": 1, "Roberto": 2, "Caio": 3}

# print(dicionario)

# dicionario["Caio"] = 4

# print(dicionario)

# dicionario.pop("Caio")

# print(dicionario)

# del dicionario

# print(dicionario)





























































# teste_dicionarios = {"carlos":"123456", "joice":"654321", "eduardo":"67890"}

# print(teste_dicionarios)

# trupla = (1, 3, 4)

# print(trupla[0])

# inteiro_para_adcionar = 10

# nova_trupla = trupla + (inteiro_para_adcionar,)


# print(nova_trupla)




























# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)
 
 
# print(fun(25))




































# # Implementação recursiva da função fatorial.
 
# def factorial(n):
#     if n == 1:    # O caso base (condição de rescisão).
#         return 1
#     else:
#         return n * factorial(n - 1)
 
 
# print(factorial(4)) # 4 * 3 * 2 * 1 = 24
 


















# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)
 

# factorial_function(10)













































































# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254
 
 
# def lb_to_kg(lb):
#     return lb * 0.4535923
 
 
# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None
 
#     return weight / height ** 2
 
 
# print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))






































































# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
 






















# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)
 
























# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])
 


























































# temps = [[0.0 for h in range(24)] for d in range(31)]


# total = 0.0
# for day in temps:
#     total += day[12]  # Índice 12 para 12:00 PM

# average = total / 31
# print("Temperatura média ao meio-dia:", average)

































































# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
 
# del list_1[0]
# del list_2
 
# print(list_3)


















































# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# list = []

# for i in  range(len(my_list)):
#     if i not in list:
#       list.append(i)

# my_list = list

# print("A lista com os elementos exclusivos aqui")
# print(my_list)

































# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits: int = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

# print(hits)












































# my_list = [1, 2, 3, 4, 5, 9, 10, 23, 39, 45]
# to_find = 6
# found = False

# for i in my_list:
#     found = i == to_find
#     if found:
#         break

# if found:
#     print("Numero encontrado!")
# else:
#     print("Ausente!")

















































# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]

# if 15 in my_list:
#     print("Elemento encontrado !")
# else:
#     print("Elemento não encontrado !") 






































































#largest = my_list[0]
 





















# for i in my_list[1:]:
#     if i > largest:
#         largest = i
 
# print(largest)




















































# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
 
# for i in my_list:
#     if i > largest:
#         largest = i
 
# print(largest)



































































# my_list = [17, 3, 5, 12, 4, 6]

# maior_num_list = my_list[0]

# for i in range(len(my_list)):
#     if maior_num_list < my_list[i]:
#         maior_num_list = my_list[i]
    
# print(maior_num_list)












































# list_1 = [12, 20]
# list_2 = list_1[:]

# list_1 = [40]

# print(list_2)

















































# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = list_1
# list_1[0] = 20

# print(list_2)













































# def saudacao():
#     print("Olá")
#     return "Bom dia!"

# i = saudacao()

# print(i)









































# def liters_100km_to_miles_gallon(mi):
#     fator: float = 1.60934
#     km: float = mi * fator
#     print(km)

# def miles_gallon_to_liters_100km(gal):
#     fator: float = 0.264172
#     lit = gal * 3.78541
#     print(lit)

# print(liters_100km_to_miles_gallon(1))

# print(miles_gallon_to_liters_100km(10))































































# import math

# def is_prime(n: int):
#    if n <= 1:
#      return False
#    if n == 2:
#      return True
#    if n % 2 == 0:
#      return False
#    else:
#     limite: int = int(math.sqrt(n))        
#     for i in range(3, limite, 2):
#          if n % i == 0:
#              return False
#     return True

# print("E primo:", is_prime(35))




















































# def is_year_leap(year: int):
#  if year % 4 != 0:
#   return False
#  elif year % 100 != 0:
#   return True
#  elif year % 400 != 0:
#   return False
#  else:
#   return True

# def days_in_month(year: int, month: int):
#  if year < 1582 or month < 1 or month > 12:
#   return None
#  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  res = days[month - 1]
#  if month == 2 and is_year_leap(year):
#   res = 29
#  return res

# def day_of_year(year: int, month: int, day: int):
#  days = 0
#  for m in range(1, month):
#   md = days_in_month(year, m)
#  if md == None:
#   return None
#  days += md
#  md = days_in_month(year, month)
#  if day >= 1 and day <= md:
#   return days + day
#  else:
#   return None

# print(day_of_year(2000, 12, 31))












































































# def is_year_leap(year: int):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

   
# def main():
#    entrada = input("Digite um ano (por exemplo, 2024):")

#    try:
#       ano = int(entrada)
#    except ValueError:
#       print("Por favor digite um numero inteiro valido")

#       return
#    if is_year_leap(ano):
#       print(f"{ano} e um ano bissexto!")
#    else:
#       print(f"{ano} não é um ano bissexto!")

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#  yr = test_data[i]
#  print(yr,"->",end="")
#  result = is_year_leap(yr)
#  if result == test_results[i]:
#      print("OK")
#  else:
#     print("Fracassado")


































# def strange_list_fun(n):
#  strange_list = []
 
#  for i in range(0, n):
#     strange_list.insert(0, i)
 
#  return strange_list

# print(strange_list_fun(5))

























































































# def function_list(n: int):
#     if(n % 2 == 0):
#         return True
    
# print(function_list(1))

# def saudacao(nome):
#     print("Olá, ", nome)

# saudacao("Carlos")





























































































# def mensagem():










































































#     print("Por favor digite um numero:")

# mensagem()
# a = int(input())
# mensagem()
# b = int(input())
# mensagem()
# c = int(input())


# def soma(a: int, b: int, c: int):
#     return a + b + c

# print(soma(a, b, c))














































# my_list = [8, 10, 6, 2, 4]
# swapped = True

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#        if my_list[i] > my_list[i + 1]:
#         swapped = True
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)        
            













































# from typing import List

# beatles: List[str] = []

# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print(beatles)

# for i in range(2):
#     print("Agora você deve adicionar os membros que faltam: ")
#     beatles.append(input())

# print(beatles)

# del beatles[3]
# del beatles[3]

# print(beatles)

# beatles.insert(0, "Ringo Starr")

# print(beatles)

































# numbers = [10, 5, 7, 2, 1]
# print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
# numbers[0] = 111
# print("\nConteúdo da lista anterior:", numbers)  # Imprimindo conteúdos de listas anteriores.
 
# numbers[1] = numbers[4]  # Copiando o valor do quinto elemento para o segundo.
# print("Novo conteúdo da lista:", numbers)  # Printing Conteúdo atual da lista.
 
# print ("\n List length:", len (numbers)) # Imprimindo o comprimento da lista.

# del numbers[1]

# print(numbers)

# numbers.append(9)

# print(numbers)

# numbers.insert(2, 222)

# print(f"Depois do metodo insert: {numbers}")




















































































# i = 0
# j = 7

# print(i and j)













































# i = 22
# j = 25

# log = i & j

# print(log)





































# for digit in "0165031806510":
#     if digit == "0":
#       digit = "x"
#     print(digit, end="")



















# nome = ""
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     if ch != "@":
#         nome += ch
# print(nome)































# print("Bem vindo ao loop for")

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     else:
#         print("i: ", i)






































# print("Olá usuario, seja bem-vindo!")
# nome = input("Como gostaria de ser chamado? ")

# print(f"Vamos começar {nome}")

# c0 = int(input("Digite um numero inteiro diferente de zero:"))

# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 // 2
#     else:
#         c0 = 3 * c0 + 1
#     print(f"O valor de c0 é {c0}")
#     finalizar_jogo = input("Deseja finalizar o jogo? s/n")
#     if finalizar_jogo.lower() == "s":
#         exit()

# print("Fim do programa....")






































# import math
#
# blocos = int(input("Digite um valor inteiro para uma quantidade de blocos:"))
#
# descriminante = math.sqrt(1 + 8 * blocos)
#
# altura = (-1 + descriminante ) // 2
#
# print(f"A altura da piramide é {altura}")
#
#
#
#








































# print("Seja Bem-Vindo!")
# print("Poderia escolher uma opção?")
# print("1 - para iniciar o jogo")
# print("2 - para que voce possar inserir o seu nome")
# print("0 - para sair do programa")
# entrada = int(input("Esolha uma opção:"))
#
# if entrada == 1 :
#     print("Digite um palavra: ")
#     palavra = input()
#
#     i = 5
#     while i < 5:
#         i += 1
#         print(palavra)
#     else:
#         print("Testando minhas novaas habilidades")
#
# elif entrada == 2:
#     nome = input("Poderia inserir o seu nome: ")
#     print(f"Olá {nome}, tudo bem com você")
#
# elif entrada == 0:
#     exit()
#
#

































# palavra = input("Digite uma palavras:")
# consoantes = ""
# palavra = palavra.upper()
# for letras in palavra:
#     if letras in "AEIOU":
#         continue
#     consoantes += letras
#
# print(consoantes)
#
# print("Fim da brincadeira...")
#
#
#
#


























# palavra = input("Digite uma palavras no sonsole:")
# palavra = palavra.upper()
# consoantes = ""
#
# print(palavra)
# for letras in palavra:
#     if letras == "A":
#         continue
#     elif letras == "E":
#         continue
#     elif letras == "I":
#         continue
#     elif letras == "O":
#         continue
#     elif letras == "U":
#         continue
#     else:
#         resultado = letras
#         print(resultado, end="")
#



















































# tentativas = 0
# nome = input("Digite o seu nome: ")
# print(f"Olá, {nome}! Bem-vindo ao jogo de adivinhação.")
#
# palavra_secreta = "chupacabra"
# print("O seu objetivo e acertar a palavra secreta, a sua primeira dica é, ele e um animal mistico")
# entrada_usuario = input()
#
# while True:
#     if palavra_secreta == entrada_usuario:
#         break
#     else:
#         print("Você errou! Tente novamente.")
#         entrada_usuario = input()
#         tentativas += 1
#
#     if tentativas == 3:
#         print("Você errou por três vezes! Iremos dar mais uma dica. Preparado ? Lá vai a dica")
#         print("O nome desse animal tem dez letras")
#         entrada_usuario = input()
#
#     if tentativas == 5:
#         print("Você estrapolou o seu numero de tentativas.")
#         print("Deseja continuar? s/n")
#         entrada = input()
#
#         if entrada != "s":
#             break
#         else:
#             print("Você recebeu mais 3 tentativas")
#             print("Ultima dica, o animal misterioso tem o abito de sair para chupar outra especie")
#             tentativas_extras = 0
#
#             entrada_usuario = input()
#
#             if entrada_usuario != palavra_secreta:
#                 tentativas_extras += 1
#                 if tentativas_extras ==3:
#                     print("Você perdeu")
#                     print("finalizando jogo...")
#
#
# print("Fim do jogo...")










































# break - exemplo

# print("The break instrução:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro do laço.", i)
# print("Fora do loop.")


# continue - exemplo

# print("The continue instrução:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro do laço.", i)
# print("Fora do loop.")
#






























# import time
#
# nome = input("Digite o seu nome: ")
# print(f"O usuario {nome}, vamos jogar um jogo? y/n")
# entrada = input()
#
# if entrada == "y":
#     for i in range(6):
#         print(f" Mississipi {i}")
#         time.sleep(1)
#     print("Pronto ou não lá vou eu !!")
# else:
#     print("Fechando jogo...")
#
#
#
#


































# for i in range(10):
#     print(i)
#
# for i in range(1, 11, 2):
#     print(f"O valor de i é {i}")
#
#

















































# secret_number = 777
#
# print(
# """
# +===================================+
# | Bem vindo ao meu jogo, trouxa!    |
# | Insira um número inteiro          |
# | e adivinhar o número que tenho    |
# | escolhidos para você.             |
# | Então, qual é o número secreto?   |
# +===================================+
# """)
# numero_usuario = int(input("Tente acertar o numero secreto. Digite um numero: "))
# while numero_usuario != secret_number:
#     print("Ha ha! Você está preso no meu loop!")
#     numero_usuario = int(input("Tente novamente. Digite um valor: "))
# print("Muito bem, trouxa! Você está livre agora.")
#















# year = int(input("Digite um ano: "))

# if year < 1582:
#   print("Não dentro do período do calendário gregoriano")
# elif year % 4 != 0 :
#      print("Ano comun")
# elif year % 100 != 0:
#       print("Ano bissexto") 
# elif year % 400 != 0:
#       print("Ano comun")
# else:
#      print("Ano bissexto")


































# income = float(input("Entre com os rendimentos anuais: "))
# tax: float = 0.0

# if income <= 85528:
#     tax = income * 0.18 - 556.02
#     if tax < 0:
#         tax = 0.0
# else:
#     tax = 14839.02 + (income - 85528) * 0.32

# tax = round(tax, 0)
# print("A taxa é:", tax, "thalers")





































































#sair = True

# while(sair):
#  planta = input("Digite o nome da planta: ")

#  if(planta == "spathiphyllum"):
#     print("No, I want a big Spathiphyllum!")

#  if(planta == "pelargonium"):
#     print("Spathiphyllum! Not pelargonium!")

#  if(planta == "Spathiphyllum"):
#     print("Yes - Spathiphyllum is the best plant ever!")
#  else:
#     print("O valor da entrada é inválido")

#  terminar = input("Deseja sair s/n ?")
#  if(terminar == "s"):
#     sair = False



































# sair = True

# while(sair):
#  planta = input("Digite o nome da planta: ")

#  if(planta == "spathiphyllum"):
#     print("No, I want a big Spathiphyllum!")

#  if(planta == "pelargonium"):
#     print("Spathiphyllum! Not pelargonium!")

#  if(planta == "Spathiphyllum"):
#     print("Yes - Spathiphyllum is the best plant ever!")
#  else:
#     print("O valor da entrada é inválido")

#  terminar = input("Deseja sair s/n ?")
#  if(terminar == "s"):
#     sair = False











































# numero1 = int(input("Digite o primeiro numero: "))
# numeor2 = int(input("Digite o segundo numero: "))
# numero3 = int(input("Digite o terceiro numero: "))

# numero_maior = max(numero1, numeor2, numero3)

# print("O maior numero é:", numero_maior)







































# numero1 = int(input("Digite o primeiro numero:"))
# numero2 = int(input("Digite o segundo numero:"))
# numero3 = int(input("Digite o terceiro numero:"))

# maoir_numero = numero1

# if(numero2 > maoir_numero):
#     maoir_numero = numero2

# if(numero3 > maoir_numero):
#     maoir_numero = numero3

# print("O maoir numero é:", maoir_numero)



















































# numero1 = int(input("Digite um valor:"))
# numero2 = int(input("Digite outro valor:"))
# numero_maior = 0

# if numero1 > numero2: 
#     numero_maior = numero1
# elif numero2 > numero1:
#      numero_maior = numero2
# else: 
#     print("Os valores digitados são iguais.")

# print(f"O maior numero entre os dois é: {numero_maior}")











































# entrada = input("Olá, digite o seu nome:")
# idade = int(input("Digite a sua idade:"))

# if(idade <= 16):
#     print("Adolecente")
# elif(idade == 17):
#     print("Esta quase atingindo a maioridade")
# elif(idade >= 18):
#     print("Você já e maior de idade")
# else:
#     print("O valor digitado e inválido. Encerrando programa...")



















# n = 100
# if (n >= 100):
#     print(True)
# else:
#     print(False)


































# x = 11
# y = 4

# x = x % y
# x = x % y
# y = y % x

# print(y)



# a = 4
# b = 3
# c = a % b
# print(c)







# anything = float(input("Digite um numero: "))
# something = anything ** 2.0
# print(anything, "elevado a 2 é:", something) 



























































# jonh = 3
# maria = 5
# adam = 6


# print(jonh, maria, adam, sep=",")

# soma = jonh + maria + adam

# print(soma)

# print("Numero total de maçãs:", soma)












































































































    # print("\"Eu Sou\" \n \"\" aprendizado \"\"\n \"\"\" python \"\"\"")






































# variavel_francionada = 3E8
# print(variavel_francionada)


# print("Eu sou uma string \"oi eu sou uma string\"")

# print('Eu gosto "Monty Python"')

# print("I\'m Monty Python")
# print("I'm Monty Python1")


# print(True > False)
# print(True < False)
 















# print("2", end=" ")
# print(2)

# numeroQuebrado: float = 2.0

# x: float = 1.0

# inteiro: int = 1_233_33

# negativo = +1

# octal = 0o123

# print(octal)


# valor_fracionado = .4
# print(valor_fracionado)      





































































































# # Solução de amostra

# ###################
# print("versão original:")
# ###################
# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")
# ###################
# print("com menos 'print()' invocações:")
# ###################
# print("    *\n   * *\n  *   *\n *     *\n***   ***")
# print("  *   *\n  *   *\n  *****")
# ###################
# print("mais alto:")
# ###################
# print("        *")
# print("       * *")
# print("      *   *")
# print("     *     *")
# print("    *       *")
# print("   *         *")
# print("  *           *")
# print(" *             *")
# print("******     ******")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *******")
# ###################
# print("dobrou:")
# ###################
# print("        *        "*2)
# print("       * *       "*2)
# print("      *   *      "*2)
# print("     *     *     "*2)
# print("    *       *    "*2)
# print("   *         *   "*2)
# print("  *           *  "*2)
# print(" *             * "*2)
# print("******     ******"*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *******     "*2)

































# print("Meu", "nome", "é", "Monty", "Python.", sep=",")


# print("Carlos", "Giovan", "Rafael", "Cati", sep="*", end=" ")
# print("O carlos é um bom companheiro", end=" ")
# print("Ninguém pode negar")





















































# print("A pequenina aranha escalou a tromba d'água.")
# print()
# print("Caiu a chuva e lavou a aranha.")


# print("A pequenina aranha", "subil", "a tromba d'água")


# idade = 22

# print("Idade:", idade)

# print("Hoje o dia esta frio", "meu deus", end=" ")
# print("Eu sei")






















































# idade = 22

# print(f"A minha idade é {idade}")




# print("Olá, pytohn!")
# print('carlos')


















# print("Hello world")

# idade = 22

# print(idade)

# x: str = "carlos"

# print(x)

# def Saudacao () :
#     print("Olá " + x)

# Saudacao()