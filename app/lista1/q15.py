print("Q15")
n1 = int (input ("informe o 1° número "))
n2 = int (input ("informe o 2° número "))
n3 = int (input ("informe o 3° número "))
n4 = int (input ("informe o 4° número "))
lista = []
resto1 =  (n1 % 2)
resto2 =  (n2 % 2)
resto3 =  (n3 % 2)
resto4 =  (n4 % 2)
if resto1 == 0:
    lista.append(n1)
if resto2 == 0:
    lista.append(n2)
if resto3 == 0:
    lista.append(n3)
if resto4 == 0:
    lista.append(n4)
print(sum(lista))