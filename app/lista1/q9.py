print("Q9")
print ("Informe a 1º nota")
nt1 = int (input ())
print ("Informe a 2° nota")
nt2 = int (input ())
print ("Informe a 3° nota")
nt3 = int (input ())
media = (nt1 + nt2 + nt3)/3
print (("sua média é:"),(media))
if (media) >= 6:
    print ("Você foi aprovado")
elif (media) >= 2 and (media) < 6:
    print ("Você está em recuperação")
elif (media) < 2 :
    print ("você foi reprovado")
else :
    ("Você digitou algo de errado, tente novamente ou solicite ajuda de um servidor!")
