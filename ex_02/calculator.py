num_1 = int(input("Entrez le premier nombre: "))
num_2 = int(input("Entrez le deuxième nombre: "))
operateur = input("Choisissez un opérateur (+, -, *, /) : ")

if operateur == '+':
    resultat = num_1 + num_2
elif operateur == '-':
    resultat = num_1 - num_2
elif operateur == '*':
    resultat = num_1 * num_2
elif operateur == '/':
    if num_2 != 0:
        resultat = num_1 / num_2
    else:
        resultat = "Erreur: Division par zéro"
else:
    resultat = "Erreur: Opérateur invalide"
    
print(f"Le résultat de {num_1} {operateur} {num_2} est: {resultat}")