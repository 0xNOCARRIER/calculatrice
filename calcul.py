# calcul.py - Calculatrice simple v1
print("===Calculatrice Simple===")
print("Opérations disponibles : +, -, *, /, **")
print()

a = float(input("Entrez le premier nombre : "))
operation = input("Entrez l'opération(+, -, *, /, **) : ")
b = float(input("Entrez le deuxième nombre : "))

if operation == "+":
    resulat = a + b
elif operation == "-":
    resulat = a - b
elif operation == "*":
    resulat = a * b
elif operation == "/":
    if b == 0:
        print("Erreur : division par zéro impossible !")
        exit()
    resulat = a / b
elif operation == "**":
    resultat = a ** b
else:
    print("Opération inconnue !")
    exit()

print(f"Résultat de l'addition : {a} + {b} = {resulat}")
