import os

def cifrado():
 
 Abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',"ñ",'o', 'p', 'q', 'r',"s", 't', 'u', 'v', 'w', 'x', 'y', 'z']

 frase=input("Pon la frase que quieras cifrar,no añadas numeros: ")

 clave=input("Qual clave? ")

 frase=str(frase)

 cifrar=list(frase)
  
 fin_cifrado=[]

 for letra in cifrar:
    try:
     valor=Abecedario.index(letra)
     clave=int(clave)
     valor=int(valor)
     valor+=clave
     if valor>27:
       valor=int(valor)
       nvalor=valor-27
       nvalor=str(nvalor)
       total=Abecedario[nvalor]
       fin_cifrado.append(total)
     else:
      total=Abecedario[valor]
      fin_cifrado.append(total)
    except:
       valor=0
 final_cifrado="".join(fin_cifrado)

 print(final_cifrado)
 
    



def descifrar():
   
   Abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',"ñ",'o', 'p', 'q', 'r',"s", 't', 'u', 'v', 'w', 'x', 'y', 'z']

   frase=input("Pon la frase que quieras descifrar, no añadas numeros: ")

   
   clave=input("Qual clave? ")
   
   frase=str(frase)

   cifrar=list(frase)

   fin_cifrado=[]

   for letra in cifrar:
    try:
     valor=Abecedario.index(letra)
     valor=int(valor)
     clave=int(clave)
     valor-=clave
     if valor>27:
       valor=int(valor)
       nvalor=valor-27
       total=Abecedario[nvalor]
       fin_cifrado.append(total)
     else:
      total=Abecedario[valor]
      fin_cifrado.append(total)
    except:
       valor=0
   final_cifrado="".join(fin_cifrado)
   print(final_cifrado)
opcion=input("Que quieres cifrar o descifrar. ")
if opcion=="cifrar":
  cifrado()
elif opcion =="descifrar":
  descifrar()
else:
  print("No has introduido nada. ")
