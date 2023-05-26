import os

def cifrado():
 
 Abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',"ñ",'o', 'p', 'q', 'r',"s", 't', 'u', 'v', 'w', 'x', 'y', 'z']

 frase=input("Pon la frase que quieras cifrar,no añadas numeros: ")

 clave=input("Qual clave? ")

 frase=str(frase)

 fin_cifrado=[]
 for letra in frase:
    if letra.isdigit():
       fin_cifrado.append(letra)
    elif letra.isspace():
      fin_cifrado.append(" ")
    else:
      valor=Abecedario.index(letra)
      clave=int(clave)
      valor=int(valor)
      valor+=clave
      if valor>26:
       valor=int(valor)
       nvalor=valor-27
       nvalor=int(nvalor)
       total=Abecedario[nvalor]
       fin_cifrado.append(total)
      else:
       total=Abecedario[valor]
       fin_cifrado.append(total)
 final_cifrado = "".join(str(elemento)for elemento in fin_cifrado)

 print(final_cifrado)
 
    



def descifrar():
   
 Abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',"ñ",'o', 'p', 'q', 'r',"s", 't', 'u', 'v', 'w', 'x', 'y', 'z']

 frase=input("Pon la frase que quieras descifrar,no añadas numeros: ")

 clave=input("Qual clave? ")

 frase=str(frase)

 fin_cifrado=[]
 for letra in frase:
    if letra.isdigit():
       fin_cifrado.append(letra)
    elif letra.isspace():
      fin_cifrado.append(" ")
    else:
      valor=Abecedario.index(letra)
      clave=int(clave)
      valor=int(valor)
      valor-=clave
      if valor>26:
       valor=int(valor)
       nvalor=valor-27
       nvalor=int(nvalor)
       total=Abecedario[nvalor]
       fin_cifrado.append(total)
      else:
       total=Abecedario[valor]
       fin_cifrado.append(total)
 final_cifrado = "".join(str(elemento)for elemento in fin_cifrado)

 print(final_cifrado)
 
    

opcion=input("Que quieres cifrar o descifrar. ")
if opcion=="cifrar":
  cifrado()
elif opcion =="descifrar":
  descifrar()
else:
  print("No has introduido nada. ")
