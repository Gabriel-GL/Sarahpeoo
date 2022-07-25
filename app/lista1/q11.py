print("Q11")
vper = float (input ("Qual a velocidade máxima permitida na avenida?"))
vmtr = float (input ("Qual a velocidade máxima que o motorista atingiu?"))
if vmtr > vper and vmtr < vper + 11:
    print ("A multa será no valor de 50 R$")
elif vmtr >= vper + 11 and vmtr < vper + 31:
    print ("A multa será no valor de 100 R$")
elif vmtr >= vper + 31:
    print ("A multa será no valor de 200 R$")