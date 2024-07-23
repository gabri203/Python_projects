numero1=int(input("Inserisce  il primo numero : "))
numero2=int(input("Inserisce  il secondo numero : "))
#Pinglinux GitHub
def menu():
    print("1: Somma")
    print("2: Sottrazione")
    print("3: Moltiplicazione")
    print("4: Divisione")
    print("5: Modulo")
    print("0: Per uscire dalla calcolatrice")

menu()

opzione=int(input("Inserisce l'operazione aritmetica che si desidera fare :  "))

while opzione != 0:

    if opzione == 1:
        print("La somma è ",numero1+numero2)

    elif opzione == 2:
        print("La sottrazione è ",numero1-numero2)

    elif opzione == 3:
       print("La Moltiplicazione è ",numero1*numero2)

    elif opzione == 4:
       print("La divizione è ",numero1/numero2)

    elif opzione == 5:
        print("Il modulo è ",numero1%numero2)      
    else:
     print("Operazione non valida o non trovata")

    print()
    menu()
    opzione=int(input("Inserisce l'operazione aritmetica che si desidera fare :  "))

print("Grazie per usare la calcolatrice. Seguimi su Github ")
