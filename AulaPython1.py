# # # # Estruturas de Repetição
# # #
# # # Contador:
# # #
# # # cont = 0
# # # while cont <= 10:
# # #     print("Olá!")
# # #     cont += 1
# # # print("Fim.")
# #
##------------
##
# # cont = 0
# # pares = 0
# # while cont < 10:
# #     numero= int(input("Digite um Número inteiro: "))
# #     if numero % 2 == 0:
# #         pares += 1
# #     cont +=1
# # print(f"Você digitou {pares} números pares.")

# -----------

# media = float(input("Informe sua média: "))
# while media < 0 or media > 10:
#     print("Média Invalida")
#     media = float("Digite Novamente: ")
#
# if media >=6:
#     print("Aprovado.")
# elif media >= 4.0:
#     print("Exame.")
# else:
#     print("Reprovado")
#
# ----------
#
# Somadores:
#
# cont = 1
# somador = 0
# while cont <= 10:
#     somador += cont
#     cont += 1
# print(f"A soma dos 10 primeiros números é: {somador}")

#
# num = int(input("Informe um número:"))
# cont = 1
# while cont <= 10:
#     print(f"{num} x {cont} = {num*cont}")
#     cont +=1

print("Cachorro-quente | 100 | R$13,20")
print("Hambúrguer | 101 | R$19,90")
print("Chesseburguer | 102 | R$21,90")
print("Suco Natural | 103 | R$7,00")
print("Refrigerante | 104 | R$6,50")

resp = "sim"
total = 0
while resp == "sim":
    cod = int(input("Informe o código do seu pedido: "))
    match cod:
        case 100:
            quant = int(input("Informe a quantidade: "))
            valor = quant*13.2
        case 101:
            quant = int(input("Informe a quantidade: "))
            valor = quant*19.9
        case 102:
            quant = int(input("Informe a quantidade: "))
            valor = quant*21.9
        case 103:
            quant = int(input("Informe a quantidade: "))
            valor = quant*7
        case 104:
            quant = int(input("Informe a quantidade: "))
            valor = quant*6.5
        case _:
            print(f"Código inválido!")

    total += valor
    resp = input("Deseja continuar seu pedido?: sim ou não")

print(f"O Valor total do seu pedido é: R${total:.2f}")