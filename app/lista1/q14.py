print("Q14")
n1 = float (input ("informe o 1° número "))
n2 = float (input ("informe o 2° número "))
n3 = float (input ("informe o 3° número "))
#probabilidades em n1 é maior#
if n1 > n2 and n1 > n3 and n2 > n3:
    print("primeira possibilidade")
    print (n1)
    print (n2)
    print (n3)
elif n1 > n2 and n1 > n3 and n3 > n2:
    print("segunda possibilidade")
    print (n1)
    print (n3)
    print (n2)
#probabilidades em n2 é maior#
elif n2 > n1 and n2 > n3 and n1 > n3:
    print("terceira possibilidade")
    print (n2)
    print (n1)
    print (n3)
elif n2 > n1 and n2 > n3 and n3 > n1:
    print("quarta possibilidade")
    print (n2)
    print (n3)
    print (n1)
#probabilidades em n3 é maior#
elif n3 > n1 and n3 > n2 and n1 > n2:
    print("quinta possibilidade")
    print (n3)
    print (n1)
    print (n2)
elif n3 > n1 and n3 > n2 and n2 > n1:
    print("sexta possibilidade")
    print (n3)
    print (n2)
    print (n1)