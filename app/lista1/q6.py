("Q6")
print ("A quantos anos o senhor(a) fuma?")
AnoFum = float (input ())
DiasFum = ((AnoFum)* 365)
print ("Quantas carteiras consome por dia?")
qtdFum = float (input ())
print ("Informe o valor da carteira na moeda de real:")
valorFum = float (input())
gastottl = float ((DiasFum) * (qtdFum) * (valorFum))
print (("O senhor gastou aproximadamente:"),(gastottl),("reais em cigarros neste período."))