# calcul.py - Calculatrice simple v1
print("===Calculatrice Simple===")
print("Opérations disponibles : +, -, *, /")
print()

a = float(input("Entrez le premier nombre : "))
operation = input("Entrez l'opération(+, -, *, /) : ")
b = float(input("Entrez le deuxième nombre : "))

if operation == "+":
    resulat = a + b
elif operation == "-":
    resulat = a - b
elif operation == "*":
    resulat = a * b
elif operation == "/":
    resulat = a / b
else:
    print("Opération inconnue !")
    exit()

print(f"Résultat de l'addition : {a} + {b} = {resulat}")
