#Módulo 1

#atividade 1
#print("olá mundo!")

#atividade2
#nome = input("digite seu nome:")
#print("é um prazer te conhecer, {}".format(nome))

#atividade 3
#numb1 = int(input("digite um número: "))
#numb2 = int(input('digite outro numero'))
#print ('A soma de {} com {} é {}'.format(numb1, numb2, numb1+numb2))

#atividade 4
#num = input("digite uma entrada: ")
#print ('ele é número: {}, é texto: {}, é alfanúmerico: {}'.format(num.isnumeric(), num.isalpha(), num.isalnum() ))

#atividade 5
#numero = float(input('Digite um número \n' ))
#print('O número informado é {}, seu antecessor é {} e seu sucessor {}'.format(numero, numero-1, numero+1))

#atividade 6
#num = float(input("informe um número \n"))
#print("o número informado é {}, seu dobro é {}, o triplo {}, e por fim a raiz quadrada {:.4f}".format(num, num*2, num*3, num**(1/2)))

#atividade 7
#nota1 = float(input("informe a primeira nota \n"))
#nota2 = float(input("informe a segunda nota \n"))
#print("a sua média é {:.1f}".format((nota1+nota2)/2))

#atividade 8
#metros = float(input("informe uma medida em metros \n"))
#print("a medida em metros equivale em centimetros a: {}cm e em milimetros a {}mm".format(metros*100, metros*1000))

#atividade 9
#num = float(input("informe um número para ser a tabuada \n"))
#print("a tabuada do número informado até 10 é: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(num*1, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9, num*10))

#atividade 10
#num = float(input("quantos reais você possui na sua carteira? \n"))
#print("você pode comprar a quantidade de doláres de: {:.2f}".format(num/3.27))

#atividade 11
#largura = float(input("informe a largura \n"))
#altura = float(input("informe a altura \n"))
#area = largura * altura
#print("a quantidade de tinta necessária para pintar a área da parede é de {:.0f} litros de tinta".format(area/2))

#atividade 12
#preco = float(input("informe o preço \n"))
#print("o novo preço com 5% de desconto é {:.2f}".format(preco*0.95))

#atividade 13
#salario = float(input("informe o salário para ser reajustado \n"))
#print("seu novo salário reajustado é de R${:.2f}".format(salario*1.15))

#atividade 14
#temp = float(input("Digite a temperatura em Celsius \n"))
#print("a temperatura em Fahrenheit é de {:.1f}F".format(temp*1.8+32))

#atividade 15
#km = float(input("informe a quantidade de Km rolados \n"))
#dias = int(input("informe a quantidade de dias usados \n"))
#preco = ((0.15*km)+(60*dias))
#print("O preço total a se pagar é de R${:.2f}".format(preco))

#aula
#from math import sqrt
#num = int(input("Insira um número \n"))
#raiz = sqrt(num)
#print("a raiz de {} é {}".format(num, raiz))
#import emoji
#print(emoji.emojize("Olá, mundo :earth_americas:", use_aliases=True))

#atividade 16
#from math import trunc
#num = float(input("informe um número \n"))
#print("o número arredondado é {}".format(trunc(num)))

#atividade 17
#import math
#catOps = float(input("informe o valor do cateto oposto \n"))
#catAdj = float(input("informe o valor para o cateto adjacente \n"))
#print("a hipotenusa é {:.2f}".format(math.sqrt(((catOps**2)+(catAdj**2)))))
#from math import hypot
#co = float(input("informe o cateto oposto \n"))
#ca = float(input("informe o cateto adjacente \n"))
#print("a hipotenusa é {:.2f}".format(hypot(co,ca)))

#atividade 18 
#import math
#graus = float(input("informe o ângulo \n"))
#angulo = graus * 2 * math.pi / 360 
#print("o cosseno é {:.2f}, o seno é {:.2f} e a tangente {:.2f}".format(math.cos(angulo), math.sin(angulo), math.tan(angulo))) 

#atividade 19
#from random import choice
#n1 = input("primeiro aluno: ")
#n2 = input("segundo aluno: ")
#n3 = input("terceiro aluno: ")
#n4 = input("quarto aluno: ")
#lista = [n1,n2,n3,n4]
#sorteado = choice(lista)
#print("o escolhido foi ", sorteado)

#atividade 20
#import random
#n1 = input("primeiro nome: ")
#n2 = input("segundo nome: ")
#n3 = input("terceiro nome: ")
#n4 = input("quarto nome: ")
#lista = [n1, n2, n3, n4]
#random.shuffle(lista)
#print("a ordem de apresentação será: ")
#print(lista)

#atividade 21 ERRO EM CIMA DE ERRO
#from playsound import playsound
#playsound('ex1.mp3')

#atividade 22
#nome = input("escreva seu nome \n")
#print(nome.upper())
#print(nome.lower())
#listaNome = nome.split()
#print("O total de letras é: {}".format(len(''.join(listaNome))))
#print("O primeiro nome possui {} letras".format(len(listaNome[0])))

#O professor utilizou do seguinte modelo para contar o total de letras do nome.
#Total de caracteres menos a contagem de caracteres vazios(espaços).
#print("seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))

#Para imprimir a quantidade de caracteres do primeiro nome, utilizou-se o artifício de procurar o caractere vazio(espaço) 
#que separa os nomes e utilizar a posição dele como o número de caracteres
#print("Seu primeiro nome tem {} letras".format(nome.find(' ')))

#atividade 23
#num = int(input("informe um número \n"))
#print("unidade {}".format(num // 1 % 10))
#print("dezena {}".format(num // 10 % 10))
#print("centena {}".format(num//100 % 10))
#print("milhar {}".format(num//1000 % 10))

#atividade 24
#cidade = input("digite o nome da sua cidade \n")
#cidade = cidade.strip().upper().split()
#print("sua cidade começa com santo: {}".format("SANTO" in cidade[0]))

#atividade 25
#nome = input("insira seu nome \n")
#nome = nome.upper().strip().split()
#print("Você possui silva no nome: {}".format("SILVA" in nome))

#Professor
#nome = input("insira seu nome")
#print("Você possui silva no nome: {}".format("SILVA" in nome.upper()))

# atividade 26 FALTANDO
#frase = str(input("Insira sua frase \n")).strip().lower()
#print("a quantidade de letras a que aparecem é de: {}".format(frase.count('a')))
#print("O índice da primeira letra a é a {}".format(frase.find('a')+1))
#print("O índice da última letra é {}".format(frase.rfind('a')+1))

#Professor
#frase = str(input("digite uma frase: ")).upper()
#print("a quantidade de letras A é de: {}".format(frase.count("A")))
#print("A primeira letra a aparece na posição {".format(frase.find("A"+1)))
#print("O índice da última letra é {}".format(frase.rfind('A')+1))

#atividade 27
#nome = str(input("Insira seu nome completo \n")).strip().split()
#print(f"Seu primeiro nome é {nome[0]}")
#Como o nome foi dividido, a função len irá ler as entradas da lista(cada nome que foi dividido 0,1,2,3...) ao invez de cada caractere
#print("Seu último nome é {}".format(nome[len(nome)-1]))

#atividade 28
#import random
#numpc = random.randint(0,5)
#print("o numero é {}".format(numpc))
#num = int(input("tente adivinhar um número entre 0 e 5 \n"))
#if num == numpc:
#    print("você acertou o número")
#else:
#    print("você errou o número")

#atividade 29
#velocidade = int(input("Qual a velocidade do veículo: "))
#if velocidade > 80:
#    print("você irá pagar uma multa no valor de R${},00".format((velocidade-80) * 7))
#print("passar bem")

#atividade 30
#num = int(input("informe um número \n"))
#if (num % 2) == 0:
#    print (f"O número {num} é par")
#else:
#    print (f"O número {num} é ímpar")

#atividade 31
#distancia = float(input("Informe a distância da viagem em quilômetros: "))
#if distancia <= 200:
#    print("O valor a ser pago é de R${:.2f}".format(distancia*0.5))
#else:
#    print("O valor a ser pago na viagem é de R${:.2f}".format(distancia*0.45))

#atividade 32
#import datetime
#ano = int(input('Insira um ano: '))
#if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
#    print("o ano é bissexto")
#else:
#    print("O ano não é bissexto")

#Modelo do professor
#from datetime import date
#ano = int(input('Insira um ano: '))
#if ano == 0:
#    ano = date.today().year
#if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
#    print("o ano é bissexto")
#else:
#    print("O ano não é bissexto")    

#atividade 33 
#a = int(input("Informe o primeiro número: "))
#b = int(input("Infome o segundo número: "))
#c= int(input("informe o terceiro número: "))
#menor = a
# menor
#if b < a and b < c:
#    menor = b
#if c < b and c < a:
#    menor = c
# maior
#maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b:
#    maior = c
#print(f'o menor valor é {menor}')
#print(f'o maior valor é {maior}')        

#atividade 34
#salario = float(input("informe o seu salário: "))
#if salario > 1250.00:
#   print(f"O seu salário com aumento é de R${salario*1.1}")
#else:
#    print(f'O seu salário com aumento é de R${salario*1.15}')

#atividade 35
#r1 = float(input('informe o tamanho da primeira reta: '))
#r2 = float(input('informe o tamanho da segunda reta: '))
#r3 = float(input("informe o tamanho da terceira reta: "))
#if r1+r2 >r3 and r1+r3 > r2 and r2+r3> r1:
#    print("os valores das retas formam um triângulo")
#else:
#    print("Os valores das retas não formam um triângulo")

#Aula 11
#print('\033[1;31;43m Olá mundo \033[m')
#nome = "Anderson"
#print('Olá {}{}{}'.format('\033[0;36m',nome, '\033[m'))

#Módulo 2

#atividade 36
#entradas
#casa = float(input("Qual o valor da casa que você irá comprar? \n"))
#salario = float(input("Qual o valor do salário? \n"))
#tempo = int(input("em quantos anos você irá pagar o empréstimo? \n"))
#processamento
#meses = tempo * 12 #anos em dias
#parcela = salario * 0.3 #calcula o valor da parcela que pode pagar
#empréstimo = casa / meses #calcula quanta será o valor do empréstimo por mês
#decisão
#if empréstimo <= parcela:
#    print("seu empréstimo foi aprovado com parcelas de R${:.2f} em {} meses".format(empréstimo, meses))
#else:
#    print("O empréstimo foi rejeitado.")

#atividade 37
#print('=-='*10)
#num = int(input("informe um número inteiro para conversão: "))
#print('=-='*10)
#escolha = int(input("agora escolha entre as seguintes opções de conversões: \n 1- binário \n 2- octal \n 3- hexadecimal \n"))
#print('=-='*10)
#if escolha == 1:
#    print("a transformação do número {0} para binário é: \'{1:b}\'".format(num, num))
#elif escolha == 2:
#    print("a transformação do número {} para octal é: \'{:o}\'".format(num, num))
#elif escolha == 3:
#    print("a transformação do número {} para hexadecimal é \'{:x}\'".format(num, num))
#else:
#    print("o número inserido não corresponde a uma transformações disponível")

#O modelo do professor para transformar e remover os dois digitos iniciais:
#print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
#print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
#print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))

#atividade 38
#num1 = float(input("insira o primeiro valor: "))
#num2 = float(input("insira o segundo valor: "))
#if num1 > num2:
#    print("O {} é maior que {}".format(num1,num2))
#elif num1 < num2:
#    print("O {} é menor que {}".format(num1,num2))
#else:
#    print("os valores são iguais")

#atividade 39
#import datetime
#anoatual = datetime.date.today().year
#sexo = str(input('qual o seu sexo? F- femino, M - masculino \n')).upper().strip()
#if sexo == 'M':
#    ano = int(input("Informe o ano de nascimento: "))
   # if anoatual - ano < 18:
  #      tempo = int(18 - (anoatual - ano))
 #       print("Você ainda irá se alistar, faltam {} anos".format(tempo))
#        print(f'O seu alistamento irá ocorre em {anoatual + (18-(anoatual-ano))}')
#    elif anoatual - ano == 18:
#        print("Esta na hora de se alistar")
#    else:
#        tempo = int((anoatual - ano)- 18)
#        print("o prazo de alistamento já passou em {} anos".format(tempo))
#        print(f'Ele ocorreu em {anoatual-((anoatual - ano)-18)}')    
#else:
#    print("Você é do sexo feminino e não precisa se alistar")

#atividade 40
#n1 = float(input('informe a primeira nota \n'))
#n2 = float(input('informe a segunda nota \n'))
#média =float((n1+n2)/2)
#if média < 5:
#    print("reprovado")
#elif 5 <= média <= 6.9:
#    print('Recuperação')
#else:
#    print('Aprovado') 

#atividade 41
#from datetime import date
#atual = date.today().year
#anoN = int(input('informe o ano de nascimento para saber a categoria do nadador: '))
#idade = atual - anoN
#if idade <= 9:
#    print('mirim')
#elif 9 < idade <= 14:
#    print('infantil')
#elif 14 < idade <= 19:
#    print('Junior')
#elif 19 < idade <= 25:
#    print('Sênior')
#else:
#    print('master')

#atividade 42
#n1 = float(input('informe a primeira medida do lado do triângulo: '))
#n2 = float(input('informe a segunda medida do lado do triângulo: '))
#n3 = float(input('informe a medida do terceiro lado do triângulo: '))
#if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
#   print("forma um triângulo")
#    if n1 == n2 == n3:
#        print('O triângulo é equilátero')
#    elif n1 != n2 != n3 != n1:
#        print('O triângulo é escaleno')
#    else:
#        print('O triângulo é isósceles')
#else:
#    print("não forma um triângulo")

#atividade 43
#altura = float(input('informe sua altura: '))
#massa = float(input('informe seu peso: '))
#imc = massa / (altura ** 2)
#if 0 < imc < 18.5:
#    print('Abaixo do peso')
#elif 18.5 <= imc < 25:
#    print('Peso ideal')
#elif 25 <= imc < 30:
#    print('sobrepeso')
#elif 30 <= imc < 40:
#    print('Obesidade')
#elif imc > 40:
#    print('Obesidade morbida')

#atividade 44
#preço = float(input('qual o valor normal do produto? '))
#print('=-='*20)
#print('1- à vista {}{}{}: {}{}{} de desconto'.format('\033[0;34m', 'dinheiro ou cheque' ,'\033[m', '\033[0;33m', '10%','\033[m'))
#print('2- à vista no {}{}{}: {}{}{} de desconto'.format('\033[0;34m', 'cartão' ,'\033[m', '\033[0;33m', '5%','\033[m'))
#print('3- Em até {}{}{} preço normal'.format('\033[0;34m', '2x no cartão' ,'\033[m'))
#print('4- {}{}{} no cartão: {}20{} de juros{} de juros'.format('\033[0;34m', '3x ou mais' ,'\033[m', '\033[0;33m', '%' ,'\033[m'))
#print('=-='*20)
#count=int(input('forma de pagamento? '))
#if count == 1:
#    print('O preço a se pagar é de R${:.2f}'.format(preço*0.9 ))
#elif count == 2:
#    print('O preço a se pagar é de R${:.2f}'.format(preço * 0.95))
#elif count == 3:
#    print('O preço a se pagar é de R${:.2f}'.format(preço))
#elif count == 4:
#    print('O preço a se pagar é de R${:.2f}'.format(preço*1.2))
#else:
#    print('A opção informada não está listada nas formas de pagamento')

#atividade 45
#import random
#from time import sleep
# escolhas = ['pedra', 'tesoura', 'papel'] #escolha do computador
#pc = random.choice(escolhas)
#print(pc)
#print('=-='* 20) #amostra das opções
#print('1-Pedra') 
#print('2-tesoura')
#print('3-Papel')
#print('=-='* 20)
#jogador = int(input('Você está jogando pedra, papel tesoura contra o computador, faça sua escolhe e tente vencê-lo! \n'))
#jogador = escolhas[jogador-1] #Escolha de decisões
#print('JO')
#sleep(1)
#print('KEN')
#sleep(1)
#print('PÔ!!!')
#Tomada de decisões
#if jogador == 'pedra' and pc == 'tesoura' or jogador == 'tesoura' and pc == 'papel' or jogador == 'papel' and pc == 'pedra':
#    print(f"você venceu, você escolheu {jogador} e o computador {pc}")
#elif jogador == pc:
#    print(f"Empate, vocês escolheram a mesma coisa que foi {jogador}")
#else:
#    print(f"você perdeu, vocÊ escolheu {jogador} e o computador {pc}")

#atividade 46
#from time import sleep
#print('=-='*20)
#print('Ano novo em...')
#print('=-='*20)
#for c in range(10,-1,-1):
#   print(c)
#   sleep(1)
#print('Feliz ano novo!')

#atividade 47
#for c in range(1,51):
#   if c % 2 == 0:
#      print(c)
#print('fim')

#modelo otimizado do professor
#for n in range(2,51, 2):
#   print(m, end=' ')
#print('acabou')

#atividade 48
#soma = 0
# for c in range(1,501):
#   if (c % 2 != 0) and c % 3 == 0:
#      soma += c
#print(soma)
# print('fim')

#modelo otimizado do professor
#soma = 0 # acumulador
#cont = 0 # contador
#for c in range(1, 501, 2): #já pega os números ímpares
#  if  c % 3 ==0: # divisíveis por três
#     soma += c
#     cont += 1
#print(soma)
#print(cont)

#atividade 49
#num = int(input('informe um número \n'))
#for c in range(1,11):
#   print('{:2} x {:2} = {:2}'.format(c,num , c*num ))
#print('fim')

#atividade 50
#soma = 0
#for c in range(0,6):
#   n = int(input('informe um número \n'))
#   if n % 2 == 0:
#      soma += n
#print(f'a soma dos números ímpares é {soma}')
#print('fim')

#atividade 51
#n1 = int(input('informe o primeiro termo para a PA \n'))
#razao = int(input('informe a razão \n'))
#for c in range(1,11):
#   print(n1+(c-1)*razao)
#print('fim')

#atividade 52
#div = 0
#num = int(input('informe um número para saber se ele é primo  \n'))
#for c in range(1,num+1):
#   if (c != 1) and (num % c == 0):
#      div += 1
#if div == 1:
#   print('É primo')
#else:
#   print('não é primo')

#modelo do professor mais bonito
#cont = 0
#num = int(input('digite um número: '))
#for c in range(1, num+1):
#   if num % c == 0:
#      print('\033[33m', end=' ')
#      cont += 1
#   else:
#      print('\033[31m', end=' ')
#   print('{}'.format(c), end = ' ')
#print('\n \033[m o número {} foi divisível {} vezes'.format(num, cont))
#if cont == 2:
#   print("O número é primo")
#else:
#   print('o número não é primo')

#atividade 53 Não soube fazer
#frase = str(input('digite uma frase: ')).strip().upper().split()
#junto = ''.join(frase)
#inverso = ''
#for letra in range(len(junto)-1, -1, -1):
#   inverso += junto[letra]
#if inverso == junto:
#   print('temos um palindromo')
#else:
#   print('não é um palindromo')
#print(junto, inverso)

#modelo sem o uso do laço de repetição
#frase = str(input('digite uma frase: ')).strip().upper().split()
#junto = ''.join(frase)
#inverso = junto[::-1] irá ler o string de trás pra frente usando fatiamento
#if inverso == junto:
#   print('temos um palindromo')
#else:
#   print('não é um palindromo')
#print(junto, inverso)

#atividade 54
#import datetime
#maiores = 0
#menores = 0
#atual = datetime.date.today().year
#for c in range(0, 7):
#   nasc = int(input('informe a data de nascimento \n'))
#   if atual - nasc >= 21:
#     maiores += 1
#   else:
#      menor += 1
#print('no total existem {} pessoas de maior e {} pessoas de menor'.format(maiores, menores))
#print('fim')

#atividade 55 Não sei tbm oxe
#maior = float
#menor = float
#for c in range(0,5):
#   peso = float(input(f'informe o peso da pessoa {c+1} \n'))
#   if c == 0:
#      menor = peso
#      maior = peso
#   else:
#      if peso > maior:
#         maior = peso
#      elif peso < menor:
#         menor = peso
#print('O maior peso foi de {}kg e o menor foi de {}kg'.format(maior, menor))

#atividade 56
#idadeTotal= 0
#maisVelho = 0
#nomeVelho = str
#jovens = 0
#for c in range(0,4):
#   print('-------{} Pessoa ------'.format(c+1))
#   nome = str(input('informe o nome da pessoa {} \n'.format(c+1)))
#  idade = int(input('Infome a idade da pessoa \n'))
#   sexo = str(input('''informe o sexo: 
#   [M] - MASCULINO
#   [F] - FEMININO \n''')).strip().upper()
#   
#   idadeTotal += idade
#   #Uma ideia seria colocar um if c == 0 para anotar o primeiro valor do mais velho
#   if idade >= maisVelho and sexo == 'M':
#      maisVelho= idade 
#      nomeVelho = nome
#   
#  if sexo == 'F' and idade < 20:
#      jovens += 1
#print('A média da idade do grupo é {}'.format(idadeTotal/4))
#print('O homem mais velho se chama {}'.format(nomeVelho))
#print('A quantidade de mulheres que tem menos de 20 anos é de {}'.format(jovens))

#atividade 57
#sexo = str(input('Informe seu sexo: ')).upper().strip()
#while sexo != ('M' or 'F'):
#   sexo = (input('Informe seu sexo, novamente \n')).upper().strip()
#print('O sexo informador foi Masculino'if sexo == 'M'else 'O sexo informado foi feminino')

#Modelo do professor que pega a primeira letra
#sexo = str(input('informe seu sexo: M/F: ')).strip().upper()[0]
#while sexo not in 'MmFf':
#   sexo = str(input('Informação inválida, insira novamente o sexo: ')).strip().upper()[0]
#print('O sexo {} foi registrado com sucesso'.format(sexo))

#atividade 58
#import random
#tentativas = 1
#numpc = random.randint(0,10)
#print(numpc)
#num = int(input('Tente adivinhar o número que o computador está pensando \n'))
#while num != numpc :
#   num = int(input('Errou, tente novamente \n'))
#   tentativas += 1
#print('você acertou o número com {} tentativas'.format(tentativas)) 

#atividade 59
#n1 = float(input('Insira o primeiro valor: '))
#n2 = float(input('Insira o segundo valor: '))
#n3 = 0
#while n3 != 5:
#   n3= int(input('''
   #[1] Somar
   #[2] Multiplicar
   #[3] Maior
   #[4] Novos números
   #[5] Sair
#   '''))
#   if n3 == 1:
#      print('{} + {} = {}'.format(n1, n2, n1+n2))
#   elif n3 == 2:
#      print('{} * {} = {}'.format(n1, n2, n1*n2))
#   elif n3 == 3:
#      if n1 > n2:
#         print(f'O maior é {n1}')
#      elif n2 > n1:
#         print(f'O maior é {n2}')
#     else:
#         print('os números são iguais')
#   elif n3 == 4:
#      n1 = float(input('Insira novamento o primeiro valor: '))
#      n2 = float(input('Insira novamente o segundo valor: '))
#   elif n3 != 5:
#      print('opção não é valida')
#print('fim')  

#atividade 60
#num = int(input('informe um número para o cálculo do seu fatorial: '))
#c = num
#fat = 1
#while c != 0:
#   print('{}'.format(c), end=' ')
#   print(' X ' if c>1 else ' = ', end='')
#  fat = fat * c
#   c -= 1
#print('{}! é {}'.format(num, fat))

#atividade 61
#n1 = int(input('informe o primeiro termo para a PA \n'))
#razao = int(input('informe a razão \n'))
#c = 1
#while c <= 10:
#   print(n1+(c-1)*razao, end=' ')
#   c += 1
#print('fim')

#atividade 62
#n1 = int(input('Informe o número para a PA: '))
#razão = int(input('informe a razão da PA: '))
#c = termos =1
#while termos != 0:
#   termos = int(input('Quantos termos você quer vê? '))
#  c = 1
#   while c <= termos:
#     print (n1+(c-1)*razão, end=" ")
#      c +=1
#print('fim')

#Modelo do professor
#print('gerador de PA')
#PRINT('-='*10)
#primeiro = int(input('Primeiro termo: '))
#razão = int(input('Razão da PA: '))
#termo = primeiro
#cont = 1
#total = 0
#mais = 10 #sEMPRE IRÁ MOSTRAR OS 10 PRIMEIROS TERMOS, FALHA NA LÓGICA DO PROFESSOR
#while mais != 0:
#   total += mais
#   while cont <= total:
#      print('{} > '.format(termo), end=' ')
#      termo += razão
#      cont += 1
#   print('Pausa')
#   mais = int(input('Quantos termos você quer mostrar a mais? '))
#   print('Foram mostrados {}'.format(total))

#atividade 63
#numero = 0
#anterior = 1
#anterior2 = 0
#contador = 1 #tem que começar de um número a menos porque o 1 sempre irá aparecer
#sequência = int(input('Quantos números você quer vê da sequência de Fibonacci: '))
#while contador < sequência:
#   numero = anterior + anterior2
#   if contador == 1: #condição para imprimir o 1 pela primeira vez, poderia ser colocado fora do while
#      print(numero, end=' ')
#   print(numero, end=' ')   
#   anterior2 = anterior
#   anterior = numero
#   contador += 1

#Modelo do professor que começa erroneamente por 0
#print('-'*30)
#print('Sequência de Fibonacci')
#print('-'*30)
#n = int(input('Quantos termos você quer vê? '))
#t1 = 0
#t2 = 1
#print('~~'*15)
#print('{} > {}'.format(t1, t2), end= ' ')
#cont = 3
#while cont <= n:
#   t3 = t2 + t1
#   print(' > {}'.format(t3), end=" ")
#  t1 = t2
#   t2 = t3
#   cont += 1
#print(' fim')

#atividade 64
#num = cont = acu = 0
#while num != 999:
#   num = int(input('digite um número inteiro, use o valor 999 para sair \n'))
#   if num != 999:   
#      acu += num
#      cont += 1
#print('Foram digitados {} números e a soma deles é {}'.format(cont, acu ))

#atividade 65
#contador = 0
#acumulador = 0
#numero = 0
#validador = 'S'
#while validador != 'N':
#   numero = int(input('Informe um número inteiro \n'))
#   validador = str(input('Quer continuar S/N? \n')).strip().upper()
#   contador += 1
#   acumulador += numero
#   if contador == 1:
#      maior = numero
#      menor = numero
#   if numero > maior:
#      maior = numero
#   if numero < menor:
#      menor = numero
#print('A média entre os números é {}'.format(acumulador/contador))
#print('O menor valor é {} e o maior valor {}'.format(menor, maior))

#atividade 66
#soma = cont = 0
#while True:
#   num = int(input('Digite um número(Digite 999 para parar): '))
#   if num == 999:
#      break
#   soma += num
#   cont += 1
#print(f'A soma dos números é {soma} e foram digitados {cont} números')

#atividade 67
#print('-'*20)
#print('Tabuada, digite número negativo para sair')
#print('-'*20)
#while True:
#   num = int(input('Quer ver a tabuada de qual valor? '))
#   if num < 0:
#      break
#   cont = 1
#   while cont <= 10:
#     print(f'{num} x {cont:2} = {num*cont}')
#      cont += 1
#print('fim')   

#atividade 68
'''
from random import randint

print('=-='*20)
print('Jogando ímpar ou par')
print('=-='*20)

sequência = 0

while True:
   computador = randint(0, 10)
   jogador = int(input('Digite um valor: '))
   escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
   jogada = (jogador + computador) % 2 == 0 # se for par retornar True, se for ímpar retorna False
   if jogada and escolha =='P': # True and True = True
      print('=-='*20)
      print(f'você jogou {jogador} e o computador {computador}. A soma é de {jogador+computador}, sendo Par')
      print('Você acertou!!! Tente novamente')
      print('=-='*20)
      sequência += 1
   elif not jogada and escolha == 'I': # not False and True = True and True = True
      print('=-='*20)
      print(f'Você jogou {jogador} e o o computador {computador}. A soma é de {jogador+computador}, sendo Ímpar')
      print('Você acertou!!! Tente novamente')
      print('=-='*20)
      sequência += 1
   else:
      print('=-='*20)
      print('Você perdeu!')
      print(f'Você jogou {jogador} e o computador jogou {computador}. A soma é de {jogador+computador}')
      print('=-='*20)
      break 
print(f'A sequência de vitória foi de {sequência}')
'''

#atividade 69
'''
print('-=-'*20)
print('Cadastro de pessoas')
print('-=-'*20)

maiores = homens = mulheres = 0

while True:
   idade = int(input('Informe a idade: '))

   sexo = ' '
   while sexo not in 'FnMn':
      sexo = str(input('informe o sexo: [F/M] ')).strip().upper()[0]

   if idade >= 18:
      maiores += 1
   if sexo == 'M':
      homens += 1
   if sexo == 'F' and idade < 20:
      mulheres += 1

   escolha = ' '
   while escolha not in 'SsNn':
      escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
   if escolha == 'N':
      break

print (f'A quantidade de pessoas de maior é de {maiores} pessoas')
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos')
'''

#atividade 70
"""
print('='*20)
print('Supermercado bigbom')
print('='*20)

total = custoMil = 0
barato = str
contador = 1

while True:
   nome = str(input('Qual o nome do produto? '))
   custo = float(input('Quanto custo o produto em R$? '))

   total += custo
   
   if custo > 1000:
      custoMil += 1

   if contador == 1:
      menor = custo
      barato = nome
      contador +=1

   if custo < menor: #Pode juntar com um OU junto com o if acima
      menor = custo
      barato = nome

   controle = ' '
   while controle not in 'SN':
      controle = str(input('quer continuar? [S/N]')).strip().upper()[0]
   
   if controle == 'N':
      break

print('='*20)
print(f'O total gasto foi de R${total:.2f}')
print(f'O total de produtos acima de mil reais foi de {custoMil} itens')
print(f'Ó nome do produto mais barato é: {barato}')
print('='*20)
"""

#atividade 71
#print('='*20)
#print('Caixa Eletrônico 24H')
#print('='*20)
#
#num = int(input('Quanto você deseja sacar? '))
#total = num
#resto = 0
#cinquenta = 0
#vinte = 0
#dez = 0
#um = 0
#
#cinquenta = total // 50
#resto = total % 50
#
#total = resto
#vinte = total // 20
#resto = total % 20
#
#total= resto
#dez = total // 10
#resto = total % 10
#
#total = resto
#um = total
#resto = 0
#
#print(f'serão entregue as seguintes notas: {cinquenta} de cinquenta, {vinte} de vinte, {dez} de dez, {um} de um real')

#Versão do professor
'''
print('='*30)
print('{:^30}'.format('Caixa 24h'))
print('='*30)

valor = int(input('Quanto você quer sacar? '))
total = valor
ced = 50
totced = 0
while True:
   if total >= ced:
      total -= ced
      totced += 1
   else:
      if totced > 0:
         print(f'total de {totced} cédulas de R${ced}')
      if ced == 50:
         ced = 20
      elif ced == 20:
         ced = 10
      elif ced == 10:
         ced = 1
      totced = 0
      if total == 0:
         break
print('fim')
'''

#Módulo 3

#atividade 72
'''
numero = ('zero','dois','três','quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete ', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20 \n'))
while (num < 0) or (num > 20):
    num = int(input('Número inválido, digite novamente \n'))
print(f' você digitou {numero[num]}')
print('fim')
'''
#modelo do professor otimizado
'''
while True:
   num = int(input('Digite um número entre 0 e 20: '))
   if 0 <= num <= 20:
      break
   print('tente novamente. ', end='')
'''

#atividade 73
'''
times = ('Bragantino', 'Atlético-PR', 'Palmeiras', 'Fortaleza', 'Bahia', 'Santos', 'Atlético-GO', 'Atlético-MG', 'Fluminense', 'Flamengo', 'Corinthians', 'Ceará', 'Internacional', 'Juventude', 'Sport', 'Cuiabá', 'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio')
print('=='*20)
print(f'Os 5 primeiors colocados são {times[:5]}')
print('=='*20)
print (f' os últimos 4 colocados são {times[-4:]}')
print('=='*20)
print(f' Os times em ordem alfábetica: {sorted(times)}')
print('=='*20)
chapeco = (times.index('Chapecoense')+1)
print(f'Chapecoense está na posicão {chapeco}')
print('=='*20)
'''

#atividade 74
"""
from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
tupla = (n1, n2, n3, n4, n5)
menor = maior = 0
for c in range(0,len(tupla)):
   if c == 0:
      maior = tupla[c]
      menor = tupla[c]
   else:
      if tupla[c] > maior:
         maior = tupla[c]
      if tupla[c] < menor:
         menor = tupla[c]
print(tupla)   
print(f'O menor é {menor}')
print(f'O maior é {maior}')
"""

#Modelo do professor (OTIMIZADO)
'''
from random import randint
n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteadors foram {n}')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
'''

#atividade 75 
'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('digite o quarto valor: '))
tupla = (n1,n2,n3,n4)
contP = 0
cont9 = 0
for c in tupla:
   if c == 9:
      cont9 += 1
   if c % 2 == 0:
      contP += 1
if cont9 > 0:
   print(f'O valor 9 apareceu {cont9} vezes')
else:
   print('Não foram digitados valores 9')
if 3 in tupla:
   print(f' O valor 3 está na posição: {tupla.index(3)+1}')
else:
   print('Não foram informados valores de número 3')
if contP > 0:
   print(f'A quantidade de números pares é de {contP}')
else:
   print('Não foram digitados valores pares')
'''

#modelo do professor
'''
num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), 
int(input('Digite um valor: ')), int(input('Digite um valor: ')), 
int(input('Digite um valor: ')))
print(f'Os valores digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
   print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
   print('O valor três não foi digitado')
for n in num:
   if n % 2 == 0:
      print(n, end=' ')
'''

#atividade 76
'''
lista = ('lápis', 1.75,
'caderno', 15.00,
'borracha', 2,
'Estojo', 20,
'Transferidor', 4.20,
'mochila', 124.20)
print('-'*40)
print('Listagem de Preços')
print('-'*40)
for p in range(0,len(lista)):
   if p % 2 == 0:
      print(f'{lista[p]:.<30}', end = ' ')
   else:
      print(f'R$ {lista[p]:>7.2f}')
print('-'*40)
'''

#atividade 77
'''
palavras = ('aprender','gratis','programar','futuro','Python','curso','free','programador')
for p in palavras:
   print(f'\nNa palavra {p.upper()} temos ', end='')
   for letra in p:
      if letra.lower() in 'aeiou':
         print(letra, end=' ')
'''

#aula 17
'''
valores = []
for cont in range(0, 5):
   valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
   print(f'Na posição {c} encontrei o valor {v}!')
print('fim')
'''

#atividade 78
'''
lista = []
for c in range(0,5):
   lista.append(float(input(f'informe o valor {c+1}: ')))
print(f'O maior foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor foi {min(lista)} na posição {lista.index(min(lista))}')
'''
#Modelo do professor para mostrar mais de um índice
'''
for i, v in enumerate(lista): #O i representa o índice e o v o valor do item na lista
   if v == maior:
      print(f'{i}...', end= ' ')
'''

#atividade 79
'''
lista = []
p = 0
while True:
   c = float(input(f'Insira o valor da posição {p} \n'))
   if c not in lista:
      lista.append(c)

   p += 1

   controle = ' '
   while controle not in 'SsNn':
      controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
   if controle == 'N':
      break
print('='*30)
print(f'Os valores ÚNICOs em ordem crescente são {sorted(lista)}')
print('fim')
'''

#modelo do professor
'''
numb = list()
while True:
   n = int(input('Digite um número: '))
   if n not in numb:
      numb.append(n)
      print('número adicionado')
   else:
      print('Valor duplicado, não pode ser adicionado a lista')   
   r = str(input('quer continuar? [S/N]')).strip().lower()[0]
   if r in 'Nn':
      break
print('-'*30)
print(f'Os número digitados fora: {sorted(numb)}')
'''   

#atividade 80 NÃO CONSEGUI
'''
lista = []
for c in range(0,5):
   n = int(input('Digite um valor: '))
   if c == 0 or n > lista[-1]:
      lista.append(n)
      print('adicionado ao final da lista')
   else:
      pos = 0
      while pos < len(lista):
         if n <= lista[pos]:
            lista.insert(pos, n)
            print(f'adicionado na posição {pos} da lista')
            break
      pos += 1
print('-'*30)
print(lista)
'''

#atividade 81
'''
lista = []
c = 0
while True:
   lista.append(float(input(f'Informe o {c}º número \n')))
   c +=1

   controle = ' '
   while controle not in 'SN':
      controle = str(input('Quer continuar? [S/N] \n')).strip().upper()[0]
   if controle == 'N':
      break
print('='*40)
print(f'Foram digitados {len(lista)} números')
print(f'a lista é: {sorted(lista, reverse=True)}')
if 5 in lista:
   print(f'O cinco está presente e na posição {lista.index(5)}')
else:
   print('O cinco não está presente')
print('='*40)
print('fim')
'''

#atividade 82
'''
lista = []
impar = []
par = []
c = 0
while True:
   lista.append(float(input(f'Digite um valor na posição {c} \n')))
   if lista[c] % 2 == 0:
      par.append(lista[c])
   else:
      impar.append(lista[c])
   c += 1
   controle = ' '
   while controle not in 'sn':
      controle = str(input('Quer continuar? [S/N]\n')).strip().lower()[0]
   if controle == 'n':
      break
print('As listas são:')
print(f'A lista um: {sorted(lista)}')
print(f'A lista dos pares: {sorted(par)}')
print(f'A lista dos impares: {sorted(impar)}')
print('Fim')
'''

#Outro modelo
'''
numero = [] 
while True:
   numero.append(float(input('Informe um valor a ser armazenado\n')))
   controle = ' '
   while controle not in 'SN':
      controle = str(input('Quer continuar? [S/N] \n')).strip().upper()[0]
   if controle == 'N':
      break
par = []
impar = []
for c, valor in enumerate(numero):
   if valor % 2 ==0:
      par.append(valor)
   else:
      impar.append(valor)
print('=-='*20)
print(numero)
print(par)
print(impar)
print('=-='*20)
'''

#atividade 83
'''
expressão = str(input('digite uma expressão \n'))
if expressão.count(')') == expressão.count('('):
   print('expressão válida')
else:
   print('expressão inválida')
print('fim')
'''
#Modelo do professor
'''
expressão = str(input('Digite a expresão: '))
pilha = []
for simb in expressão:
   if simb == '(':
      pilha.append('(')
   elif simb == ')':
      if len(pilha) > 0:
         pilha.pop()
      else:
         pilha.append(')')
         break
if len(pilha) == 0:
   print('Expressão válida')
else:
   print('Expressão inválida')
'''

#aula 18
'''
galera = []
dado = list()
maior = menor = 0
for c in range(0,3):
   dado.append(str(input('Nome: ')))
   dado.append(str(input('Idade: ')))
   galera.append(dado[:])
   dado.clear()

for p in galera:
   if p[1] >= 21:
      print(f'{p[0]} é maior de idade.')
      maior += 1
   else:
      print(f'{p[0]} é menor de idade.')
      menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')
'''

#atividade 84 (Faltou listar os mais pesados, não só um)
'''
lista = []
temp = list()

while True:
   temp.append(str(input('Informe seu nome \n')))
   temp.append(float(input('Informe seu peso \n')))
   
   lista.append(temp[:])
   temp.clear()

   controle = ' '
   controle = str(input('quer continuar? [S/N] \n')).strip().upper()[0]
   if controle == 'N':
      break

print(lista)
print(f'Foram cadastrados ao todo {len(lista)} pessoas')

maior = menor = c = 0
for p in lista:
   if c == 0:
      maior = p[1]
      nomeMax = p[0]      
      menor = p[1]
      nomeMin = p[0]
      c += 1
   elif p[1] > maior:
      maior = p[1]
      nomeMax = p[0]
   elif p[1] < menor:
      menor = p[1]
      nomeMin = p[0]   
print(f'O mais pesado foi {nomeMax} com {maior:.2f}Kg')
print(f'O menos pesado foi {nomeMin} com {menor:.2f}Kg')
print('fim')
'''

#modelo do professor
'''
temp = []
prin = []
maior = menor = 0

while True:
   temp.append(str(input('Nome: ')))
   temp.append(float(input('Peso: ')))
   if len(prin) == 0: #verificar se não foi cadastrado nada ainda e assimilar o maior e menor aos maiores valores
      maior = menor = temp[1]
   else:
      if temp[1] > maior: #funciona, pois logo irá da um clear e o índice 1 da lista temp irá ficar vazia
         maior = temp[1]
      if temp[1] < menor:
         menor = temp[1]
   prin.append(temp[:]) #passa a lista temp para a principal
   temp.clear() #limpa a lista temp para ser usada novamente, com índices resetados
   resp = str(input('Quer continuar? [S/N] \n')).strip().upper()[0]
   if resp in 'Nn':
      break

print('=='*30)
print(f'os dados foram {prin}')
print(f'foram cadastrados {len(prin)}')
print(f'O maior peso foi {maior}', end='')
for p in prin:
   if p[1] == maior:
      print(f' [{p[0]}]', end=' ')
print()
print(f'O menor peso foi {menor}', end='')
for p in prin:
   if p[1] == menor:
      print(f' [{p[0]}]', end=' ')
'''

#atividade 85
'''
lista = []
impar = list()
par = list()
for c in range(0,7):
   num = int(input(f'digite o {c+1}º valor \n'))
   if num % 2 == 0:
      par.append(num)
   else:
      impar.append(num)

lista.append(par[:]) 
lista.append(impar[:])

print(f'Os valores pares são: {sorted(lista[0])}')
print(f'Os valores ímpares são: {sorted(lista[1])}')
print('fim')
'''

#modelo do professor
'''
num = [[], []]
valor = 0
for c in range(0,7):
   valor = int(input('Digite um valor: '))
   if valor % 2 == 0:
      num[0].append(valor)
   else:
      num[1].append(valor)
print('='*30)
print(f'Todos os valores: {num}')
print(f'Os valores pares: {sorted(num[0])}')
print(f'Os valores impares{sorted(num[1])}')
'''

#atividade 86
'''
Lmatriz = []
Cmatriz = list()

for i in range(0,3):
   for j in range(0,3):
      num = int(input(f'Insira o valor para a posição [{i}, {j}] \n'))
      Cmatriz.append(num)
   Lmatriz.append(Cmatriz[:])
   Cmatriz.clear()

for i in range(0,3):
   for j in range(0,3):
      print(f'[ {Lmatriz[i][j]} ]', end='')
   print('')
print('{:-^30}'.format('Fim'))
'''

#Modelo do professor
'''
matriz = [[0,0,0,], [0,0,0,], [0,0,0,]]
for i in range(0,3):
   for j in range(0,3):
      matriz[i][j] = int(input(f'Digiten o valor da posição [{i}, {j}] \n'))
print('='*15)
for i in range(0,3):
   for j in range(0,3):
      print(f'[{matriz[i][j]:^5}]', end='')
   print()
'''

#atividade 87 
'''
Lmatriz = []
Cmatriz = list()
soma = terceira = 0
for i in range(0,3):
   for j in range(0,3):
      num = int(input(f'Insira o valor para a posição [{i}, {j}] \n'))
      if num % 2 == 0:
         soma += num
      if i == 2:
         terceira += num
      Cmatriz.append(num)
   Lmatriz.append(Cmatriz[:])
   Cmatriz.clear()

for i in range(0,3):
   for j in range(0,3):
      print(f'[{Lmatriz[i][j]:^5}]', end='')
   print()
print(f'A soma dos números pares da matriz são: {soma}')
print(f'A soma da terceira linha da matriz é {terceira}')
print(f'O valor máximo da terceira linha é {max(Lmatriz[2])}')
'''

#Modelo do professor
'''
matriz = [[0,0,0,], [0,0,0,], [0,0,0,]]
soma = maior = terceira = 0
for i in range(0,3):
   for j in range(0,3):
      matriz[i][j] = int(input(f'Digiten o valor da posição [{i}, {j}] \n'))
print('='*15)
for i in range(0,3):
   for j in range(0,3):
      print(f'[{matriz[i][j]:^5}]', end='')
      if matriz[i][j] % 2 == 0:
         soma += matriz[i][j]
   print()
print('-=-'*30)
print(f'A soma dos números pares é {soma}')
for i in range(0,3):
   terceira += matriz[i][2]
print(f'A soma da terceira linha é {terceira}}')
for c in range(0, 3):
   if c == 0:
      maior == matriz[1][c]
   elif matriz[1][c] > maior:
      maior = matriz[1][c]
print(f'O maior valor da linha dois é {maior}')
'''
   
#atividade 88
'''
from random import randint
from time import sleep
matriz = []
tabela = list()
palpites = int(input('Quantos palpites você quer? \n'))
total = 1
while total <= palpites:
   cont = 0
   while True:
      num = randint(0,60)
      if num not in tabela:
         tabela.append(num)
         cont += 1
      if cont >= 6:
         break
   tabela.sort()
   matriz.append(tabela[:])
   tabela.clear()
   total += 1
for i, l in enumerate(matriz):
   print(f'Jogo {i+1}: {l}')
   sleep(1)
print('fim')
'''

#atividade 89
'''
ficha = []
while True:
   nome = str(input('Nome: '))
   nota1 = float(input('Nota 1: '))
   nota2 = float(input('Nota 2: '))
   media = (nota1 + nota2) / 2
   ficha.append([nome, [nota1, nota2], media])
   resposta = str(input('Quer continuar? S/N \n ')).strip().upper()[0]
   if resposta in 'N':
      break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
   print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
   print('-'*35)
   opção = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
   if opção == 999:
      print('fim')
      break
   if opção <= len(ficha)-1:
      print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
print('<<< Volte Sempre >>>')
'''

#aula 19
'''
pessoas = {'nome': 'anderson', 'sexo':'M', 'idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
'''
'''
brasil = list()
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
'''
'''
estado = dict()
brasil = list()
for c  in range(0,3):
   estado['uf']= str(input('Unidade Federativa: '))
   estado['sigla']= str(input('Sigla do estado: '))
   brasil.append(estado.copy())
for e in brasil:
   for k, v in e.items():
      print(f'O campo {k} tem valor {v}.')
'''

#atividade 90
'''
aluno = dict()
aluno['nome'] = str(input('Nome do aluno \n'))
aluno['média'] = float(input(f'A média de {aluno["nome"]} \n'))
if aluno['média'] >= 7:
   aluno['situação'] = 'aprovado'
elif 5 <= aluno['média'] < 7:
   aluno['situação'] = 'recuperação'
elif aluno['média'] < 3:
   aluno['situação'] = 'reprovado'
for k, v in aluno.items():
   print(f'O campo {k} é {v}')
'''

#atividade 91 
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = { 
'jogador1': randint(1,5),
'jogador2': randint(1,5),
'jogador3': randint(1,5),
'jogador4': randint(1,5),
'jogador5': randint(1,5)
}
print('valores sorteados')
for k, v in jogo.items():
   print(f'{k} tirou {v} no dado ')
   sleep(1)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
   print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
   sleep(1)
'''

#atividade 92 
'''
import datetime
dados = dict()
anoAtual = datetime.date.today().year

dados['nome'] = str(input('Informe o nome \n'))

ano = int(input('informe o ano de nascimento \n'))
dados['idade'] = anoAtual - ano

ctps = int(input('Carteira de trabalho (0 caso não tenha) \n'))
if ctps != 0:
   dados['contrato'] = int(input('ano de contratação \n'))
   dados['salário'] = float(input('Salário R$ \n'))
   aposentadoria = dados['contrato']+35
print(dados)

for k, v in dados.items():
   print(f'{k} é {v}')

if ctps != 0:
   print(f'Aposentadoria em {aposentadoria}')
'''

'''
#modelo do professor
from datetime import datetime
dados = dict()
dados['nome']= str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
   dados['contratação'] = int(input('Ano de contratação: '))
   dados['salário'] = float(input('Salário: R$'))
   dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-'*30)
for k,v in dados.items():
   print(f' {k} tem o valor {v}')
'''

#atividade 93
''' 
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input (f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, total):
   partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
   print(f'{k} tem o vlaor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
   print(f' => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''

#atividade 94
'''
galera = list()
pessoa = dict()
soma = média = 0
while True:
   pessoa.clear()
   pessoa['nome'] = str(input('Nome: '))
   while True:
      pessoa['sexo'] = str(input('Sexo: [M/F]')).upper[0]
      if pessoa['sexo'] in 'MF':
         break
      print('Erro, por favor, digite apenas M ou F.')
   pessoa['idade'] = int(input('idade: '))
   soma += pessoa['idade']
   galera.append(pessoa.copy())
   while True:
      resposta = str(input('Quer continuar? [S/N]')).upper[0]
      if resposta in 'SN':
         break
      print('Erro, responda apenas S ou N.')
   if resposta == 'N':
      break
print('-='*30)
print(f'Foram cadastrado {len(galera)} pessoas.')
média = soma / len(galera)
print(f'A média das idades é de {média:5.2f} anos.')
print(' As mulheres cadastradas foram', end='')
for p in galera:
   if p['sexo'] in 'Ff':
      print(f'p["nome"] ', end='')
print()
print('Lista de pessoas que estão acima da média: ')
for p in galera:
   if p['idade'] >= média:
      print('', end='')
      print(' ')
      for k, v in p.itens():
         print(f'{k} = {v};', end='')
print('<< ENCERRADO >>')
'''

#atividade 95 
'''
time = list()
jogador = dict()
partidas = list()

while True:
   jogador.clear()
   jogador['nome'] = str(input('Nome do jogador: '))
   total = int(input (f'Quantas partidas o {jogador["nome"]} jogou? '))
   partidas.clear()
   for c in range(0, total):
      partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
   jogador['gols'] = partidas[:]
   jogador['total'] = sum(partidas)
   time.append(jogador.copy())
   while True:
      resposta = str(input('quer continuar? [S/N]')).upper()[0]
      if resposta in 'SN':
         break
      print('Erro, responda apenas S ou N.')
   if resposta == 'N':
      break

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
   print(f'{i:<15}', end='')
print()
print('-'*40)   
for k, v in enumerate(time):
   print(f'{k:>3}', end='')
   for d in v.values():
      print(f'{str(d):<15}', end='')
   print()
print('-'*40)

while True:
      busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
      if busca == 999:
         break
      if busca >= len(time):
         print(f'Erro, não existe jogador com código {busca}')
      else:
         print(f'Levantamento do jogador {time[busca]["nome"]:}')
         for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gols.')
      print('-'*30)
print('fim')
'''

#aula 20
'''
def soma(a, b):
   s = a + b
   print(s)

#programa principal:
soma(4,5)
soma(8,9)
soma(2,1)
soma(b=4, a=5)
'''
'''
def contador(*num):
   tam = len(num)
   print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8,0)
contador(4, 4, 7, 6, 2)
'''
'''
def dobra(list):
   pos = 0
   while pos < len(list):
      list[pos] *= 2
      pos += 1

valores = [6 , 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

#atividade 96
'''
def area(a,b):
   print(f'a área do seu terro é de {a*b}')

a = float(input("informe o comprimento do terreno. \n"))
b = float(input("informe a largura do terreno. \n"))
area(a,b)
'''

#modelo do professor
'''
def área(larg, comp):
   a = larg* comp
   print(f'A área de um terrenos {larg}x{comp} é de {a}m²')
   
 
print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura(m): '))
c = float(input('Comprimento (m): '))
área(l, c)
'''

#atividade 97
'''
def escreva(text):
   tamanho = len(str((text)))+4
   print('='*tamanho)
   print(f'  {text}')
   print('='*tamanho)

escreva(str(input('escreva uma mensagem \n')))
'''

#atividade 98
'''
from time import sleep

def contador(inicio, fim, passo):
   if inicio == fim == passo == 0:   
      print('Contagem de 1 até 10 em 1 em 1: ')
      for c in range(0, 10):
         print(c+1, end=' ')
         sleep(0.5)         
      print ( )
      print('Contagem de 10 até 0 de 2 em 2: ')
      for c in range(10, -1, -2):
         print (c, end=' ' )
         sleep(0.5) 
      print()
   else:
         print('Sua contagem personalizada é:')
         print(f'De {inicio} até {fim} com passo de {passo} em {passo}')
         if passo <= 0:
            for i in range(inicio, fim-1, passo):
               print(i, end= ' ')
               sleep(0.5) 
         else:
            for i in range(inicio, fim+1, passo):
              print(i, end= ' ') 
              sleep(0.5)           

contador(0,0 ,0 )

print('Agora é sua vez, faça um contador!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
   passo = 1
contador(inicio,fim,passo)
'''

'''
#modelo do professor
from time import sleep

def contador(i, f, p):
   if p < 0:
      p *= -1
   if p == 0:
      p= 1  

   print(f'Contagem de {i} até {f} de {p} em {p}')
   sleep(2.5)


   if i < f:
      cont = 1
      while cont <= f:
         print(f'{cont}', end=' ')
         sleep(0.5)
         cont += p
      print('Fim')
   else:
      cont = 1
      while cont >= f:
         print(f'{cont}', end=' ')
         sleep(0.5) 
         cont -= p
      print('Fim') 
   print('-=-'*20)


#Main program
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('passo: '))
contador(ini,fim,pas)
'''

#atividade 99
'''
def maior():
   
   lista = list()
   while True:
      lista.append(int(input('Informe um número: '))) 
      while True:
         resposta = str(input('Quer continuar? [S/N]')).upper()[0]
         if resposta in 'SsNn':
            break
         print('Apenas respostas com S ou N.')
      if resposta == 'N':
         break
   print(f'O maior valor da lista: {lista} é {max(lista)}')

maior()
'''
'''
#modelo do professor
from time import sleep

def maior(*num):
   cont = maior = 0
   print('\n Analisando os valores passados...')
   for valor in num:
      print(f'{valor}', end=' ', flush=True)
      sleep(0.3)
      if cont == 0:
         maior = valor
      else:
         if valor > maior:
            maior = valor
      cont += 1

   print(f'Foram informados {cont} valores ao todo.')
   print(f'O maior valor informado foi {maior}.')

maior(2, 9, 1, 9 , 20, 0, 23)
'''

#atividade 100
'''
numeros = list()

def sorteia(lista):
   from random import randint
   for c in range(0,5):
      lista.append(randint(1,10))
   print(lista)

def somaPar(lista):   
   soma = 0
   for c in range(0, len(numeros)):
      if lista[c] % 2 == 0:
         soma += lista[c]
   print(f'A soma dos valores pares da lista é {soma}')

sorteia(numeros)
somaPar(numeros)
'''
'''

#aula 21
def contador(i, f, p):
   """
   => Faz uma contagem demonstrando na tela
   i para inicio da contagem
   f para fim da contagem
   p para passo da contagem
   retunr: null
   function criada por Anderson Carlos
   """
   c = i
   while c <= i:
      print(f'{c}', end=' ')
      c += p
   print('Fim')

help(contador)

#
def somar(a=0,b=0,c=0):
   """
   Função somar, soma os parâmetros a, b e c, respectivamente.
   caso um parâmetros não seja informado, assumirá o valor de 0
   """
   s = a+b+c
   print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar()

#
def test(b):
   # b e c é uma variável local
   # chamando o a global.
   global a
   b += 4
   c = 2
   print(f'A dentro vale {a}')
   print(f'B dentro vale {b}')
   print(f'C dentro vale {c}')

#Main program
# a sendo variável global
a = 5
test(a)
print(f'A fora vale {a}')

#
def somar(a=0,b=0,c=0):
   """
   Função somar, soma os parâmetros a, b e c, respectivamente.
   caso um parâmetros não seja informado, assumirá o valor de 0
   """
   s = a+b+c
   return s

r1 = somar(3,2,5)
r2= somar(8,4)
r3= somar()
print(f'os resultados foram {r1}, {r2} e {r3}')

#
def fatorial(num1):
   f= 1
   for c in range(num1, 0, -1):
      f *= c
   return f

f1 = fatorial(3)
f2 = fatorial(4)
f3 = fatorial(5)
print(f'Os resultados são {f1},{f2} e {f3}')

#
def par(num):
   if num % 2 ==0:
      return True
   else:
      return False

num = int(input('Digite um número: '))
if par(num):
   print('É par')
else:
   print('Não é par')
'''

#atividade 101
'''
def voto(idade=0):
   if idade < 16:
      return print('NEGADO')
   elif (idade >= 16 and idade <= 18) or idade >= 80:
      return print('OPCIONAL')
   elif idade > 18 and idade <80:
      return print('OBRIGATÓRIO')
voto()
'''

#modelo do professor
'''
def voto(ano):
   from datetime import date
   atual = date.today().year
   idade = atual - ano
   if idade < 16:
      return f'Com {idade} anos: NÃO VOTA.'
   elif 16 <= idade < 18 or idade > 65:
      return f'Com {idade} anos: VOTO OPCIONAL.'
   else:
      return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

#programa principal
nasc = int(input('Em que ano você nasceu?'))
print(voto(nasc))
'''

#atividade 102
'''
def fatorial(i, show=False):
   """
   Função fatorial:
   i = número fatorial
   Show = False - não mostra o cálculo
   Show = True - mostra o cálculo
   """
   f = 1
   for c in range(i, 0, -1):
      f *= c
   
   if show == False:
      return print(f'{f}')
   else:          
      for c in range(i,0,-1):
         print(f'{c}', end='')
         if c != 1:
            print(' x ', end='')
         else:
            print(f' = {f}')      
      

fatorial(5, show=True)
'''

'''
#Modelo do professor
def fatorial(n, show=False):
   """
   Função fatorial:
   n = número fatorial
   Show = False - não mostra o cálculo
   Show = True - mostra o cálculo
   """   
   f = 1
   for c in range(n, 0, -1):
      if show:
         print(c, end='')
         if c > 1:
            print(' x ', end='')
         else:
            print(' = ', end='')
      f *= c
   return f


#main program
print(fatorial(5, show=True))
'''

#atividade 103 
'''
def ficha(nome='<desconhecido>', gol=0):
   print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


#main program
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
   g = int(g)
else:
   g = 0
if n.strip() == '':
   ficha(gol=g)
else:
   ficha(n, g)
'''

#atividade 104
'''
def leiaint(num):
   if type(num) == int:
      return print(f'O valor [{num}] foi aceito por ser um número')
   else:
      return print(f'O valor [{num}] não é um número e por isso foi rejeitado')


num = str(input('informe um valor '))
if num.isnumeric():
   num = int(num)
leiaint(num)
'''

#modelo do professor
'''
def leiaInt(msg):
   ok = False
   valor = 0
   while True:
      n = str(input(msg))
      if n.isnumeric():
         valor = int(n)
         ok = True
      else: 
         print('\033[0;31m ERRO! Digite um número inteiro válido.\033[m')
      if ok:
         break
   return valor


#main program
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
'''

#atividade105
'''
def notas(*n, sit=False):
   """
   -> FUNÇÃO NOTAS: avaliar as notas que foram repassadas, sendo quantas forem necessárias
   - n: são as notas a serem repassadas.
   - sit=True  apresenta a situação do aluno de acordo com a média das notas
   """
   r = dict()
   r['total'] = len(n)
   r['maior'] = max(n)
   r['menor'] = min(n)
   r['média'] = sum(n)/len(n)
   if sit:
      if r['média'] >=7:
         r['situação'] = 'boa'
      elif r['média'] >= 5:
         r['situação'] = 'razoável'
      else:
         r['situação'] = 'ruim'

   return r


#main program
resp = notas(5.5, 2.6, 9, 8.5, sit = True)
print(resp)
'''

#atividade106
'''
from time import sleep

c = ('\033[m',        # 0 - sem cor
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;40m'    # 6 - branco
   );


def ajuda(com):
   título(f'Acessando o manual do comando \'{com}\'', 0)
   help(com)
   sleep(2)


def título(msg, cor=0):
   tam = len(msg)+4
   print(c[cor], end='')
   print('~'*tam)
   print(f' {msg} ')
   print('~'*tam)
   print(c[0], end='')
   sleep(1)

#main program
comando = ''
while True:
   título('Sistema de ajuda PyHelp  ', 1)
   comando = str(input('Função ou Biblioteca: '))
   if comando.upper().strip() == 'FIM':
      break
   else:
      ajuda(comando)
título('Até logo', 1)
'''

#aula 22

#atividade 107
'''
from utilidades import moeda

valor = float(input('Digite um valor em R$. \n'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10% de {valor} temos {moeda.aumentar(valor,10)}')
print(f'Diminuindo 13% de {valor} temos {moeda.diminuir(valor,13)}')
'''

#atividade 108
'''
from utilidades import moeda

valor = float(input('Digite um valor em R$. \n'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.aumentar(valor,10))}')
print(f'Diminuindo 13% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.diminuir(valor,13))}')
'''

#atividade 109
'''
from utilidades import moeda

valor = float(input('Digite um valor em R$. \n'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando 10% de {moeda.moeda(valor)} temos {moeda.aumentar(valor,10, True)}')
print(f'Diminuindo 13% de {moeda.moeda(valor)} temos {moeda.diminuir(valor,13, True)}')
'''

#atividade 110
'''
from utilidades import moeda

valor = float(input('Digite um valor em R$ \n'))
moeda.resumo(valor,75,25)
'''

#atividade 111 
#Feito

#atividade 112
'''
from utilidadesCeV import dado, moeda

num = dado.leiadinheiro('Digite o preço R% \n')
moeda.resumo(num, 35, 22)
'''

#aula 23
'''
try:
   a = int(input('A: '))
   b = int(input('B: '))
   r = a / b
except (ValueError, TypeError):
   print(f'O problema ocorreu devido aos tipos de dados que você digitou')
except ZeroDivisionError:
   print('Não é possível dividir por zero')
except KeyboardInterrupt:
   print('O usuário prefiiriu não informar os dados')
except Exception as erro:
   print(f'O erro encontrado foi {erro.__cause__}')
else:
   print(f'O resultado foi {r:.2f}')
finally:
   print('Programa concluido')
'''

#atividade 113
'''
def validador():
   try:
      i = int(input('Digite um número inteiro \n'))
      f = float(input('Digite um número fracionado \n'))

   except KeyboardInterrupt:
      print('O usuário não digitou valores')
      return validador()

   except (ValueError, TypeError):
      print('Valores inválido, por favor insirar números.')
      return validador()

   except Exception as error:
      print(f'O erro encotrado foi {error.__cause__}')
      return validador()

   else:
      print(f'O valor inteiro foi {i} e o fracionado {f}')

validador()
'''

#Modelo do professor
'''
def leiaint(msg):
   while True:
         try:
            n = int(input(msg))
         except(ValueError, TypeError):
            print('\033[31m ERRO: por favor, digite um número inteiro válido.\033[m')
            continue
         except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
         else:
            return n

def leiafloat(msg):
   while True:
         try:
            n = float(input(msg))
         except(ValueError, TypeError):
            print('\033[31m ERRO: por favor, digite um número real válido.\033[m')
            continue
         except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
         else:
            return n     

num = leiaint('Digite um valor \n')
print(f'O valor digitado foi {num}')
num2 = leiafloat('Difite um real \n')
print(f'O valor real foi {num2}')
'''

#atividade 114
'''
import urllib
import urllib.request

try:
   site = urllib.request.urlopen('http://www.pudim.com.br')
except:
   print('ERRO!')
else:
   print('Deu tudo certo')
'''

#atividade 115a, b e c
#Projeto realizado