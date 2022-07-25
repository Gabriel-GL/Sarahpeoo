print("Q12")
n1 = float (input ("informe o 1° número "))
n2 = float (input ("informe o 2° número "))
if n2 > 0 or n2 < 0:
    print (n1 / n2)
elif n2 == 0:
    print ("DIVISÃO POR 0")
else:
    print ("Você digitou algo errado, tente novamente")