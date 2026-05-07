#num = [5,2,12,2,9,21]

#print(num)

#print(num[0])
#print(num[1])
#print(num[2])
#print(num[3])
#print(num[4])
#print(num[5])
#####################################################################
# num = [5,7,12,2,9,21]
#
# num[1] = 17
# num[3] = 22
#
# print(num)
#
# num[2]= 1
# num[4]= 29
# print(num)
####################################################################
# num = [5,17,1,22,29,21]
#
# soma=num[5] + num[4]
# subtracao=num[3] - num[1]
# multiplicacao=num[0] * num[5]
# divisao=num[3] / num[2]
#
# print(soma)
# print(subtracao)
# print(multiplicacao)
# print(divisao)
########################################################################
# num=[5,17,1,22,29,21]
# i=0
# while i < len(num):
#     print(num[i]*2)
#     i +=1
# print('-='*30)
# num=[5,17,1,22,29,21]
# for i in range(len(num)):
#     print(num[i]*2)
########################################################################
# apostados=[0,0,0,0,0,0]
# sorteados=[10,15,22,30,45,60]
# for i in range(6):
#     apostados[i]=int(input('Digite um numero:'))
# acertos = 0
# for i in range(6):
#     for j in range(6):
#         if apostados[i] == sorteados[j]:
#             acertos += 1
#
# print('Numeros sorteados:')
# print(sorteados)
#
# print('numeros apostados:')
# print(apostados)
#
# print('Quantidade de acertos:')
# print(acertos)
