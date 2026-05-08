# EXERCÍCIO 1
#
# A = [1, 0, 5, -2, -5, 7]
#
# soma = A[0] + A[1] + A[5]
#
# print("Soma:", soma)
#
# A[4] = 100
#
# for valor in A:
#     print(valor)
#
########################################################
# EXERCÍCIO 2
#
# vetor = []
#
# for i in range(6):
#     numero = int(input(f"Digite o {i+1}º número: "))
#     vetor.append(numero)
#
# print("\nValores digitados:")
#
# for valor in vetor:
#     print(valor)
##########################################################
# EXERCÍCIO 3
#
# vetor = []
# quadrados = []
#
# for i in range(10):
#     numero = float(input(f"Digite o {i+1}º número: "))
#     vetor.append(numero)
#     quadrados.append(numero ** 2)
#
# print("\nVetor original:")
# for valor in vetor:
#     print(valor)
#
# print("\nVetor ao quadrado:")
# for valor in quadrados:
#     print(valor)
###########################################################
# EXERCÍCIO 4
#
# vetor = []
#
# for i in range(8):
#     numero = int(input(f"Digite o valor da posição {i}: "))
#     vetor.append(numero)
#
# x = int(input("Digite a posição X: "))
# y = int(input("Digite a posição Y: "))
#
# soma = vetor[x] + vetor[y]
#
# print("Soma:", soma)
#################################################################
# EXERCÍCIO 5
#
# vetor = []
# pares = 0
#
# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número: "))
#     vetor.append(numero)
#
# for valor in vetor:
#     if valor % 2 == 0:
#         pares += 1
#
# print("Quantidade de números pares:", pares)
#####################################################################
# EXERCÍCIO 6
#
# vetor = []
#
# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número: "))
#     vetor.append(numero)
#
# maior = max(vetor)
# menor = min(vetor)
#
# print("Maior valor:", maior)
# print("Menor valor:", menor)
######################################################################
# EXERCÍCIO 7

# vetor = []
#
# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número: "))
#     vetor.append(numero)
#
# maior = max(vetor)
# posicao = vetor.index(maior)
#
# print("\nVetor:")
# for valor in vetor:
#     print(valor)
#
# print("\nMaior valor:", maior)
# print("Posição:", posicao)
######################################################################
# EXERCÍCIO 8
#
# notas = []
# soma = 0
#
# for i in range(15):
#     nota = float(input(f"Digite a nota do aluno {i+1}: "))
#     notas.append(nota)
#     soma += nota
#
# media = soma / 15
#
# print("Média geral:", media)
###########################################################################
# EXERCÍCIO 9

# vetor = []
# negativos = 0
# soma_positivos = 0
#
# for i in range(10):
#     numero = float(input(f"Digite o {i+1}º número: "))
#     vetor.append(numero)
#
# for valor in vetor:
#     if valor < 0:
#         negativos += 1
#     elif valor > 0:
#         soma_positivos += valor
#
# print("Quantidade de negativos:", negativos)
# print("Soma dos positivos:", soma_positivos)
#################################################################################
# EXERCÍCIO 10

# valores = []
#
# for i in range(5):
#     numero = float(input(f"Digite o {i+1}º valor: "))
#     valores.append(numero)
#
# maior = max(valores)
# menor = min(valores)
# media = sum(valores) / 5
#
# print("\nValores digitados:")
# for valor in valores:
#     print(valor)
#
# print("\nMaior valor:", maior)
# print("Menor valor:", menor)
# print("Média:", media)
##############################################################################
# EXERCÍCIO 11
#
# valores = []
#
# for i in range(5):
#     numero = float(input(f"Digite o {i+1}º valor: "))
#     valores.append(numero)
#
# maior = max(valores)
# menor = min(valores)
#
# pos_maior = valores.index(maior)
# pos_menor = valores.index(menor)
#
# print("Posição do maior valor:", pos_maior)
# print("Posição do menor valor:", pos_menor)
#############################################################################